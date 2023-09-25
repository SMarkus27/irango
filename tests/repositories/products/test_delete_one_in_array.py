# Standard Library
from unittest.mock import patch, MagicMock

# IRango
from src.repositories.bases.mongodb.repository import BaseMongoDBRepository
from src.repositories.products.repository import ProductsRepository
from tests.repositories.bases.mongodb.stub_mongodb_operations import StubMongoDBOperations


@patch.object(BaseMongoDBRepository, "_get_mongodb_base_collection")
def test_delete_one_in_array(_get_mongodb_base_collection_patch: MagicMock):
    query = {"name": "IRango"}

    product_data = {"email": "iragon2@email.com"}

    _get_mongodb_base_collection_patch.return_value = StubMongoDBOperations()

    ProductsRepository.delete_one_in_array(query, product_data)
    assert _get_mongodb_base_collection_patch.update_one_called
