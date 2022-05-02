from celery import Celery
from datetime import timedelta

app = Celery("sora_parser")

class Config:
    result_backend="redis"
    broker_url="redis://localhost:6379/"
    result_broker="redis://localhost:6379/"
    task_serializer="json"
    result_serializer="json"
    worker_max_tasks_per_child = 1
    result_expires = timedelta(minutes=10)

app.config_from_object(Config)

