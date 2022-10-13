from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, TextAreaField, IntegerField
from wtforms.validators import InputRequired, Length


class RegisterUserForm(FlaskForm):
    """Form to register new user"""

    username = StringField("Username", validators=[InputRequired(message='Enter a Username.'), Length(min=6, max=50, message='Length between 6-50 characters.')])

    password = PasswordField("Password", validators=[InputRequired(message='Enter a password.'), Length(min=6, max=30, message='Length between 6-30 characters.')])

    first_name = StringField("First name", validators=[InputRequired(message='Enter your first name.'), Length(min=2, max=30, message='Length between 2-30 characters.')])
    
    last_name = StringField("Last name", validators=[InputRequired(message='Enter your last name.'), Length(min=2, max=50, message='Length between 2-50 characters.')])

    age = IntegerField("Age")

    email = EmailField("Email Address", validators=[InputRequired(message='Enter your email address.'), Length(min=6, max=80, message='Length between 6-80 characters.')])

    profile_pic = StringField("Profile picture")

    notes = TextAreaField("Miscellaneous notes about this user")


class LoginForm(FlaskForm):
    """Form to login existing user."""

    username = StringField("Username", validators=[InputRequired(message='Enter your Username.'), Length(min=6, max=50, message='Length between 6-50 characters.')])

    password = PasswordField("Password", validators=[InputRequired(message='Enter your password.'), Length(min=6, max=30, message='Length between 6-30 characters.')])


class EditUserProfileForm(FlaskForm):
    """Edit user's profile form."""

    username = StringField("Username", validators=[InputRequired(message='Enter a Username.'), Length(min=6, max=50, message='Length between 6-50 characters.')])

    password = PasswordField("Password", validators=[InputRequired(message='Enter a password.'), Length(min=6, max=30, message='Length between 6-30 characters.')])

    first_name = StringField("First name", validators=[InputRequired(message='Enter your first name.'), Length(min=2, max=30, message='Length between 2-30 characters.')])
    
    last_name = StringField("Last name", validators=[InputRequired(message='Enter your last name.'), Length(min=2, max=50, message='Length between 2-50 characters.')])

    age = IntegerField("(Optional) Age")

    email = EmailField("Email Address", validators=[InputRequired(message='Enter your email address.'), Length(min=6, max=80, message='Length between 6-80 characters.')])

    profile_pic = StringField("(Optional) Profile picture")

    notes = TextAreaField("(Optional) Miscellaneous notes about this user")



