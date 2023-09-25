# Standard Libraries
from collections import namedtuple
from unittest.mock import patch, MagicMock

# IRango
from src.repositories.products.repository import ProductsRepository
from src.repositories.restaurants.repository import RestaurantsRepository
from src.services.products.service import ProductsService


@patch.object(RestaurantsRepository, "find_one")
def test_update_product_restaurant_not_found_not_updated(find_one_patch: MagicMock):

    payload = {
        "product_id": "xl-burger",
        "restaurant_id": 1,
        "update_data": {
            "product_id": 12,
            "name": "large burger"
        }
    }

    find_one_patch.return_value = None

    expected = {
        "message": f"Restaurant 1 not found",
        "status_code": 204,
    }

    result = ProductsService.update_product(payload)

    assert result == expected


@patch.object(RestaurantsRepository, "find_one")
@patch.object(ProductsRepository, "update_one")
def test_update_product_product_not_updated(update_one_patch: MagicMock, find_one_patch: MagicMock):

    payload = {
        "product_id": "xl-burger",
        "restaurant_id": 1,
        "product_data": {
            "name": "large burger"
        }
    }

    restaurant_info = {
        "name": "burger",
        "id": 12,
        "products": [
            {
                "name": "burger12",
                "id": 1
            }
        ]
    }

    find_one_patch.return_value = restaurant_info

    update_result = namedtuple("UpdateResult", ["modified_count"])
    update_result.modified_count = 0

    update_one_patch.return_value = update_result

    expected = {
        "message": f"Product not updated",
        "status_code": 200,
    }

    result = ProductsService.update_product(payload)

    assert result == expected


@patch.object(RestaurantsRepository, "find_one")
@patch.object(ProductsRepository, "update_one")
def test_update_product(update_one_patch: MagicMock, find_one_patch: MagicMock):
    payload = {
        "product_id": "xl-burger",
        "restaurant_id": 1,
        "product_data": {
            "product_id": 12,
            "name": "large burger"
        }
    }

    restaurant_info = {
        "name": "burger",
        "id": 12,
        "products": [
            {
                "name": "burger12",
                "id": 1
            }
        ]
    }

    find_one_patch.return_value = restaurant_info

    update_result = namedtuple("UpdateResult", ["modified_count"])

    update_result.modified_count = 1

    update_one_patch.return_value = update_result
    expected = {
        "message": f"Product updated",
        "status_code": 201,
    }
    result = ProductsService.update_product(payload)

    assert result == expected
