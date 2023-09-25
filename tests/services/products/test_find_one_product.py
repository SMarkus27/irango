# Standard Library
from unittest.mock import patch, MagicMock

# IRango
from src.repositories.products.repository import ProductsRepository
from src.repositories.restaurants.repository import RestaurantsRepository
from src.services.products.service import ProductsService


@patch.object(RestaurantsRepository, "find_one")
def test_find_one_product_restaurant_not_found(find_one_patch: MagicMock):
    payload = {
        "product_id": "xl-burger",
        "restaurant_id": 12
    }

    find_one_patch.return_value = None

    expected = {
        "message": f"Restaurant 12 not found",
        "status_code": 204
    }

    result = ProductsService.find_one_product(payload)

    assert result == expected


@patch.object(ProductsRepository, "find_one")
@patch.object(RestaurantsRepository, "find_one")
def test_find_one_product_product_not_found(find_one_restaurant_patch: MagicMock, find_one_product_patch: MagicMock):
    payload = {
        "product_id": "xl-burger",
        "restaurant_id": 12
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
    find_one_restaurant_patch.return_value = restaurant_info
    find_one_product_patch.return_value = None

    expected = {"message": f"Product xl-burger not found",
                "status_code": 204}

    result = ProductsService.find_one_product(payload)

    assert result == expected


@patch.object(ProductsRepository, "find_one")
@patch.object(RestaurantsRepository, "find_one")
def test_find_one_product(find_one_restaurant_patch: MagicMock, find_one_product_patch: MagicMock):
    payload = {
        "product_id": "burger12",
        "restaurant_id": 12
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

    product_info = {
        "products": [
            {
                "name": "burger12",
                "id": 1
            }
        ]
    }
    find_one_restaurant_patch.return_value = restaurant_info
    find_one_product_patch.return_value = product_info

    expected = {"message": f"Product burger12 found",
                "result": product_info,
                "status_code": 200
                }

    result = ProductsService.find_one_product(payload)

    assert result == expected