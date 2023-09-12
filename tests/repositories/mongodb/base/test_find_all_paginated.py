# Standard Library
from unittest.mock import patch, MagicMock

# Third-Party Library
import pytest

# IRango
from src.repositories.mongodb.base.repository import BaseMongoDBRepository
from tests.repositories.mongodb.base.stub_mongodb_operations import StubMongoDBOperations


@pytest.mark.asyncio
@patch.object(BaseMongoDBRepository, "_get_mongodb_base_collection")
async def test_find_all_paginated_no_items(_get_mongodb_base_collection_patch: MagicMock):
    data = []
    _get_mongodb_base_collection_patch.return_value = StubMongoDBOperations(data)

    expected = ([], 0)

    query = {
        "name": "IRango",
    }
    projection = {"_id": False}

    result = await BaseMongoDBRepository.find_all_paginated(query, projection, 0, 0)

    assert result == expected


@pytest.mark.asyncio
@patch.object(BaseMongoDBRepository, "_get_mongodb_base_collection")
async def test_find_all_paginated_sorted(_get_mongodb_base_collection_patch: MagicMock):
    data = [{
        "name": "IRango",
        "email": "iragon@email.com",
        "id": "1234"
    },
    {
        "name": "IRango2",
        "email": "iragon2@email.com",
        "id": "1234"
    },
    ]

    _get_mongodb_base_collection_patch.return_value = StubMongoDBOperations(data)

    query = {
        "name": "IRango",
    }
    projection = {"_id": False}

    expected = ([{'name': 'IRango', 'email': 'iragon@email.com', 'id': '1234'}], 2)

    result = await BaseMongoDBRepository.find_all_paginated(query, projection, 0, 1, ("name",))

    assert result == expected


@pytest.mark.asyncio
@patch.object(BaseMongoDBRepository, "_get_mongodb_base_collection")
async def test_find_all_paginated(_get_mongodb_base_collection_patch: MagicMock):
    data = [{
        "name": "IRango",
        "email": "iragon@email.com",
        "id": "1234"
    },
        {
            "name": "IRango2",
            "email": "iragon2@email.com",
            "id": "1234"
        },
    ]

    _get_mongodb_base_collection_patch.return_value = StubMongoDBOperations(data)

    query = {
        "name": "IRango",
    }
    projection = {"_id": False}

    expected = ([{'name': 'IRango', 'email': 'iragon@email.com', 'id': '1234'}], 2)

    result = await BaseMongoDBRepository.find_all_paginated(query, projection, 0, 1)

    assert result == expected

