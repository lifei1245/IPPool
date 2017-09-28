# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GetipspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class IPItem(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()
    type = scrapy.Field()
    protocol = scrapy.Field()
    from_website = scrapy.Field()
    response_time = scrapy.Field()
