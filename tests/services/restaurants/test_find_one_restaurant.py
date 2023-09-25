# Standard Library
from unittest.mock import patch, MagicMock

# IRango
from src.repositories.restaurants.repository import RestaurantsRepository
from src.services.restaurants.service import RestaurantsService


@patch.object(RestaurantsRepository, "find_one")
def test_find_one_restaurant(find_one_patch: MagicMock):
    payload = {
        "restaurant_id": 1111
    }

    restaurant_info = {
        "name": "burgers",
        "id": 1
    }
    find_one_patch.return_value = restaurant_info

    expected = {"result": restaurant_info, "message": "Restaurant found", "status_code": 200}

    result = RestaurantsService.find_one_restaurant(payload)

    assert result == expected


@patch.object(RestaurantsRepository, "find_one")
def test_find_one_restaurant_not_found(find_one_patch: MagicMock):
    payload = {
        "restaurant_id": 1111
    }

    find_one_patch.return_value = None

    expected = {
        "message": f"Restaurant 1111 not found",
        "status_code": 204,
    }

    result = RestaurantsService.find_one_restaurant(payload)

    assert result == expected