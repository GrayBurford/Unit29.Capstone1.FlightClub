from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, TextAreaField, IntegerField, DateField, SelectField
from wtforms.validators import InputRequired, Length

###########################################################################
# USER FORMS ##############################################################
###########################################################################
class RegisterUserForm(FlaskForm):
    """Form to register new user"""

    username = StringField("Username", validators=[InputRequired(message='Enter a Username.'), Length(min=3, max=50, message='Length between 3-50 characters.')])

    password = PasswordField("Password", validators=[InputRequired(message='Enter a password.'), Length(min=6, max=80, message='Length must be between 6 and 80 characters.')])

    first_name = StringField("First name", validators=[InputRequired(message='Enter your first name.'), Length(min=2, max=50, message='Length between 2-30 characters.')])
    
    last_name = StringField("Last name", validators=[InputRequired(message='Enter your last name.'), Length(min=2, max=50, message='Length between 2-50 characters.')])

    age = IntegerField("(Optional) Age")

    email = EmailField("Email Address", validators=[InputRequired(message='Enter your email address.'), Length(min=6, max=80, message='Length between 6-80 characters.')])

    profile_pic = StringField("(Optional) Profile picture")

    notes = TextAreaField("(Optional) Miscellaneous notes about this user")


class EditUserProfileForm(FlaskForm):
    """Edit user's profile form."""

    username = StringField("Username", validators=[InputRequired(message='Enter a Username.'), Length(min=3, max=50, message='Length between 3-50 characters.')])

    password = PasswordField("Password", validators=[InputRequired(message='Enter a password.'), Length(min=6, max=80, message='Length between 6-80 characters.')])

    first_name = StringField("First name", validators=[InputRequired(message='Enter your first name.'), Length(min=2, max=30, message='Length between 2-30 characters.')])
    
    last_name = StringField("Last name", validators=[InputRequired(message='Enter your last name.'), Length(min=2, max=50, message='Length between 2-50 characters.')])

    age = IntegerField("(Optional) Age")

    email = EmailField("Email Address", validators=[InputRequired(message='Enter your email address.'), Length(min=6, max=80, message='Length between 6-80 characters.')])

    profile_pic = StringField("(Optional) Profile picture")

    notes = TextAreaField("(Optional) Miscellaneous notes about this user")


class LoginForm(FlaskForm):
    """Form to login existing user."""

    username = StringField("Username", validators=[InputRequired(message='Enter your Username.'), Length(min=3, max=50, message='Length between 3-50 characters.')])

    password = PasswordField("Password", validators=[InputRequired(message='Enter your password.'), Length(min=6, max=80, message='Length between 6-80 characters.')])


###########################################################################
# FLIGHT FORMS ############################################################
###########################################################################
class SearchFlightForm(FlaskForm):
    """Form for searching and generating flight info."""

    origin = StringField("Origin", validators=[InputRequired(message='Please enter a 3 character airport IATA code'), Length(min=3, max=3, message='Airport IATA code must be exactly 3 characters long.')])

    destination = StringField("Destination", validators=[InputRequired(message='Please enter a 3 character airport IATA code'), Length(min=3, max=3, message='Airport IATA code must be exactly 3 characters long.')])

    date = DateField("Departure Date", validators=[InputRequired(message='Please choose a departure date.')])



###########################################################################
# REWARD PROGRAM FORMS ####################################################
###########################################################################

class AddRewardProgramForm(FlaskForm):
    """Form to add new airline reward program to user profile."""

    oneworld = SelectField('Oneworld Members')

    staralliance = SelectField('Star Alliance Members')

    skyteam = SelectField('Sky Team Members')

    acct_number = StringField("Account Number", validators=[InputRequired(message='Please enter the program\'s account number')])
    
    notes = StringField("Additional Notes")


###########################################################################
# CREDIT CARD FORMS #######################################################
###########################################################################





