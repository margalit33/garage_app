# Garage Management Application

This Flask application manages a virtual garage with users and cars. It provides RESTful API endpoints to perform CRUD operations on users and cars stored in a database.

## Features

- View all users and their details.
- View all cars and their details, including their owners.
- Add, update, or delete users and cars.

## Technologies Used

- Flask: Web framework for Python.
- SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library.
- Flask-SQLAlchemy: Flask extension for SQLAlchemy integration.
- Flask-CORS: Flask extension for handling Cross-Origin Resource Sharing (CORS).

## Setup

1. **Clone the repository:**

   git clone <https://github.com/margalit33/garage_app>
   cd garage_management_app

2. **Install dependencies:**
   pip install -r requirements.txt

3. **Database Setup**:

   Modify config.py to specify your database URI (SQLite, PostgreSQL, etc.).
   Initialize the database by running:

   python initialize_db.py

4. **Run the Flask application**:
   python app.py


5. **Access the API Endpoints**:

      Users
      GET /users: Get all users.
      GET /users/<user_id>: Get details of a specific user.
      POST /users: Create a new user.
      PUT /users/<user_id>: Update an existing user.
      DELETE /users/<user_id>: Delete an existing user.

            
      Cars
      GET /cars: Get all cars.
      GET /cars/<car_id>: Get details of a specific car.
      POST /cars: Create a new car.
      PUT /cars/<car_id>: Update an existing car.
      DELETE /cars/<car_id>: Delete an existing car.









