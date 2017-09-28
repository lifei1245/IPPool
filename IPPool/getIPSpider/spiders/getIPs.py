import scrapy
from requests import ReadTimeout, ConnectTimeout
from requests.exceptions import ProxyError, ConnectionError
from scrapy_splash import SplashRequest
from getIPSpider import spider_config
from scrapy_redis.spiders import RedisSpider

from getIPSpider.items import IPItem
from getIPSpider.spiders.CusRedisSpider import CusRedisSpider
from scrapy import Spider
from fake_useragent import UserAgent
import json
import requests


class GetipsSpider(RedisSpider):
    name = 'getIPs'
    start_urls = ['http://www.baidu.com']

    custom_settings = {
        'SPIDER_MIDDLEWARES': {
            'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
        },
        'DOWNLOADER_MIDDLEWARES': {
            'scrapy_splash.SplashCookiesMiddleware': 723,
            'scrapy_splash.SplashMiddleware': 725,
            'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
            'getIPSpider.middlewares.IpMiddleWare': 1,
        },
        'SPLASH_URL': spider_config.splash_url,
        # 'DUPEFILTER_CLASS': 'scrapy_splash.SplashAwareDupeFilter',
        'HTTPCACHE_STORAGE': 'scrapy_splash.SplashAwareFSCacheStorage',

        # scrapy redis
        'REDIS_HOST': spider_config.REDIS_HOST,
        'REDIS_PORT': spider_config.REDIS_PORT,
        'SCHEDULER': "scrapy_redis.scheduler.Scheduler",
        # 'DUPEFILTER_CLASS': "scrapy_redis.dupefilter.RFPDupeFilter",
        'ITEM_PIPELINES': {
            'scrapy_redis.pipelines.RedisPipeline': 300,
            'getIPSpider.pipelines.InsertItemPipline': 1,
        },
        'DUPEFILTER_CLASS': 'getIPSpider.spiders.CusDupeFilter.SplashAwareDupeFilter'
    }

    def __init__(self):
        self.parserList = spider_config.parserList
        self.ua = UserAgent()
        super(GetipsSpider, self).__init__()

    def parse(self, response):
        print(response.body)
        U_A = self.ua.random
        for i in range(20):
            for item in self.parserList:
                for url in item['urls']:
                    yield SplashRequest(url=url, callback=self.parserresult, dont_filter=True,
                                        args={'wait': 3, 'itemdata': item, 'headers': {'User-Agent': U_A}},
                                        splash_headers={'User-Agent': U_A})

    def parserresult(self, response):
        metas = response.request.meta['splash']['args']['itemdata']
        if metas['type'] == 'xpath':
            datas = response.xpath(metas['pattern'])
            for data in datas:
                info = metas['position']
                ip = data.xpath(info['ip'] + '/text()').extract_first()
                port = data.xpath(info['port'] + '/text()').extract_first()
                type = data.xpath(info['type'] + '/text()').extract_first()
                protocol = data.xpath(info['protocol'] + '/text()').extract_first()
                from_website = metas['from_website']
                retry_count = 3
                current_time = 0
                while current_time < retry_count:
                    try:
                        result = requests.get('http://116.196.96.140:32768/', proxies={
                            'http': 'http://%s:%s' % (ip, port),
                            'https': 'http://%s:%s' % (ip, port),
                        }, timeout=1)
                        response_time = result.elapsed.microseconds

                        if result.status_code == 200:  # 代理有效性判斷
                            ip_item = IPItem()
                            ip_item['ip'] = ip
                            ip_item['port'] = port
                            ip_item['type'] = type
                            ip_item['protocol'] = protocol
                            ip_item['from_website'] = from_website
                            ip_item['response_time'] = response_time
                            print('------->%s:%s  is correct,current retry time is %s' % (ip, port, current_time + 1))
                            current_time = 3
                            yield ip_item
                        else:
                            current_time += 1
                    except (ReadTimeout, ConnectTimeout, ProxyError,)as e:
                        print('------->%s:%s  is no use,current retry time is %s' % (ip, port, current_time + 1))
                        current_time += 1
                    except ConnectionError:
                        print('------->%s:%s  is no use,current retry time is %s ------->return content is none' % (
                            ip, port, current_time + 1))
                        current_time += 1
