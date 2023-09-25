# Standard Library
from unittest.mock import patch, MagicMock

# IRango
from src.repositories.restaurants.repository import RestaurantsRepository
from src.services.restaurants.service import RestaurantsService


@patch.object(RestaurantsRepository, "find_one")
def test_create_restaurant_restaurant_already_exist(find_one_patch: MagicMock):
    payload = {
        "data": {
            "name": "burgers",
        }
    }

    restaurant_info = {
        "name": "burgers",
        "id": 1
    }
    find_one_patch.return_value = restaurant_info

    expected = {
        "message": f"Restaurant burgers already exist, try it a new one",
        "status_code": 200,
    }

    result =  RestaurantsService.create_restaurant(payload)

    assert result == expected


@patch.object(RestaurantsRepository, "insert_one")
@patch.object(RestaurantsRepository, "find_one")
def test_create_restaurant_restaurant(find_one_patch: MagicMock, insert_one_patch: MagicMock):
    payload = {
        "data": {
            "name": "burgers",
        }
    }

    find_one_patch.return_value = None

    expected =  {"message": "Restaurant Created", "status_code": 201}

    insert_one_patch.return_value = True

    result =  RestaurantsService.create_restaurant(payload)

    assert result == expected