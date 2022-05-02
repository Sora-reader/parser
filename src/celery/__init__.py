# TODO: move to backend
import asyncio

from asgiref.sync import sync_to_async

from src.celery import _tasks as tasks
from src.celery._app import app


def task_to_async(task, *, start_delay=0.1, delay_multiplier=1.5, max_delay=2):
    async def wrapper(*args, **kwargs):
        delay = start_delay
        async_result = await sync_to_async(task.delay)(*args, **kwargs)
        while not async_result.ready():
            await asyncio.sleep(delay)
            delay = min(delay * delay_multiplier, max_delay)  # exponential backoff, max 2 seconds
        return async_result.get()

    return wrapper
