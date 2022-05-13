"""Base values and classes to inherit from."""
from abc import ABC, abstractmethod
from typing import List, Union

from src.core.spider import AutoNameMixin, WithOptionalUrl, WithRedisClient, WithTaskID
from src.readmanga.items import MangaItem


class ReadmangaSpider(ABC, AutoNameMixin, WithTaskID, WithRedisClient, WithOptionalUrl):
    """Base readmanga spider."""

    @abstractmethod
    def parse(self, *args, **kwargs) -> Union[MangaItem, List[MangaItem]]:
        ...
