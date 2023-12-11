# IRango API Python

This API you can do:
* Get all the restaurants
* Create a new restaurants
* Get a restaurant
* Update a restaurant
* Delete a restaurant
* Get all restaurant products
* Create restaurant product
* Update restaurant product
* Delete restaurant product

### Tech Stack
* Python 3.11
* MongoDB
* Redis

### First Step
* If you have docker on your machine, run the code below and go to the section [How to use the API](#-How-to-use-the-API).
* We will use docker compose to manager our containers with our application and Redis and MongoDB.
```
docker-compose up -d
```

* Creates a virtual environment for the project.
```
python -m venv venv
```
* Install all packages with poetry.
```
pip install poetry
```
```
poetry install 
```
* Creates a .env file and use the .env_example file as a model.

### Running the API
```
python main.py
```

### How to use the API

* For all CRUD operations you'll need an access token. See how to get an token in User Routes.

### Restaurants Routes
#### Restaurant Model

```
{
  "name": str,
  "address": {
    "street_name": str,
    "street_number": str
  },
  "business_hours": {
    "business_day": str,
    "weekend": str
  }
}
```

* Creates a restaurant

Send in the request body, and the restaurant info. Use the restaurant model.

```
http://localhost:5000/restaurants/
```
* Get all Restaurants.


Send in the request page, size, sort and name. To receive your Paginated data.

```
http://localhost:5000/restaurants?name=name&size=size&page=page&sort=sort
```
* Get a specific restaurants

```
http://localhost:5000/restaurants/restaurant_id
```
* Update a restaurants

Send the restaurant data you want to update in the body of your request. Use the Restaurant model for this.
```
http://localhost:5000/restaurants/restaurant_id
```

* Delete a restaurants
```
http://localhost:5000/restaurants/restaurant_id
```
### Products Routes

#### Product Model
```
{
  "name": str,
  "price": float,
  "category": str,
  "promotion": {
    "active": bool,
    "special_price": float,
    "description": str,
    "business_day": str,
    "weekend": str
  }
}
```

* Create a product
Send the product you want to create in the body of your request. Use the Product model for this.
```
http://localhost:5000/resturants/resturant_id/products
```
* Get all products

```
http://localhost:5000/resturants/resturant_id/products
```
* Get a specific product
```
http://localhost:5000/resturants/resturant_id/products/product_id
```
### Users Routes

#### Users Model
```
{
    "username": str,
    "email": str,
    "password": str
}
```

* Create am user

Create an user. And receive an access token to execute operations.

```
http://localhost:5000/register
```
* Login

Login in the application.

```
http://localhost:5000/login
```
* Logout

Logout in the application.


```
http://localhost:5000/logout
```

### API Swagger 
* You can access all API routes and also test all API functionalities.
```
http://localhost:5000/docs
```

### Tests
* Run unit tests
```
pytest tests
```

#### License

This project is under license [MIT](/LICENSE).