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
def test_insert_one(_get_mongodb_base_collection_patch: MagicMock):
    _get_mongodb_base_collection_patch.return_value = StubMongoDBOperations()

    data = {
        "name": "IRango",
    }
    result = BaseMongoDBRepository.insert_one(data)
    assert result is None
