from redis import Redis

from src.core.utils import init_redis_client, pascal_to_snake


class AutoNameMixin:
    """Automatically generate scrapy spider name."""

    def __init__(self, *args, **kwargs):
        self.__class__.name = pascal_to_snake(self.__class__.__name__)
        super().__init__(*args, **kwargs)


class WithRedisClient:
    """
    Add redis_client to self.

    Later used by pipelines.
    """

    redis_client: Redis

    def __init__(self, *args, **kwargs):
        client = init_redis_client()
        self.redis_client = client
        super().__init__(*args, **kwargs)


class WithTaskID:
    """Type class to add task_id attribute."""

    task_id: str
    "usually a UUID4 string which resembles celery task id."

    def __init__(self, *args, **kwargs):
        self.task_id = kwargs.pop("task_id")
        super().__init__(*args, **kwargs)


class WithOptionalUrl:
    """Add url parameter to be able to override start_urls."""

    def __init__(self, *args, **kwargs):
        url = kwargs.pop("url", None)
        if not getattr(self.__class__, "start_urls", None) and url:
            super().__init__(*args, start_urls=[url], **kwargs)
        else:
            super().__init__(*args, **kwargs)
