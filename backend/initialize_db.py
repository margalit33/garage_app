# initialize_db.py

from app import app, db
from models import User, Car

# Initialize database
with app.app_context():
    db.create_all()

    # Add users
    for i in range(1, 16):
        user = User(username=f'user{i}')
        db.session.add(user)

    # Add cars
    for i in range(1, 16):
        car = Car(make=f'Make{i}', model=f'Model{i}', owner_id=i)
        db.session.add(car)

    db.session.commit()

print("Database initialized and populated with initial data.")
