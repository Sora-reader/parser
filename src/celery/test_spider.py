import scrapy
from src.core.spider import WithRedisClient

class QuotesSpider(WithRedisClient, scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        print("start called")
        urls = [
            'https://quotes.toscrape.com/page/1/',
            'https://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print("parse called")
        return {"data": [1,2,3]}

