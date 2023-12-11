from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint
from flask import jsonify, request

from src.domain.schemas.paginator.schema import PaginatorSchema
from src.domain.schemas.restaurants.schema import RestaurantSchema
from src.services.restaurants.service import RestaurantsService

restaurant = Blueprint("restaurant", "restaurant", description="Restaurants")


@restaurant.post("/restaurants")
@jwt_required()
@restaurant.arguments(RestaurantSchema)
def create_restaurant(restaurant_data: dict):
    return RestaurantsService.create_restaurant({"data": restaurant_data})


@restaurant.get("/restaurants/<string:restaurant_id>")
def find_one_restaurant(restaurant_id: str):
    return RestaurantsService.find_one_restaurant({"restaurant_id": restaurant_id})


@restaurant.get("/restaurants")
@restaurant.arguments(PaginatorSchema, location="query")
def find_all_restaurant(xaps):
    data = request.args
    restaurant_data = {
        "name": data.get("name"),
        "sort": data.get("sort"),
        "limit": data.get("limit"),
        "skip": data.get("skip"),
    }
    return RestaurantsService.find_all_restaurant(restaurant_data)


@restaurant.put("/restaurants/<string:restaurant_id>")
@jwt_required()
@restaurant.arguments(RestaurantSchema)
def update_restaurant(restaurant_data: dict, restaurant_id: str ):
    payload = {
        "restaurant_id": restaurant_id,
        "update_data": restaurant_data
    }
    return RestaurantsService.update_restaurant(payload)


@restaurant.delete("/restaurants/<string:restaurant_id>")
@jwt_required()
def delete_restaurant(restaurant_id: str):
    return RestaurantsService.delete_restaurant({"restaurant_id": restaurant_id})