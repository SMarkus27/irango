# Standard Library
from unittest.mock import patch, MagicMock

# Third-Party Library
import pytest

# IRango
from src.repositories.restaurants.repository import RestaurantsRepository
from src.services.products.service import ProductsService


@patch.object(RestaurantsRepository, "find_one")
@pytest.mark.asyncio
async def test_find_one_product_restaurant_not_found(find_one_patch: MagicMock):
    payload = {
        "restaurant_id": "burgers"
    }

    find_one_patch.return_value = None

    expected = {"message": f"Restaurant burgers not found",
                "status_code": 204}

    result = await ProductsService.find_all_product(payload)

    assert result == expected


@patch.object(RestaurantsRepository, "find_one")
@pytest.mark.asyncio
async def test_find_one_product(find_one_patch: MagicMock):
    payload = {
        "restaurant_id": "burgers"
    }

    restaurant_info = [
        {"name": "burger1",
         "id": 12
         },
        {"name": "burger2",
         "id": 13
         },
    ]

    find_one_patch.return_value = restaurant_info

    expected = {
            "message": f"Product found",
            "result": restaurant_info,
            "status_code": 204,
        }

    result = await ProductsService.find_all_product(payload)

    assert result == expected
