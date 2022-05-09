from typing import Optional

from src.celery.utils import crawl_spider_and_return_results
from src.core.consts import CHAPTERS, DETAIL, IMAGES, LIST
from src.core.utils import init_redis_client
from src.readmanga.spiders import (
    ReadmangaChapterSpider,
    ReadmangaDetailSpider,
    ReadmangaImageSpider,
    ReadmangaListSpider,
)

METHOD_TO_SPIDER = {
    LIST: ReadmangaListSpider,
    DETAIL: ReadmangaDetailSpider,
    CHAPTERS: ReadmangaChapterSpider,
    IMAGES: ReadmangaImageSpider,
}


def entrypoint(task_id: str, method: str, url: Optional[str], *args, **kwargs) -> str:
    """Readmanga scraping entrypoint."""
    if method == IMAGES:
        client = init_redis_client()
        images = client.get(url)
        if images:
            return images

    spider = METHOD_TO_SPIDER[method]

    results = crawl_spider_and_return_results(
        task_id,
        spider,
        url=url,
        *args,
        **kwargs,
    )
    return results
