from typing import Union

from orjson import dumps


class RedisTaskIDPipeline:
    """
    Pipeline which loads all returned data into redis with task_id as the key.

    Spider must have redis_client and task_id attributes.
    """

    @staticmethod
    def process_item(item: Union[dict, list], spider):
        spider.redis_client.set(spider.task_id, dumps(item))
        return item
