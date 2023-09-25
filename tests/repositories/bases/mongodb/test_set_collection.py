# Standard Library
from unittest.mock import patch, MagicMock

# Third-Party Library
import pytest

# IRango
from src.infrastructures.mongodb.infrastructure import MongoDBInfrastructure
from src.repositories.bases.mongodb.repository import BaseMongoDBRepository
from tests.infrastructures.mongodb.stub import StubPyMongoClient


def test_set_mongodb_base_collection_invalid():
    with pytest.raises(Exception):
        BaseMongoDBRepository._set_mongodb_base_collection()


@patch.object(MongoDBInfrastructure, "get_client")
def test_set_mongodb_base_collection_valid(get_client_patch: MagicMock):
    BaseMongoDBRepository._mongodb_database = "database"
    BaseMongoDBRepository._mongodb_collection = "collection"

    database = {"collection": StubPyMongoClient}
    client = {"database": database}

    get_client_patch.return_value = client

    assert BaseMongoDBRepository._set_mongodb_base_collection()
