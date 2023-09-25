# Standard Library
from unittest.mock import patch, MagicMock

# IRango
from src.repositories.restaurants.repository import RestaurantsRepository
from src.services.restaurants.service import RestaurantsService


@patch.object(RestaurantsRepository, "find_one")
def test_delete_restaurant_restaurant_not_found(find_one_patch: MagicMock):
    payload = {
        "restaurant_id": 123
    }

    find_one_patch.return_value = None

    expected = {"message": f"Restaurant not found", "status_code": 204}

    result = RestaurantsService.delete_restaurant(payload)

    assert result == expected


@patch.object(RestaurantsRepository, "find_one")
@patch.object(RestaurantsRepository, "delete_one")
def test_delete_restaurant(delete_one_patch: MagicMock, find_one_patch: MagicMock):
    payload = {
        "restaurant_id": 1,

    }

    restaurant_info = {
        "name": "large burger"
    }

    find_one_patch.return_value = restaurant_info
    delete_one_patch.return_value = True

    expected = {"message": f"Restaurant deleted", "status_code": 204}
    result = RestaurantsService.delete_restaurant(payload)

    assert result == expected

