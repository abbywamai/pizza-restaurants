# pizza-restaurants

# Pizza Restaurants API

This is a Flask-based API for managing pizza restaurants and their associated pizzas. It provides routes for retrieving restaurant information, pizzas, and creating new associations between restaurants and pizzas.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python (3.x recommended)
- Postman (or any API testing tool)

### Installation

1. **Clone the repository:**


2. **Navigate to the project directory:**


3. **Create a virtual environment (optional but recommended):**

4. **Activate the virtual environment:**

5. **Install the required packages:**

   
### Running the ApplicationThe API will be accessible at `http://127.0.0.1:5555`.

## Routes

### GET /restaurants

Returns a list of all restaurants along with their details.

### GET /restaurants/:id
Returns details of a specific restaurant along with its associated pizzas.

### GET /pizzas
Returns a list of all pizzas along with their details.

### POST /restaurant_pizzas
Creates a new association between a restaurant and a pizza.

### Contributing
Feel free to contribute to this project by forking and creating pull requests. Please make sure to follow the existing code style and add relevant tests if applicable.

### License
This project is licensed under the MIT License.


