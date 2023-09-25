# Standard Library
from unittest.mock import MagicMock, patch

# IRango
from src.infrastructures.redis.infrastructure import RedisInfrastructure
from src.repositories.bases.redis.repository import BaseRedisRepository
from tests.repositories.bases.redis.stub_redis import StubRedisRepository


@patch.object(RedisInfrastructure, "get_client")
def test_set_with_ttl(get_client_patch: MagicMock):
    stub = StubRedisRepository()

    get_client_patch.return_value = stub

    value = "hello"
    key = "my_key"
    ttl = 10

    BaseRedisRepository.set(key, value, ttl)

    assert stub.set_called


@patch.object(RedisInfrastructure, "get_client")
def test_set_none_ttl(get_client_patch: MagicMock):
    stub = StubRedisRepository()

    get_client_patch.return_value = stub

    value = "hello"
    key = "my_key"

    BaseRedisRepository.set(key, value)

    assert stub.set_called
