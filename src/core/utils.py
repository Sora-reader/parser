from re import sub

import redis

from src.core.base_settings import REDIS_URL


def init_redis_client() -> redis.Redis:
    return redis.StrictRedis.from_url(REDIS_URL, decode_responses=True)


def pascal_to_snake(string: str) -> str:
    return sub(r"(?<!^)(?=[A-Z])", "_", string).lower()
