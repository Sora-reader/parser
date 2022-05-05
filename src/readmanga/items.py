from scrapy import Field, Item


class ImageList(Item):
    images = Field()
