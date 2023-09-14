from uuid import uuid4

from src.core.interfaces.services.products.interface import IProductsService
from src.repositories.products.repository import ProductsRepository
from src.repositories.restaurants.repository import RestaurantsRepository


class ProductsService(IProductsService):
    @classmethod
    async def create_product(
        cls,
        payload: dict,
        restaurant_repository=RestaurantsRepository,
        product_repository=ProductsRepository,
    ):
        restaurant_id = payload.get("restaurant_id")
        query = {"restaurant_id": restaurant_id}
        projection = {"_id": False}

        restaurant_info = await restaurant_repository.find_one(query, projection)

        if not restaurant_info:
            return {
                "message": f"Restaurant {restaurant_id} not found",
                "status_code": 204,
            }

        product_data = payload.get("product_data")

        products = product_data.get("products")
        product_name = products.get("name")
        product_in_restaurant = restaurant_info.get("products", {})

        for product in product_in_restaurant:
            product_exist = product.get("name") == product_name
            if product_exist:
                return {
                    "message": f"Product {product_name} already exist",
                    "status_code": 204,
                }
        products.update({"product_id": str(uuid4())})
        product_data.update({"products": products})
        result = await product_repository.add_one_in_array(query, product_data)

        return result

    @classmethod
    async def find_one_product(
        cls, payload: dict, restaurant_repository=RestaurantsRepository
    ):
        product_id = payload.get("product_id")
        query = {"products": {"$elemMatch": {"product_id": product_id}}}
        projection = {"_id": False, "products.$": 1}

        restaurant_info = await restaurant_repository.find_one(query, projection)

        if not restaurant_info:
            return {"message": f"Product {product_id} not found", "status_code": 204}

        return {
            "message": f"Product {product_id}found",
            "result": restaurant_info,
            "status_code": 204,
        }

    @classmethod
    async def find_all_product(
        cls, payload: dict, restaurant_repository=RestaurantsRepository
    ):
        restaurant_id = payload.get("restaurant_id")
        query = {"restaurant_id": restaurant_id}
        projection = {"_id": False, "products": True}

        restaurant_info = await restaurant_repository.find_one(query, projection)

        if not restaurant_info:
            return {
                "message": f"Restaurant {restaurant_id} not found",
                "status_code": 204,
            }
        return {
            "message": f"Product found",
            "result": restaurant_info,
            "status_code": 204,
        }

    @classmethod
    async def update_product(
        cls, payload: dict, restaurant_repository=RestaurantsRepository
    ):
        product_id = payload.get("product_id")
        product_data = payload.get("update_data")

        product_data.update({"product_id": product_id})

        query = {"products.product_id": product_id}
        product_data = {"products.$": product_data}
        await restaurant_repository.update_one(query, product_data)

    @classmethod
    async def delete_product(
        cls, payload: dict, products_repository=ProductsRepository
    ):
        restaurant_id = payload.get("restaurant_id")
        product_id = payload.get("product_id")
        query = {"restaurant_id": restaurant_id}
        new = {"products": {"product_id": product_id}}
        await products_repository.delete_one_in_array(query, new)
