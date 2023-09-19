# Standard Library
from unittest.mock import patch, MagicMock

# IRango
from src.repositories.bases.mongodb.repository import BaseMongoDBRepository
from tests.repositories.bases.mongodb.stub_mongodb_operations import (
    StubMongoDBOperations,
)


@patch.object(BaseMongoDBRepository, "_get_mongodb_base_collection")
def test_find_all_paginated_no_items(
    _get_mongodb_base_collection_patch: MagicMock,
):
    data = []
    _get_mongodb_base_collection_patch.return_value = StubMongoDBOperations(data)

    expected = ([], 0)

    query = {
        "name": "IRango",
    }
    projection = {"_id": False}

    result = BaseMongoDBRepository.find_all_paginated(query, projection, 0, 0)

    assert result == expected


@patch.object(BaseMongoDBRepository, "_get_mongodb_base_collection")
def test_find_all_paginated_sorted(_get_mongodb_base_collection_patch: MagicMock):
    data = [
        {"name": "IRango", "email": "iragon@email.com", "id": "1234"},
        {"name": "IRango2", "email": "iragon2@email.com", "id": "1234"},
    ]

    _get_mongodb_base_collection_patch.return_value = StubMongoDBOperations(data)

    query = {
        "name": "IRango",
    }
    projection = {"_id": False}

    expected = ([{'name': 'IRango', 'email': 'iragon@email.com', 'id': '1234'}, {'name': 'IRango2', 'email': 'iragon2@email.com', 'id': '1234'}], 2)


    result = BaseMongoDBRepository.find_all_paginated(
        query, projection, 0, 1, ("name",)
    )
    assert result == expected


@patch.object(BaseMongoDBRepository, "_get_mongodb_base_collection")
def test_find_all_paginated(_get_mongodb_base_collection_patch: MagicMock):
    data = [
        {"name": "IRango", "email": "iragon@email.com", "id": "1234"},
        {"name": "IRango2", "email": "iragon2@email.com", "id": "1234"},
    ]

    _get_mongodb_base_collection_patch.return_value = StubMongoDBOperations(data)

    query = {
        "name": "IRango",
    }
    projection = {"_id": False}

    expected = ([{'name': 'IRango', 'email': 'iragon@email.com', 'id': '1234'}, {'name': 'IRango2', 'email': 'iragon2@email.com', 'id': '1234'}], 2)

    result = BaseMongoDBRepository.find_all_paginated(query, projection, 0, 1)
    assert result == expected
