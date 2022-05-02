"""Celery utils."""
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings

def crawl_spider(task_id, spider_klass, *args, **kwargs):
    """
    Run spider through CrawlerRunner class.

    Used by celery tasks, hence, passing of the task_id.
    """
    runner = CrawlerRunner(settings=get_project_settings())
    d = runner.crawl(
        spider_klass,
        task_id=task_id,
        *args,
        **kwargs,
    )
    d.addBoth(lambda _: reactor.stop())
    reactor.run()

