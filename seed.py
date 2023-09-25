
#!/usr/bin/env python3

from random import choice as rc
from random import randint
from faker import Faker

from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

fake = Faker()

# Seed Restaurants
def seed_restaurants():
    for _ in range(5):
        restaurant = Restaurant(
            name=fake.company(),
            address=fake.address()
        )
        db.session.add(restaurant)
    db.session.commit()

# Seed Pizzas
def seed_pizzas():
    pizza_data = [
        {"name": "Margherita", "ingredients": "Tomato, Mozzarella, Basil"},
        {"name": "Pepperoni", "ingredients": "Tomato, Mozzarella, Pepperoni"},
        {"name": "Vegetarian", "ingredients": "Tomato, Mozzarella, Vegetables"}
    ]

    for pizza_info in pizza_data:
        pizza = Pizza(**pizza_info)
        db.session.add(pizza)
    db.session.commit()

def seed_restaurant_pizzas():
    for restaurant in Restaurant.query.all():
        for pizza in Pizza.query.all():
            restaurant_pizza = RestaurantPizza(
                price=randint(1, 30),  # Generate a random price between 1 and 30
                restaurant_id=restaurant.id,
                pizza_id=pizza.id
            )
            db.session.add(restaurant_pizza)
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        seed_restaurants()
        seed_pizzas()
        seed_restaurant_pizzas()

