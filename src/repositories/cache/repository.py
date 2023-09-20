from decouple import config

from src.repositories.bases.redis.repository import BaseRedisRepository


class CacheRepository(BaseRedisRepository):
    _redis_url = "redis://{}:{}@{}:{}/{}".format(
        config("REDIS_CACHE_USER"),
        config("REDIS_CACHE_PASSWORD"),
        config("REDIS_CACHE_HOST"),
        config("REDIS_CACHE_PORT"),
        config("REDIS_CACHE_DB")
    )
