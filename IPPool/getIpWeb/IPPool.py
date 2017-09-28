from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse, marshal_with, fields

from db.MongoHelper import MongoHelper
from getIpWeb import MyFields

app = Flask(__name__)
api = Api(app)

resource_field = MyFields.IPItemFields


class IP(Resource):
    def __init__(self):
        self.mh = MongoHelper()
        self.mh.init_db()

    @marshal_with(resource_field, )
    def get(self):
        print('get')
        parser = reqparse.RequestParser()
        parser.add_argument('count', type=str)
        parser.add_argument('page_index', type=int)
        parser.add_argument('page_size', type=int)
        args = parser.parse_args()
        return self.mh.select(args['count'] if args['count'] is not None else 5,
                              page_index=args['page_index'] if args['page_index']else 1,
                              page_size=args['page_size'] if args['page_size'] else 5)

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=str)
        args = parser.parse_args()
        return self.mh.downscore(args if args['id'] is not None else abort(500))


api.add_resource(IP, '/ips')


def start_server():
    app.run(debug=True, host='0.0.0.0', port=5000)


if __name__ == '__main__':
    start_server()
