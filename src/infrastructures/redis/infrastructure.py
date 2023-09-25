# Third-Party Library
import redis
from redis import Redis

# IRango
from src.core.interfaces.infrastructures.redis.inteface import IRedisInfrastructure


class RedisInfrastructure(IRedisInfrastructure):

    _redis_client: Redis = None
    _redis_url: str = None

    @classmethod
    def get_client(cls):
        try:
            if cls._redis_url is None:
                raise Exception("Redis url connection must be defined in the subclass")

            if cls._redis_client is None:
                cls._redis_client = redis.from_url(cls._redis_url)
            return cls._redis_client

        except Exception as error:
            print(error)
            raise error
