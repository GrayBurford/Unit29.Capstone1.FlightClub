from sqlalchemy.exc import IntegrityError
from flask import Flask, redirect, render_template, flash, session, request, g, url_for
from models import db, connect_db, User, Flight, Airline, UserAirline
from forms import RegisterUserForm, LoginForm, EditUserProfileForm, SearchFlightForm, AddRewardProgramForm
from flask_debugtoolbar import DebugToolbarExtension
import os, json, requests
from secret import API_KEY


CURR_USER_ID = "" # value is the ID from an instance of User class.

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] =  os.environ.get('DATABASE_URL', "postgresql:///flight_club")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY', 'abc123')
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['WTF_CSRF_ENABLED'] = True

toolbar = DebugToolbarExtension(app)

connect_db(app)

db.create_all()

def get_flight_data(ori, des, date):
    """Fetches flight data for a given route on a given date."""

    url = "https://priceline-com-provider.p.rapidapi.com/v2/flight/departures"

    querystring = {
        "sid":"iSiX639",
        "departure_date":date,
        "adults":"1",
        "origin_airport_code":ori,
        "destination_airport_code":des,
        "number_of_itineraries":"99"
    }

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "priceline-com-provider.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    itineraries = response.json()['getAirFlightDepartures']['results']['result']['itinerary_data']

    itineraries_list = []

    # Filters out nonstop flights from flights with a layover
    for itin in itineraries:
        if itineraries[itin]['slice_data']['slice_0']['info']['connection_count'] == 0:
            itineraries_list.append(itineraries[itin])
            # itineraries_list.append(itineraries[itin]['slice_data']['slice_0']['flight_data']['flight_0'])

    return itineraries_list


##############################################################################
# USER LOGIN/LOGOUT/REGISTER

@app.before_request
def add_user_to_g():
    """If user is logged in, add current user *instance* to Flask Global"""

    if CURR_USER_ID in session:
        g.user = User.query.get(session[CURR_USER_ID])
    else:
        g.user = None


def do_login(user):
    """Log in 'user' which is an instance of the User class."""

    session[CURR_USER_ID] = user.id


def do_logout():
    """Logout 'user' -- an instance of the User class."""

    if CURR_USER_ID in session:
        del session[CURR_USER_ID]


@app.route('/', methods=["GET"])
def home_page():
    """Display anon landing page."""

    return render_template('anon_home.html')


@app.route('/register', methods=['GET', 'POST'])
def register_user():
    """Render register user form."""

    form = RegisterUserForm()

    if form.validate_on_submit():
        try:
            # send data from WTForms to register which is a class function. Would normally make new User instance, but first need to hash pwd with register function, which returns new User instance.
            new_user = User.register(
                username=form.username.data, 
                password=form.password.data, 
                first_name=form.first_name.data, 
                last_name=form.last_name.data, 
                age=form.age.data, 
                email=form.email.data, 
                profile_pic=form.profile_pic.data or User.profile_pic.default.arg, 
                notes=form.notes.data
            )
            
            db.session.add(new_user)
            db.session.commit()

        except IntegrityError as err:
            print(err)
            flash('Username or E-Mail address is already taken! Please choose again.', 'danger')
            return render_template('register.html', form=form)

        # Adds new user's ID to session dictionary for CURR_USER_ID
        # before_request queryies User to save g.user as that user's instance
        do_login(new_user)

        flash(f"Welcome to FlightClub, {new_user.username}! Your account was created successfully!", "success")

        return redirect(url_for('display_user_profile', username=new_user.username))
    
    else:
        return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """Render login form, or log a user in."""

    airlines = Airline.query.all()

    if g.user:
        flash(f'You are already logged in as {g.user.username}! Logout first if you want to log in as a different user.', "danger")

    form = LoginForm()

    if form.validate_on_submit():
        try:
            user = User.authorize(form.username.data, form.password.data)

            if user:
                do_login(user)
                flash(f"Welcome back to FlightClub, {user.username}!", "success")
                return redirect(url_for('display_user_profile', username=user.username))
        except IntegrityError as err:
            print(err)
            flash("Your username or password is incorrect! Please try again.", "danger")
            return redirect(url_for('login'))

    else:
        return render_template('login.html', form=form, airlines=airlines)


@app.route('/logout', methods=['GET'])
def logout():
    """Handle logout of a user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    if CURR_USER_ID in session:
        user = User.query.get_or_404(session[CURR_USER_ID])
        flash(f"Good-bye {user.username}, you logged out successfully.", "success")
        do_logout()
        return redirect(url_for('home_page'))
    else:
        flash("You can't logout, because you're not logged in!", "warning")
        return redirect(url_for('login'))


@app.route('/faq', methods=['GET'])
def faq():
    """Render FAQ page."""

    return render_template('faq.html')

##############################################################################
# USER ROUTES

@app.route('/users/<username>', methods=['GET', 'POST'])
def display_user_profile(username):
    """Renders a user's personal profile page."""

    if CURR_USER_ID not in session:
        flash('Access unauthorized.', 'danger')
        return redirect(url_for('home_page'))

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect(url_for('home_page'))

    user = User.query.filter_by(username=username).first()

    return render_template('user_profile.html', user=user)


@app.route('/users/editprofile', methods=["GET", "POST"])
def edit_profile():
    """Update profile for current user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect(url_for('home_page'))

    user = g.user

    # Populates WTForms values with pre-existing DB info.
    form = EditUserProfileForm(obj=user)

    if form.validate_on_submit():
        try:
            if User.authorize(user.username, form.password.data):
                user.username = form.username.data
                user.first_name = form.first_name.data
                user.last_name = form.last_name.data
                user.age = form.age.data
                user.email = form.email.data
                user.profile_pic = form.profile_pic.data or User.profile_pic.default.arg
                user.notes = form.notes.data

                db.session.commit()
                return redirect(url_for('display_user_profile', username=user.username))
        except IntegrityError as err:
            print(err)
            flash("Wrong password! Please try again.", 'danger')

    return render_template('edit_profile.html', form=form, user=user)


@app.route('/users/delete', methods=["POST"])
def delete_user():
    """Delete user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect(url_for('home_page'))

    flash(f"You've successfully deleted your account, user-previously-known-as '{g.user.username}'. Please consider signing up again to enjoy all FlightClub's benefits.", "danger")

    do_logout()

    db.session.delete(g.user)
    db.session.commit()

    return redirect(url_for('home_page'))


@app.route('/users/<username>/rewards', methods=['GET', 'POST'])
def airline_programs(username):
    """Render page to add/edit/remove airline frequent flyer accounts."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect(url_for('home_page'))

    user = g.user

    form = AddRewardProgramForm()

    ow = [(0, '-- select an airline --')] + [(a.id, f'{a.name} ({a.reward_program})') for a in Airline.query.filter_by(alliance='Oneworld').all()]

    st = [(0, '-- select an airline --')] + [(a.id, f'{a.name} ({a.reward_program})') for a in Airline.query.filter_by(alliance='Sky Team').all()]
    
    sa = [(0, '-- select an airline --')] + [(a.id, f'{a.name} ({a.reward_program})') for a in Airline.query.filter_by(alliance='Star Alliance').all()]

    form.oneworld.choices = ow
    form.skyteam.choices = st
    form.staralliance.choices = sa

    if form.validate_on_submit():
        try:
            NOT_ZERO_ID = int(form.oneworld.data) or int(form.skyteam.data) or int(form.staralliance.data)

            new_program = UserAirline(
                user_id=user.id, 
                airline_id=NOT_ZERO_ID, 
                acct_number=form.acct_number.data
            )

            db.session.add(new_program)
            db.session.commit()

            return redirect(url_for('airline_programs', user=user, username=username, form=form))

        except IntegrityError as err:
            print(err)
            flash('Something went wrong. Please check your selections.', 'danger')

    return render_template('reward_programs.html', form=form, user=user, username=username)


@app.route('/flight/<int:flight_id>/delete', methods=["GET"])
def delete_flight(flight_id):
    """Delete a user's saved flight."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect(url_for('home_page'))

    flight = Flight.query.get_or_404(flight_id)
    db.session.delete(flight)
    db.session.commit()

    flash("You successfully deleted that saved flight", "success")    
    return redirect(f'/users/{g.user.username}')


##############################################################################
# FLIGHT ROUTES

@app.route('/search', methods=['GET', 'POST'])
def flight_search():
    """Display flight search form"""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect(url_for('home_page'))

    form = SearchFlightForm()

    if form.validate_on_submit():
        try:
            origin = form.data['origin']
            destination = form.data['destination']
            date = form.data['date']
            print(f"origin = {origin}, destination = {destination}, date = {date}")

            itins = get_flight_data(origin, destination, date)
            # EX: itins = get_flight_data("EWR", "ATL", "2022-11-21")

            flash(f"Seach successful and results compiled for viewing below.", "success")
            return render_template('search.html', form=form, itins=itins)
        except IntegrityError as err:
            print(err)
            flash('Please fill in the required fields: Origin, Destination, and Date', 'danger')

    return render_template('search.html', form=form)

@app.route('/saveflight', methods=['POST'])
def save_flight():
    """Save a chosen flight's data to user's profile"""

    if CURR_USER_ID in session:
        user = User.query.get_or_404(session[CURR_USER_ID])

    if request.method == 'POST':
        session['airline_name'] = request.form['airline_name']
        session['airline_iata_code'] = request.form['airline_iata_code']
        session['flight_number'] = request.form['flight_number']
        session['departure_date'] = request.form['departure_date']
        session['departure_time'] = request.form['departure_time']
        session['departure_airport_code'] = request.form['departure_airport_code']
        session['arrival_date'] = request.form['arrival_date']
        session['arrival_time'] = request.form['arrival_time']
        session['arrival_airport_code'] = request.form['arrival_airport_code']
        session['nonstop'] = request.form['nonstop']
        session['price'] = request.form['price']

        flight = Flight(
            airline_name=session['airline_name'],
            airline_iata_code=session['airline_iata_code'],
            flight_number=session['flight_number'],
            departure_date=session['departure_date'],
            departure_time=session['departure_time'],
            departure_airport_code=session['departure_airport_code'],
            arrival_date=session['arrival_date'],
            arrival_time=session['arrival_time'],
            arrival_airport_code=session['arrival_airport_code'],
            nonstop=bool(session['nonstop']),
            price=session['price'],
            user_username=user.username
        )

        db.session.add(flight)
        db.session.commit()
        print(flight)

        return render_template('add_flight.html', user=user, flight=flight)   
    
    else:
        return redirect(url_for('save_flight'))


@app.route('/rewards/<int:user_id>/<int:airline_id>/delete', methods=["GET"])
def delete_program(user_id, airline_id):
    """Delete a user's saved airline reward program."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect(url_for('home_page'))

    user = g.user

    try:
        program = UserAirline.query.filter_by(user_id=1, airline_id=4).one()
        print(program)

        db.session.delete(program)
        db.session.commit()
    except IntegrityError as err:
        print(err)
        flash('Cannot delete this program.', 'danger')

    flash("You successfully deleted that saved airline program", "success")    
    return redirect(f'/users/{user.username}/rewards')
    

# *********************************************************************
# RETURN DISPLAYNAME, AIRPORT IATA, STATE, ETC
# url = "https://priceline-com-provider.p.rapidapi.com/v1/flights/locations"
# querystring = {"name":"EWR"}
# headers = {
# 	"X-RapidAPI-Key": "fa1746626bmsh7be87ec830a5eccp143408jsnb247fa783472",
# 	"X-RapidAPI-Host": "priceline-com-provider.p.rapidapi.com"}
# response = requests.request("GET", url, headers=headers, params=querystring)
# print(response.text)
# *********************************************************************


# *********************************************************************
# DOWNLOAD LIST OF AIRPORTS WITH IATA CODES FOR FLIGHT SEARCH
# url = "https://priceline-com-provider.p.rapidapi.com/v2/flight/downloadAirports"
# querystring = {"limit":"9999"}
# headers = {
# 	"X-RapidAPI-Key": "fa1746626bmsh7be87ec830a5eccp143408jsnb247fa783472",
# 	"X-RapidAPI-Host": "priceline-com-provider.p.rapidapi.com"}
# response = requests.request("GET", url, headers=headers, params=querystring)
# print(response.json()['getSharedBOF2.Downloads.Air.Airports']['results'])
# *********************************************************************




# Python requests example:
# ***********************************************************
# import requests
# res = requests.get(
#             "https://itunes.apple.com/search",
#             params={"term": "billy bragg", "limit": 3}
#        )

# ***********************************************************
# from flask import Flask, render_template, request
# import requests

# API_BASE_URL = "http://www.mapquestapi.com/geocoding/v1"

# app = Flask(__name__)

# def request_coords(location):
#     """Return {lat,lng} from MapQuest for given location."""

#     key = '4WiuDGgyNC6lAp04txicEbLMUf53z5O0'
#     url = f"{API_BASE_URL}/address?key={key}&location={location}"

#     response = requests.get(url)
#     r = response.json()

#     lat = r['results'][0]['locations'][0]['latLng']['lat']
#     lng = r['results'][0]['locations'][0]['latLng']['lng']

#     return {"lat": lat, "lng": lng}