from flask import Flask, redirect, render_template, flash, session
from models import db, connect_db, User
from forms import RegisterUserForm, LoginForm, EditUserProfileForm
from flask_debugtoolbar import DebugToolbarExtension
import os, json, requests
from amadeus import Client, ResponseError

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

# Cheat Sheet:
# https://possible-quilt-2ff.notion.site/Cheat-sheet-e059caf4fcd342b78705f9f3d6f88f1d
API_BASE_URL = "https://test.api.amadeus.com"
API_KEY = "gW89o76UnCoZqBPWxvo6yLPhNqfQaGtf"
API_SECRET = "RUaGyaznry7uGL5E"
API_ACCESS_TOKEN = ""

# Obtain 30 minute access token
    # response = requests.post(f'{API_BASE_URL}/v1/security/oauth2/token',
    #                     headers = {"Content-Type" : "application/x-www-form-urlencoded"},
    #                     data = f"grant_type=client_credentials&client_id={API_KEY}&client_secret={API_SECRET}"
    #                     )

    # API_ACCESS_TOKEN = response.json()["access_token"]
    # print(response.json()["access_token"])
    # TOKEN_EXPIRATION = response.json()["expires_in"]

amadeus = Client(
    client_id = API_KEY,
    client_secret = API_SECRET
)

@app.route('/', methods=["GET"])
def home_page():
    """Display anon landing page."""

    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode='EWR',
            destinationLocationCode='ATL',
            departureDate='2022-10-14',
            adults=1,
            max=5,
            travelClass='ECONOMY',
            currencyCode='USD'
            # includedAirlineCodes='UA'
            # nonStop=True DOES NOT WORK!!!
            # SPIRIT FLIGHT TIMES ARE WRONG
        )
        print(response.data)
    except ResponseError as error:
        print(error)

    flash("Welcome to the home page", "primary")
    return render_template('base.html', response=response)

@app.route('/register', methods=['GET', 'POST'])
def register_user():
    """Render register user form."""

    # if "username" in session (or g??)
    #     return redirect('/')

    form = RegisterUserForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        age = form.age.data
        email = form.email.data
        profile_pic = form.profile_pic.data
        notes = form.notes.data

        # send data from WTForms to register which is a class function. Would normally make new User instance, but first need to hash pwd with register function, which returns new User instance.
        new_user = User.register(username, password, first_name, last_name, age, email, profile_pic, notes)
        db.session.commit()

        session['username'] = new_user.username
        flash(f"Welcome to FlightClub, {new_user.username}! Your account was created successfully!", "success")
        return redirect('/search')
    
    else:
        return render_template('register.html', form=form)

@app.route('/search', methods=['GET'])
def flight_search():
    """Display flight search form"""

    return render_template('search.html')


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


# @app.route('/')
# def home_route():
#     """Show form asking for location to geocode."""

#     return render_template('home.html')


# @app.route('/coords', methods=["POST"])
# def get_coords():
#     """Handle form submission; return form, showing lat/lng from submission."""
#     city = request.form['city']
#     coords = request_coords(city)

#     return render_template('home.html', coords=coords)


# *******************************************
# EXAMPLE JSON RESPONSE FROM FLIGHT OFFERS SEARCH:

# {
#   "meta": {
#     "count": 2,
#     "links": {
#       "self": "https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=EWR&destinationLocationCode=SEA&departureDate=2022-10-14&adults=1&travelClass=ECONOMY&nonStop=true&max=2"
#     }
#   },
#   "data": [
#     {
#       "type": "flight-offer",
#       "id": "1",
#       "source": "GDS",
#       "instantTicketingRequired": false,
#       "nonHomogeneous": false,
#       "oneWay": false,
#       "lastTicketingDate": "2022-10-04",
#       "numberOfBookableSeats": 7,
#       "itineraries": [
#         {
#           "duration": "PT6H19M",
#           "segments": [
#             {
#               "departure": {
#                 "iataCode": "EWR",
#                 "terminal": "B",
#                 "at": "2022-10-14T17:45:00"
#               },
#               "arrival": {
#                 "iataCode": "SEA",
#                 "at": "2022-10-14T21:04:00"
#               },
#               "carrierCode": "AS",
#               "number": "15",
#               "aircraft": {
#                 "code": "7M9"
#               },
#               "operating": {
#                 "carrierCode": "AS"
#               },
#               "duration": "PT6H19M",
#               "id": "1",
#               "numberOfStops": 0,
#               "blacklistedInEU": false
#             }
#           ]
#         }
#       ],
#       "price": {
#         "currency": "EUR",
#         "total": "238.46",
#         "base": "208.00",
#         "fees": [
#           {
#             "amount": "0.00",
#             "type": "SUPPLIER"
#           },
#           {
#             "amount": "0.00",
#             "type": "TICKETING"
#           }
#         ],
#         "grandTotal": "238.46"
#       },
#       "pricingOptions": {
#         "fareType": [
#           "PUBLISHED"
#         ],
#         "includedCheckedBagsOnly": false
#       },
#       "validatingAirlineCodes": [
#         "AS"
#       ],
#       "travelerPricings": [
#         {
#           "travelerId": "1",
#           "fareOption": "STANDARD",
#           "travelerType": "ADULT",
#           "price": {
#             "currency": "EUR",
#             "total": "238.46",
#             "base": "208.00"
#           },
#           "fareDetailsBySegment": [
#             {
#               "segmentId": "1",
#               "cabin": "ECONOMY",
#               "fareBasis": "NH7OAVBN",
#               "brandedFare": "SV",
#               "class": "X",
#               "includedCheckedBags": {
#                 "quantity": 0
#               }
#             }
#           ]
#         }
#       ]
#     },
#     {
#       "type": "flight-offer",
#       "id": "2",
#       "source": "GDS",
#       "instantTicketingRequired": false,
#       "nonHomogeneous": false,
#       "oneWay": false,
#       "lastTicketingDate": "2022-10-04",
#       "numberOfBookableSeats": 7,
#       "itineraries": [
#         {
#           "duration": "PT6H19M",
#           "segments": [
#             {
#               "departure": {
#                 "iataCode": "EWR",
#                 "terminal": "B",
#                 "at": "2022-10-14T19:09:00"
#               },
#               "arrival": {
#                 "iataCode": "SEA",
#                 "at": "2022-10-14T22:28:00"
#               },
#               "carrierCode": "AS",
#               "number": "715",
#               "aircraft": {
#                 "code": "7M9"
#               },
#               "operating": {
#                 "carrierCode": "AS"
#               },
#               "duration": "PT6H19M",
#               "id": "2",
#               "numberOfStops": 0,
#               "blacklistedInEU": false
#             }
#           ]
#         }
#       ],
#       "price": {
#         "currency": "EUR",
#         "total": "238.46",
#         "base": "208.00",
#         "fees": [
#           {
#             "amount": "0.00",
#             "type": "SUPPLIER"
#           },
#           {
#             "amount": "0.00",
#             "type": "TICKETING"
#           }
#         ],
#         "grandTotal": "238.46"
#       },
#       "pricingOptions": {
#         "fareType": [
#           "PUBLISHED"
#         ],
#         "includedCheckedBagsOnly": false
#       },
#       "validatingAirlineCodes": [
#         "AS"
#       ],
#       "travelerPricings": [
#         {
#           "travelerId": "1",
#           "fareOption": "STANDARD",
#           "travelerType": "ADULT",
#           "price": {
#             "currency": "EUR",
#             "total": "238.46",
#             "base": "208.00"
#           },
#           "fareDetailsBySegment": [
#             {
#               "segmentId": "2",
#               "cabin": "ECONOMY",
#               "fareBasis": "NH7OAVBN",
#               "brandedFare": "SV",
#               "class": "X",
#               "includedCheckedBags": {
#                 "quantity": 0
#               }
#             }
#           ]
#         }
#       ]
#     }
#   ],
#   "dictionaries": {
#     "locations": {
#       "EWR": {
#         "cityCode": "NYC",
#         "countryCode": "US"
#       },
#       "SEA": {
#         "cityCode": "SEA",
#         "countryCode": "US"
#       }
#     },
#     "aircraft": {
#       "7M9": "BOEING 737 MAX 9"
#     },
#     "currencies": {
#       "EUR": "EURO"
#     },
#     "carriers": {
#       "AS": "ALASKA AIRLINES"
#     }
#   }
# }