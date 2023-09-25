# Standard Library
from unittest.mock import patch, MagicMock

# Third-Party Library
import pytest

# IRango
from src.repositories.bases.mongodb.repository import BaseMongoDBRepository
from tests.infrastructures.mongodb.stub import StubPyMongoClient


@patch.object(BaseMongoDBRepository, "_set_mongodb_base_collection")
def test_get_mongodb_base_collection_non_empty_collection(
    _set_mongodb_base_collection_patch: MagicMock,
):
    BaseMongoDBRepository._mongodb_collection_in_connection = None

    _set_mongodb_base_collection_patch.return_value = StubPyMongoClient

    assert BaseMongoDBRepository._get_mongodb_base_collection()


@patch.object(BaseMongoDBRepository, "_set_mongodb_base_collection")
def test_get_mongodb_base_collection_non_empty_collection(
    _set_mongodb_base_collection_patch: MagicMock,
):
    BaseMongoDBRepository._mongodb_collection_in_connection = None

    _set_mongodb_base_collection_patch.return_value = StubPyMongoClient

    client_one = BaseMongoDBRepository._get_mongodb_base_collection()

    client_two = BaseMongoDBRepository._get_mongodb_base_collection()

    assert client_one == client_two
