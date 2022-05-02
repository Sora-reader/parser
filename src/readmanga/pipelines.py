from typing import Union

class ReadmangaPipeline:
    """
    Pipeline which loads all returned data into redis.

    Spider must have redis_client and task_id attributes.
    """
    @staticmethod
    def process_item(item: Union[dict, list], spider):
        from json import dumps
        spider.redis_client.set(spider.task_id, dumps(item))

