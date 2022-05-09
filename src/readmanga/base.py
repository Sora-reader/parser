"""Base values and classes to inherit from."""
from abc import ABC, abstractmethod
from typing import List, Union

from readmanga.items import MangaItem
from src.core.spider import AutoNameMixin, WithOptionalUrl, WithRedisClient, WithTaskID


class ReadmangaSpider(ABC, AutoNameMixin, WithTaskID, WithRedisClient, WithOptionalUrl):
    """Base readmanga spider."""

    @abstractmethod
    def parse(self, *args, **kwargs) -> Union[MangaItem, List[MangaItem]]:
        ...
