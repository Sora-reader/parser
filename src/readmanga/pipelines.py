from src.readmanga.images import ReadmangaImageSpider


class ReadmangaImagePipeline:
    """
    Readmanga image pipeline.

    Store images in redis with url of the chapter as the key.
    """

    @staticmethod
    def process_item(item: list, spider: ReadmangaImageSpider):
        from celery.contrib import rdb
        rdb.set_trace()
        spider.redis_client.json().set(spider.start_urls[0], "$", item)  # type: ignore
