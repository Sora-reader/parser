import time
from celery import Celery

app = Celery("sora_parser")

app.conf.update(
    result_backend="redis",
    broker_url="redis://localhost:6379/",
    result_broker="redis://localhost:6379/",
    task_serializer="json",
    result_serializer="json",
)

@app.task()
def task():
    time.sleep(2)
    return 2+2

import asyncio
from asgiref.sync import sync_to_async

def task_to_async(task, *, start_delay = 0.1, delay_multiplier = 1.5, max_delay = 2):
    async def wrapper(*args, **kwargs):
        delay = start_delay
        async_result = await sync_to_async(task.delay)(*args, **kwargs)
        while not async_result.ready():
            await asyncio.sleep(delay)
            delay = min(delay * delay_multiplier, max_delay)  # exponential backoff, max 2 seconds
        return async_result.get()
    return wrapper

import src.celery.run
import src.celery.test_spider
