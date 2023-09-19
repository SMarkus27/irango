from unittest.mock import patch, MagicMock

from src.routes.products.route import create_product
from src.services.products.service import ProductsService


@patch.object(ProductsService, "create_product")
def test_create_product(create_product_patch: MagicMock):
    product_data = {
        "name": "pizza",
        "price": 25.55,
    }
    restaurant_id = "122s22-1a1aa2a2a2"

    response = {
        "message": f"Product created",
        "status_code": 201,
    }

    create_product_patch.return_value = response

    result = create_product(product_data, restaurant_id)
