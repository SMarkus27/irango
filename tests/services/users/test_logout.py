from unittest.mock import patch, MagicMock

from src.repositories.cache.repository import CacheRepository
from src.services.users.service import UsersService
from tests.repositories.bases.redis.stub_redis import StubRedisRepository


@patch.object(CacheRepository, "set")
def test_logout(set_patch: MagicMock):
    jti = "9cccc861-dd17-475a-8af6-101d514a63eb"
    stub = StubRedisRepository()

    set_patch.return_value = stub

    expected = {
            "message": "Logout Successfully",
            "status_code": 200
        }

    result = UsersService.logout(jti)

    assert result == expected