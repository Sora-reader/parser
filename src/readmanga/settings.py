from src.readmanga.pipelines import ReadmangaPipeline

ROBOTSTXT_OBEY = True

DOWNLOAD_DELAY = 2

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_DEBUG = True
AUTOTHROTTLE_START_DELAY = 2
AUTOTHROTTLE_MAX_DELAY = 15
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0


BOT_NAME = "readmanga"
SPIDER_MODULES = ["src.readmanga.list"]
NEWSPIDER_MODULE = "src.readmanga"

DOWNLOADER_MIDDLEWARES = {
    "src.core.middleware.ErrbackMiddleware": 340,
    "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": 400,
}
ITEM_PIPELINES = {
    ReadmangaPipeline: 100,
}

LOG_FILE = "parse-readmanga.log"

