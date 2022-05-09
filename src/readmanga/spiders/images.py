import re

import orjson
import scrapy
from scrapy.http import HtmlResponse

from src.readmanga.base import ReadmangaSpider
from src.readmanga.items import ChapterImageList

COUNT_LINK_ELEMENTS = 3


class ReadmangaImageSpider(ReadmangaSpider, scrapy.Spider):
    """Image spider."""

    custom_settings = {
        "ITEM_PIPELINES": {
            "src.readmanga.pipelines.ReadmangaImagePipeline": 300,
            "src.core.pipelines.RedisTaskIDPipeline": 400,
        }
    }

    def parse(self, response: HtmlResponse, **kwargs) -> ChapterImageList:
        images = re.search(r"rm_h.initReader\(.*(\[{2}.*]{2}).*\)", response.text)
        image_links = []
        if images:
            image_links = [
                "".join(image[:COUNT_LINK_ELEMENTS])
                for image in orjson.loads(images.group(1).replace("'", '"'))
            ]
        return ChapterImageList(images=image_links)
