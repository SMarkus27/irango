# Standard Libraries
from collections import namedtuple
from unittest.mock import patch, MagicMock

# IRango
from src.repositories.products.repository import ProductsRepository
from src.repositories.restaurants.repository import RestaurantsRepository
from src.services.products.service import ProductsService


@patch.object(RestaurantsRepository, "find_one")
def test_create_product_restaurant_not_found(find_one_patch: MagicMock):
    payload = {"restaurant_id": "1234"}

    find_one_patch.return_value = None

    expected = {
                "message": "Restaurant 1234 not found",
                "status_code": 204,
            }
    result = ProductsService.create_product(payload)

    assert result == expected


@patch.object(RestaurantsRepository, "find_one")
def test_create_product_product_already_exist(find_one_patch: MagicMock):
    payload = {
        "restaurant_id": "1234",
        "product_data": {
                "name": "x-burger"
            }
    }
    product_in_restaurant = {
        "products": [{
            "name": "x-burger"
        }]
    }
    find_one_patch.return_value = product_in_restaurant

    expected = {
                "message": "Product x-burger already exist",
                "status_code": 204,
            }
    result = ProductsService.create_product(payload)

    assert result == expected


@patch.object(ProductsRepository, "add_one_in_array")
@patch.object(RestaurantsRepository, "find_one")
def test_create_product_product(find_one_patch: MagicMock, add_one_in_array_patch: MagicMock):
    payload = {
        "restaurant_id": "1234",
        "product_data": {
            "name": "x-burger2"
        }
    }
    product_in_restaurant = {
        "products": [{
            "name": "x-burger"
        }]
    }
    find_one_patch.return_value = product_in_restaurant
    created_result = namedtuple("UpdateResult", ["modified_count"])
    created_result.modified_count = 1
    add_one_in_array_patch.return_value = created_result

    expected = {
                "message": f"Product created",
                "status_code": 201,
            }

    result = ProductsService.create_product(payload)
    assert result == expected


@patch.object(ProductsRepository, "add_one_in_array")
@patch.object(RestaurantsRepository, "find_one")
def test_create_product_product_not_created(find_one_patch: MagicMock, add_one_in_array_patch: MagicMock):
    payload = {
        "restaurant_id": "1234",
        "product_data": {
            "name": "x-burger2"
        }
    }
    product_in_restaurant = {
        "products": [{
            "name": "x-burger"
        }]
    }
    find_one_patch.return_value = product_in_restaurant
    created_result = namedtuple("UpdateResult", ["modified_count"])
    created_result.modified_count = 0
    add_one_in_array_patch.return_value = created_result

    expected = {
                "message": f"Product not created",
                "status_code": 200
            }

    result = ProductsService.create_product(payload)
    assert result == expected
