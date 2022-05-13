"""Celery tasks."""
from celery import Task
from src.celery import app
from src.readmanga.entrypoint import entrypoint


@app.task(name="crawl", bind=True)
def crawl(self: Task, method: str, *args, **kwargs):
    """
    Task to crawl a spider.

    Runs crawler in a runner, then extracts output from redis.
    """
    task_id = self.request.id

    entrypoint(task_id, method, *args, **kwargs)
