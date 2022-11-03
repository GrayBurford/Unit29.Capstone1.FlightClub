from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from datetime import datetime

db = SQLAlchemy()

bcrypt = Bcrypt()

def connect_db(app):
    """Connect app to database"""
    db.app = app
    db.init_app(app)

default_user_pic = '../static/default_user_icon.jpg'
default_user_url = 'https://w0.peakpx.com/wallpaper/982/773/HD-wallpaper-anonymous-fawkes-hack-mask.jpg'


class User(db.Model):
    """Make model instance of User class"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(80), unique=True, nullable=False)
    profile_pic = db.Column(db.String(1000), nullable=True, default='../static/default_user_icon.jpg')
    notes = db.Column(db.String(1000), nullable=True)

    flights = db.relationship('Flight', cascade="all, delete")


    def __repr__(self):
        """Return representation of instance of User class."""

        return f"<User #{self.id}: {self.username}, {self.email}, {self.first_name}, {self.last_name}, {self.age}, {self.profile_pic}, {self.notes}>"

    @classmethod
    def register(cls, username, password, first_name, last_name, age, email, profile_pic, notes):
        """Register new user with hashed password. Data sent from view route function to here, then password is hashed, and we return new instance of User at the end."""
        
        hashed_pwd = bcrypt.generate_password_hash(password)
        # now turn bytestring into normal (unicode utf8) string
        hashed_pwd_utf8 = hashed_pwd.decode('utf8', 'ignore')

        user = cls(
            username=username,
            password=hashed_pwd_utf8,
            first_name=first_name,
            last_name=last_name,
            age=age,
            email=email,
            profile_pic=profile_pic,
            notes=notes
        )
        
        return user

    @classmethod
    def authorize(cls, username, password):
        """Authorizes a user if username/password are correct"""

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return False


class Flight(db.Model):
    """Create model instance of Trip class."""

    __tablename__ = "flights"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    airline_name = db.Column(db.String, nullable=False)
    airline_iata_code = db.Column(db.String(2), nullable=False) # DL, UA
    flight_number = db.Column(db.Integer, nullable=False) # 1679
    departure_date = db.Column(db.String, nullable=False) # 10-14-2022
    departure_time = db.Column(db.String, nullable=False) # 0930
    departure_airport_code = db.Column(db.String(3), nullable=False) # EWR
    arrival_date = db.Column(db.String, nullable=False) # 10-14-2022
    arrival_time = db.Column(db.String, nullable=False) # 1045
    arrival_airport_code = db.Column(db.String(3), nullable=False) # ATL
    nonstop = db.Column(db.Boolean, nullable=False, default=True) # True

    user_username = db.Column(db.String, db.ForeignKey('users.username'), nullable=False)

    user = db.relationship('User')

    def __repr__(self):
        """Return representation of Flight class instance."""

        return f"<Trip ID#{self.id}: {self.airline_name}, {self.airline_iata_code}, {self.flight_number}, {self.departure_date}, {self.departure_time}, {self.departure_airport_code}, {self.arrival_date}, {self.arrival_time}, {self.arrival_airport_code}, {self.nonstop}, {self.user_username}>"