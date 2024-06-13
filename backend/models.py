from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """
    User model represents a user in the system.

    Attributes:
        id (int): Unique identifier for the user.
        username (str): Username of the user.
        cars (relationship): One-to-many relationship with Car model, representing cars owned by the user.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)


class Car(db.Model):
    """
    Car model represents a car in the system.

    Attributes:
        id (int): Unique identifier for the car.
        make (str): Make of the car.
        model (str): Model of the car.
        owner_id (int): Foreign key referencing the User who owns the car.
        owner (relationship): Relationship with User model, representing the owner of the car.
    """
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50), nullable=False)
    model = db.Column(db.String(50), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    owner = db.relationship('User', backref=db.backref('cars', lazy=True))

