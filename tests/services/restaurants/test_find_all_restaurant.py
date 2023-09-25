# Standard Library
from unittest.mock import patch, MagicMock

# IRango
from src.repositories.restaurants.repository import RestaurantsRepository
from src.services.restaurants.service import RestaurantsService


@patch.object(RestaurantsRepository, "find_all_paginated")
def test_find_all_restaurant(find_all_paginated_patch: MagicMock):
    payload = {}

    restaurant_info = [{
        "name": "burgers",
        "id": 1
    },
        {
        "name": "burgers",
        "id": 1
        }

    ]

    find_all_paginated_patch.return_value = restaurant_info, 2

    expected = {'result': [{'name': 'burgers', 'id': 1}, {'name': 'burgers', 'id': 1}], 'total_items': 2, 'total_pages': 1, 'message': 'Restaurant found', 'status_code': 200}

    result = RestaurantsService.find_all_restaurant(payload)

    assert result == expected


@patch.object(RestaurantsRepository, "find_all_paginated")
def test_find_all_restaurant_by_name(find_all_paginated_patch: MagicMock):
    payload = {
        "name": "Bur"
    }

    restaurant_info = [{
        "name": "Burgers",
        "id": 1
    },
        {
        "name": "burgers",
        "id": 1
        }

    ]

    find_all_paginated_patch.return_value = restaurant_info, 2

    expected = {'result': [{'name': 'Burgers', 'id': 1}, {'name': 'burgers', 'id': 1}], 'total_items': 2, 'total_pages': 1, 'message': 'Restaurant found', 'status_code': 200}

    result = RestaurantsService.find_all_restaurant(payload)

    assert result == expected


@patch.object(RestaurantsRepository, "find_all_paginated")
def test_find_all_restaurant_restaurant_not_found(find_all_paginated_patch: MagicMock):
    payload = {
        "name": "Bur"
    }


    find_all_paginated_patch.return_value = [], 0

    expected = {"message": f"Restaurant not found", "status_code": 204}

    result = RestaurantsService.find_all_restaurant(payload)

    assert result == expected
