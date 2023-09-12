# Standard Library
from unittest.mock import patch, MagicMock

# Third-Party Library
import pytest

# IRango
from src.repositories.mongodb.base.repository import BaseMongoDBRepository
from tests.repositories.mongodb.base.stub_mongodb_operations import StubMongoDBOperations


@pytest.mark.asyncio
@patch.object(BaseMongoDBRepository, "_get_mongodb_base_collection")
async def test_delete_one(_get_mongodb_base_collection_patch: MagicMock):
    query = {"name": "IRango"}

    _get_mongodb_base_collection_patch.return_value = StubMongoDBOperations()

    await BaseMongoDBRepository.delete_one(query)
    assert _get_mongodb_base_collection_patch.delete_one_called
