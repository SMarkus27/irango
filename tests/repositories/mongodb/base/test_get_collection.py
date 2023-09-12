# Standard Library
from unittest.mock import patch, MagicMock

# Third-Party Library
import pytest

# IRango
from src.repositories.mongodb.base.repository import BaseMongoDBRepository
from tests.infrastructures.mongodb.stub import StubAsyncIOMotorClient


@pytest.mark.asyncio
@patch.object(BaseMongoDBRepository, "_set_mongodb_base_collection")
async def test_get_mongodb_base_collection_non_empty_collection(_set_mongodb_base_collection_patch: MagicMock):
    BaseMongoDBRepository._mongodb_collection_in_connection = None

    _set_mongodb_base_collection_patch.return_value = StubAsyncIOMotorClient

    assert await BaseMongoDBRepository._get_mongodb_base_collection()


@pytest.mark.asyncio
@patch.object(BaseMongoDBRepository, "_set_mongodb_base_collection")
async def test_get_mongodb_base_collection_non_empty_collection(_set_mongodb_base_collection_patch: MagicMock):
    BaseMongoDBRepository._mongodb_collection_in_connection = None

    _set_mongodb_base_collection_patch.return_value = StubAsyncIOMotorClient

    client_one = await BaseMongoDBRepository._get_mongodb_base_collection()

    client_two = await BaseMongoDBRepository._get_mongodb_base_collection()

    assert client_one == client_two