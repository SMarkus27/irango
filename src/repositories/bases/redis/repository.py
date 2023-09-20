from src.infrastructures.redis.infrastructure import RedisInfrastructure


class BaseRedisRepository(RedisInfrastructure):

    @classmethod
    def get(cls, key: str):
        client = cls.get_client()
        value = client.get(key)
        return value

    @classmethod
    def set(cls, key: str, value: any, ttl: int = 0):
        client = cls.get_client()
        if ttl > 0:
            client.set(name=key, value=str(value).encode(), ex=ttl)
        else:
            client.set(name=key, value=str(value).encode())