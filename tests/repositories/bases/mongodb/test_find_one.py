# Standard Library
from unittest.mock import patch, MagicMock

# Third-Party Library
import pytest

# IRango
from src.repositories.bases.mongodb.repository import BaseMongoDBRepository
from tests.repositories.bases.mongodb.stub_mongodb_operations import (
    StubMongoDBOperations,
)


@pytest.mark.asyncio
@patch.object(BaseMongoDBRepository, "_get_mongodb_base_collection")
async def test_find_one(_get_mongodb_base_collection_patch: MagicMock):
    data = {"name": "IRango", "email": "iragon@email.com", "id": "1234"}

    _get_mongodb_base_collection_patch.return_value = StubMongoDBOperations(data)

    query = {
        "name": "IRango",
    }
    projection = {"_id": False}

    result = await BaseMongoDBRepository.find_one(query, projection)

    assert result == data
