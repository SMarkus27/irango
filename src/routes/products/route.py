from flask_smorest import Blueprint

from src.domain.schemas.products.schema import ProductSchema
from src.services.products.service import ProductsService
from asyncio import run

products = Blueprint("products", "products", description="products")


@products.post("/restaurants/<string:restaurant_id>/products")
@products.arguments(ProductSchema)
def create_product(product_data: dict, restaurant_id: str):
    return ProductsService.create_product({"restaurant_id": restaurant_id, "product_data": product_data })


@products.get("/restaurants/<string:restaurant_id>/products/<string:product_id>")
def find_one_product(restaurant_id: str, product_id: str):
    return ProductsService.find_one_product({"restaurant_id": restaurant_id, "product_id": product_id})


@products.get("/restaurants/<string:restaurant_id>/products")
def find_all_products(restaurant_id: str):
    return ProductsService.find_all_product({"restaurant_id": restaurant_id})


@products.put("/restaurants/<string:restaurant_id>/products/<string:product_id>")
@products.arguments(ProductSchema)
def update_product(product_data: dict, restaurant_id: str, product_id: str):
    print(product_data)
    print(restaurant_id)
    return ProductsService.update_product({
        "restaurant_id": restaurant_id,
        "product_id": product_id,
        "product_data": product_data}
    )


@products.delete("/restaurants/<string:restaurant_id>/products/<string:product_id>")
def delete_product(restaurant_id: str, product_id: str):
    return ProductsService.delete_product({"restaurant_id": restaurant_id, "product_id": product_id})