from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db, User, Car
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
db.init_app(app)

# Routes for users
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{
        'id': user.id,
        'username': user.username
    } for user in users])

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({
        'id': user.id,
        'username': user.username
    })

@app.route('/users', methods=['POST'])
def create_user():
    if not request.json or 'username' not in request.json:
        abort(400)

    username = request.json['username']
    new_user = User(username=username)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully', 'id': new_user.id}), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)

    if not request.json:
        abort(400)

    if 'username' in request.json:
        user.username = request.json['username']

    db.session.commit()

    return jsonify({'message': 'User updated successfully'}), 200

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)

    db.session.delete(user)
    db.session.commit()

    return jsonify({'message': 'User deleted successfully'}), 200

# Routes for cars
@app.route('/cars', methods=['GET'])
def get_cars():
    cars = Car.query.all()
    return jsonify([{
        'id': car.id,
        'make': car.make,
        'model': car.model,
        'owner_id': car.owner_id
    } for car in cars])

@app.route('/cars/<int:car_id>', methods=['GET'])
def get_car(car_id):
    car = Car.query.get_or_404(car_id)
    return jsonify({
        'id': car.id,
        'make': car.make,
        'model': car.model,
        'owner_id': car.owner_id
    })

@app.route('/cars', methods=['POST'])
def create_car():
    if not request.json or 'make' not in request.json or 'model' not in request.json or 'owner_id' not in request.json:
        abort(400)

    make = request.json['make']
    model = request.json['model']
    owner_id = request.json['owner_id']

    new_car = Car(make=make, model=model, owner_id=owner_id)

    db.session.add(new_car)
    db.session.commit()

    return jsonify({'message': 'Car created successfully', 'id': new_car.id}), 201

@app.route('/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    car = Car.query.get_or_404(car_id)

    if not request.json:
        abort(400)

    if 'make' in request.json:
        car.make = request.json['make']
    if 'model' in request.json:
        car.model = request.json['model']
    if 'owner_id' in request.json:
        car.owner_id = request.json['owner_id']

    db.session.commit()

    return jsonify({'message': 'Car updated successfully'}), 200

@app.route('/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    car = Car.query.get_or_404(car_id)

    db.session.delete(car)
    db.session.commit()

    return jsonify({'message': 'Car deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)

