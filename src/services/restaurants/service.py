from uuid import uuid4

from src.core.interfaces.services.services.interface import IRestaurantsService
from src.repositories.restaurants.repository import RestaurantsRepository
from src.utils.calculates import calculate_skip, calculate_total_pages


class RestaurantsService(IRestaurantsService):
    @classmethod
    async def create_restaurant(
        cls, payload: dict, restaurant_repository=RestaurantsRepository
    ):
        restaurant_data = payload.get("data")
        restaurant_name = restaurant_data.get("name")
        query = {"name": restaurant_name}
        projection = {"_id": False}

        restaurant_info = await restaurant_repository.find_one(query, projection)

        if restaurant_info:
            return {
                "message": f"Restaurant {restaurant_name} already exist, try it a new one",
                "status_code": 200,
            }

        restaurant_id = uuid4().__str__()
        restaurant_data.update({"restaurant_id": restaurant_id})

        await restaurant_repository.insert_one(restaurant_data)

        return {"message": "Restaurant Created", "status_code": 201}

    @classmethod
    async def find_one_restaurant(
        cls, payload: dict, restaurant_repository=RestaurantsRepository
    ):
        restaurant_id = payload.get("restaurant_id")
        query = {"restaurant_id": restaurant_id}
        projection = {"_id": False}

        result = await restaurant_repository.find_one(query, projection)

        if not result:
            return {
                "message": f"Restaurant {restaurant_id} not found",
                "status_code": 204,
            }

        return {"result": result, "message": "Restaurant found", "status_code": 200}

    @classmethod
    async def find_all_restaurant(
        cls, payload: dict, restaurant_repository=RestaurantsRepository
    ):
        restaurant_name = payload.get("name", {})

        query = {}
        if restaurant_name:
            query = {"name": {"$regex": restaurant_name, "$options": "i"}}

        projection = {"_id": False}

        page = payload.get("page", 0)
        limit = payload.get("size", 10)

        skip = calculate_skip(limit, page)

        sort = payload.get("sort", "name")
        results, total_items = await restaurant_repository.find_all_paginated(
            query, projection, skip, limit, sort
        )

        if not results:
            return {"message": f"Restaurant not found", "status_code": 204}

        total_pages = calculate_total_pages(total_items, limit)

        return {
            "result": results,
            "total_items": total_items,
            "total_pages": total_pages,
            "message": "Restaurant found",
            "status_code": 200,
        }

    @classmethod
    async def update_restaurant(
        cls, payload: dict, restaurant_repository=RestaurantsRepository
    ):
        restaurant_id = payload.get("restaurant_id")

        query = {"restaurant_id": restaurant_id}
        projection = {"_id": False}

        result = await restaurant_repository.find_one(query, projection)

        if not result:
            return {"message": f"Restaurant not found", "status_code": 204}

        update_data = payload.get("update_data")
        update_result = await restaurant_repository.update_one(query, update_data)

        if update_result.modified_count > 0:
            return {"message": f"Restaurant updated", "status_code": 204}

        return {"message": f"Restaurant not updated", "status_code": 200}

    @classmethod
    async def delete_restaurant(
        cls, payload: dict, restaurant_repository=RestaurantsRepository
    ):
        restaurant_id = payload.get("restaurant_id")
        query = {"restaurant_id": restaurant_id}
        projection = {"_id": False}

        result = await restaurant_repository.find_one(query, projection)

        if not result:
            return {"message": f"Restaurant not found", "status_code": 204}

        await restaurant_repository.delete_one(query)

        return {"message": f"Restaurant deleted", "status_code": 204}
