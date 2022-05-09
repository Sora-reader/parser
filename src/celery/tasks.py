"""Celery tasks."""
from celery import Task
from src.celery import app
from src.celery.test_spider import QuotesSpider
from src.celery.utils import crawl_spider
from src.core.utils import init_redis_client


@app.task(name="crawl", bind=True)
# TODO: remove default spider_klass
def crawl(self: Task, spider_klass=QuotesSpider, *args, **kwargs):
    """
    Task to crawl a spider.

    Runs crawler in a runner, then extracts output from redis.
    """
    task_id = self.request.id

    # TODO
