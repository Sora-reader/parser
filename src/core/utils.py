import redis

from src.core.base_settings import REDIS_URL


def init_redis_client() -> redis.Redis:
    return redis.StrictRedis.from_url(REDIS_URL, decode_responses=True)
