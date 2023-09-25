# Standard Library
from unittest.mock import patch, MagicMock

# Third-Party Libraries
import pytest
from redis import Redis

# IRango
from src.infrastructures.redis.infrastructure import RedisInfrastructure
from tests.infrastructures.redis.stub_redis import StubRedis


def test_get_client_none_redis_url():
    RedisInfrastructure._redis_url = None

    with pytest.raises(Exception):
        RedisInfrastructure.get_client()


@patch.object(Redis, "__new__")
def test_get_client(redis_patch: MagicMock):
    RedisInfrastructure._redis_url = "redis://pizza:1234@localhost:6379/10"
    stub = StubRedis()
    redis_patch.return_value = stub
    client = RedisInfrastructure.get_client()
    assert client


@patch.object(Redis, "__new__")
def test_get_client(redis_patch: MagicMock):
    RedisInfrastructure._redis_url = "redis://pizza:1234@localhost:6379/10"
    stub = StubRedis()
    redis_patch.return_value = stub
    client_one = RedisInfrastructure.get_client()
    client_two = RedisInfrastructure.get_client()

    assert client_one == client_two


def test_get_client_error():

    with pytest.raises(Exception):
        RedisInfrastructure.get_client()
