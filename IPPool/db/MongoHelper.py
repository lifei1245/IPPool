import pymongo
from config import DB_CONFIG
from db.ISqlHelper import ISqlHelper
from bson.objectid import ObjectId


class MongoHelper(ISqlHelper):
    def __init__(self):
        self.client = pymongo.MongoClient(DB_CONFIG['DB_CONNECT_STRING'], connect=False)

    def init_db(self):
        self.db = self.client.allips
        self.proxys = self.db.ips

    def drop_db(self):
        self.client.drop_database(self.db)

    def insert(self, value=None):
        if value:
            proxy = dict(ip=value['ip'], port=value['port'], types=value['types'], protocol=value['protocol'],
                         score=value['score'],
                         from_website=value['from_website'], response_time=value['response_time'])
            self.proxys.insert_one(proxy)

    def delete(self, conditions=None):
        if conditions:
            self.proxys.delete_one(conditions)
            return ('deleteNum', 'ok')
        else:
            return ('deleteNum', 'None')

    def update(self, conditions=None, value=None):
        if conditions and value:
            self.proxys.update(conditions, {"$set": value})
            return {'updateNum': 'ok'}
        else:
            return {'updateNum': 'fail'}

    def select(self, count=None, conditions=None, page_index=1, page_size=5):
        if count:
            count = int(count)
        else:
            count = 0
        if conditions:
            conditions = dict(conditions)
            conditions_name = ['types', 'protocol']
            for condition_name in conditions_name:
                value = conditions.get(condition_name, None)
                if value:
                    conditions[condition_name] = int(value)
        else:
            conditions = {}
        items = self.proxys.find(conditions, limit=count).sort(
            [("response_time", pymongo.ASCENDING), ("score", pymongo.DESCENDING)]).skip(page_index * page_size).limit(
            page_size)
        results = []
        for item in items:
            result = {
                'ip': item['ip'],
                'port': item['port'],
                'score': item['score'],
                'type': item['type'],
                'protocol': item['protocol'],
                'response_time': item['response_time'],
                'ObjID': item['_id']
            }
            results.append(result)
        return results

    # 降低分数,分数为0了删掉该条数据
    def downscore(self, conditions):
        res = self.proxys.update_one({'_id': ObjectId(conditions['id'])}, {'$inc': {'score': -1}})
        result = self.proxys.find({'_id': ObjectId(conditions['id'])})
        for doc in result:
            if doc['score'] <= 0:
                res = self.proxys.delete_one({'_id': ObjectId(conditions['id'])})
        return res.raw_result


if __name__ == '__main__':
    mh = MongoHelper()
    mh.init_db()
    # print(mh.select(30))
    mh.downscore(conditions={'id': '59cc7a56a0f37e2874525eb6'})
