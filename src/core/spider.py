from src.core.utils import init_redis_client

class WithRedisClient:
    """
    Add redis_client to self.

    Later used by pipelines.
    """
    def __init__(self, *args, **kwargs):
        client = init_redis_client()
        kwargs["redis_client"] = client
        super().__init__(*args, **kwargs)


class InjectUrlMixin:
    """Add url parameter to be able to override start_urls."""
    def __init__(self, *args, **kwargs):
        url = kwargs.pop("url", None)
        if not getattr(self.__class__, "start_urls", None) and url:
            super().__init__(*args, start_urls=[url])
        else:
            super().__init__(*args, **kwargs)

