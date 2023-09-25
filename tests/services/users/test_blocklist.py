from unittest.mock import patch, MagicMock

from src.repositories.cache.repository import CacheRepository
from src.services.users.service import UsersService
from tests.repositories.bases.redis.stub_redis import StubRedisRepository


@patch.object(CacheRepository, "get")
def test_blocklist(get_patch: MagicMock):
    value = True
    stub = StubRedisRepository(value)

    get_patch.return_value = stub

    jti = "9cccc861-dd17-475a-8af6-101d514a63eb"
    result = UsersService.blocklist(jti)

    assert result.return_value == value
