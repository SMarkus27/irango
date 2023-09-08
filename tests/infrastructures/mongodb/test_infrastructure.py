from unittest.mock import MagicMock, patch

import decouple
import pytest
from motor.motor_asyncio import AsyncIOMotorClient
from decouple import config
from src.infrastructures.mongodb.infrastructure import MongoDBInfrastructure
from tests.infrastructures.mongodb.stub import StubAsyncIOMotorClient


@patch.object(AsyncIOMotorClient, "__new__")
def test_get_client(mongodb_client_patch: MagicMock):
    stub = StubAsyncIOMotorClient()
    mongodb_client_patch.return_value = stub

    client = MongoDBInfrastructure.get_client()

    assert client == stub


@patch.object(AsyncIOMotorClient, "__new__")
def test_get_client_client_already_created(mongodb_client_patch: MagicMock):

    stub = StubAsyncIOMotorClient()
    mongodb_client_patch.return_value = stub

    client_one = MongoDBInfrastructure.get_client()
    client_two = MongoDBInfrastructure.get_client()

    assert client_one == client_two
    MongoDBInfrastructure.mongodb_client = None


@patch.object(AsyncIOMotorClient, "__new__")
def test_get_client_error(mongodb_client_patch: MagicMock):

    with pytest.raises(Exception):
        mongodb_client_patch.side_effect = Exception
        MongoDBInfrastructure.get_client()