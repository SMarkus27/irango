from collections import namedtuple
from unittest.mock import patch, MagicMock

import pytest

from src.repositories.restaurants.repository import RestaurantsRepository
from src.services.restaurants.service import RestaurantsService


@patch.object(RestaurantsRepository, "find_one")
@pytest.mark.asyncio
async def test_update_restaurant_restaurant_not_found(find_one_patch: MagicMock):
    payload = {
        "restaurant_id": 123
    }

    find_one_patch.return_value = None

    expected = {"message": f"Restaurant not found", "status_code": 204}

    result = await RestaurantsService.update_restaurant(payload)

    assert result == expected


@patch.object(RestaurantsRepository, "find_one")
@patch.object(RestaurantsRepository, "update_one")
@pytest.mark.asyncio
async def test_update_restaurant(update_one_patch: MagicMock, find_one_patch: MagicMock):
    payload = {
        "restaurant_id": 1,
        "update_data": {
            "name": "large burger"
        }
    }

    restaurant_info = {
        "name": "large burger"
    }

    find_one_patch.return_value = restaurant_info

    update_result = namedtuple("UpdateResult", ["modified_count"])

    update_result.modified_count = 1

    update_one_patch.return_value = update_result
    expected = {"message": f"Restaurant updated", "status_code": 204}
    result = await RestaurantsService.update_restaurant(payload)

    assert result == expected


@patch.object(RestaurantsRepository, "find_one")
@patch.object(RestaurantsRepository, "update_one")
@pytest.mark.asyncio
async def test_update_restaurant_not_updated(update_one_patch: MagicMock, find_one_patch: MagicMock):
    payload = {
        "restaurant_id": 1,
        "update_data": {
            "name": "large burger"
        }
    }

    restaurant_info = {
        "name": "large burger"
    }

    find_one_patch.return_value = restaurant_info

    update_result = namedtuple("UpdateResult", ["modified_count"])

    update_result.modified_count = 0

    update_one_patch.return_value = update_result
    expected = {"message": f"Restaurant not updated", "status_code": 200}
    result = await RestaurantsService.update_restaurant(payload)

    assert result == expected