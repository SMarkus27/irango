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
async def test_update_one(_get_mongodb_base_collection_patch: MagicMock):
    query = {"name": "IRango"}

    update_data = {"email": "iragon2@email.com"}

    _get_mongodb_base_collection_patch.return_value = StubMongoDBOperations()

    await BaseMongoDBRepository.update_one(query, update_data)
    assert _get_mongodb_base_collection_patch.update_one_called
