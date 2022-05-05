"""Base values and classes to inherit from."""
from src.core.spider import InjectUrlMixin, WithRedisClient, WithTaskID


class ReadmangaSpider(WithTaskID, WithRedisClient, InjectUrlMixin):
    """Base readmanga spider."""

    pass
