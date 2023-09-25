# Standard Library
from unittest.mock import MagicMock, patch

# Third-Party Libraries
import pytest
from pymongo import MongoClient

# IRango
from src.infrastructures.mongodb.infrastructure import MongoDBInfrastructure
from tests.infrastructures.mongodb.stub import StubPyMongoClient


@patch.object(MongoClient, "__new__")
def test_get_client(mongodb_client_patch: MagicMock):
    stub = StubPyMongoClient()
    mongodb_client_patch.return_value = stub

    client = MongoDBInfrastructure.get_client()

    assert client == stub


@patch.object(MongoClient, "__new__")
def test_get_client_client_already_created(mongodb_client_patch: MagicMock):
    stub = StubPyMongoClient()
    mongodb_client_patch.return_value = stub

    client_one = MongoDBInfrastructure.get_client()
    client_two = MongoDBInfrastructure.get_client()

    assert client_one == client_two
    MongoDBInfrastructure.mongodb_client = None


@patch.object(MongoClient, "__new__")
def test_get_client_error(mongodb_client_patch: MagicMock):
    with pytest.raises(Exception):
        mongodb_client_patch.side_effect = Exception
        MongoDBInfrastructure.get_client()
