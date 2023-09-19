# Standard Library
from unittest.mock import patch, MagicMock

# Third-Party Library
import pytest

# IRango
from src.repositories.bases.mongodb.repository import BaseMongoDBRepository
from tests.repositories.bases.mongodb.stub_mongodb_operations import (
    StubMongoDBOperations,
)


@patch.object(BaseMongoDBRepository, "_get_mongodb_base_collection")
def test_delete_one(_get_mongodb_base_collection_patch: MagicMock):
    query = {"name": "IRango"}

    _get_mongodb_base_collection_patch.return_value = StubMongoDBOperations()

    BaseMongoDBRepository.delete_one(query)
    assert _get_mongodb_base_collection_patch.delete_one_called
