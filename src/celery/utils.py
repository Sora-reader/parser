"""Celery utils."""
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

from src.core.utils import init_redis_client


def crawl_spider(task_id, spider, *args, **kwargs):
    """
    Run spider through CrawlerRunner class.

    Used by celery tasks, hence, passing of the task_id.
    """
    runner = CrawlerRunner(settings=get_project_settings())
    d = runner.crawl(
        spider,
        task_id=task_id,
        *args,
        **kwargs,
    )
    d.addBoth(lambda _: reactor.stop())
    reactor.run()


def crawl_spider_and_return_results(task_id: str, spider, *args, **kwargs) -> str:
    """Run spider and retrieve results."""
    crawl_spider(
        task_id,
        spider,
        *args,
        **kwargs,
    )

    redis_client = init_redis_client()
    results = redis_client.getdel(task_id)
    return results
