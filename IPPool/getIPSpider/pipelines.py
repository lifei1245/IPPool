# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class GetipspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class InsertItemPipline(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host='localhost', port=27017)
        self.db = self.client['allips']

    def process_item(self, item, spider):
        self.db.ips.insert_one({
            'ip': item['ip'],
            'port': item['port'],
            'type': item['type'],
            'protocol': item['protocol'],
            'score': 3,
            'from_website': item['from_website'],
            'response_time': item['response_time'],
        })
        return item
