"""Celery tasks."""
from celery import Task
from src.celery import app
from src.celery.test_spider import QuotesSpider
from src.readmanga.images import ReadmangaImageSpider
from src.celery.utils import crawl_spider
from src.core.utils import init_redis_client


@app.task(name="crawl", bind=True)
# TODO: remove default spider_klass
def crawl(self: Task, *args, **kwargs):
    """
    Task to crawl a spider.

    Runs crawler in a runner, then extracts output from redis.
    """
    task_id = self.request.id

    crawl_spider(
        task_id,
        ReadmangaImageSpider,
        *args,
        **kwargs,
    )

    redis_client = init_redis_client()
    res = redis_client.get(task_id)
    redis_client.delete(task_id)
    return res
