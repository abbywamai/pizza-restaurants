from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

from models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


migrate = Migrate(app, db)

db.init_app(app)

from models import Restaurant, Pizza, RestaurantPizza

# root route
@app.route('/', methods=['GET'])
def index():
    return " Pizza Restaurant API!"



# Routes
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    data = [{
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address
    } for restaurant in restaurants]
    return jsonify(data)


@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant is None:
        return jsonify({'error': 'Restaurant not found'}), 404
    data = {
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': [{
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        } for pizza in restaurant.pizzas]
    }
    return jsonify(data)


@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant is None:
        return jsonify({'error': 'Restaurant not found'}), 404

    
    RestaurantPizza.query.filter_by(restaurant_id=id).delete()
    
    
    db.session.delete(restaurant)
    db.session.commit()

    return '', 204


@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    data = [{
        'id': pizza.id,
        'name': pizza.name,
        'ingredients': pizza.ingredients
    } for pizza in pizzas]
    return jsonify(data)


@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    # Validate input data 
    if not all([price, pizza_id, restaurant_id]):
        return jsonify({'errors': ['Missing required fields']}), 400

    
    try:
        new_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(new_pizza)
        db.session.commit()
        pizza = Pizza.query.get(pizza_id)
        return jsonify({
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        }), 201
    except Exception as e:
        return jsonify({'errors': [str(e)]}), 400

if __name__ == '__main__':
    app.run(port=5555)
