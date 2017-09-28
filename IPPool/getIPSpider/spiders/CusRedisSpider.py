from scrapy_redis.spiders import RedisSpider


class CusRedisSpider(RedisSpider):
    redis_url = None

    def __init__(self):
        super(CusRedisSpider, self).__init__()

    @classmethod
    def update_settings(cls, settings):
        redis_settings = {
            "REDIS_URL": None,
            "SCHEDULER": "scrapy_redis.scheduler.Scheduler",
            "DUPEFILTER_CLASS": "scrapy_redis.dupefilter.RFPDupeFilter",
            'CONCURRENT_REQUESTS': 32,
            "ITEM_PIPELINES": {
                'scrapy_redis.pipelines.RedisPipeline': 300
            }
        }
        if cls.custom_settings is not None:
            cls.custom_settings = dict(redis_settings, **cls.custom_settings)
        else:
            cls.custom_settings = redis_settings
        if cls.redis_url is not None:
            cls.custom_settings["REDIS_URL"] = cls.redis_url
        settings.setdict(cls.custom_settings or {}, priority='spider')

    def parse(self, response):
        pass
