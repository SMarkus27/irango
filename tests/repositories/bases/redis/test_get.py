# Standard Libraries
from unittest.mock import patch, MagicMock

# IRango
from src.infrastructures.redis.infrastructure import RedisInfrastructure
from src.repositories.bases.redis.repository import BaseRedisRepository
from tests.repositories.bases.redis.stub_redis import StubRedisRepository


@patch.object(RedisInfrastructure, "get_client")
def test_get(get_client_patch: MagicMock):
    value = "hello"
    key = "my_key"
    stub = StubRedisRepository(value)

    get_client_patch.return_value = stub

    result = BaseRedisRepository.get(key)

    assert result == value