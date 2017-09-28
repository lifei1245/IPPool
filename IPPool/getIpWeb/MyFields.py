# coding=utf-8
# @Time : 2017/9/27 14:55
# @Author : 李飞
from flask_restful import fields

IPItemFields = {
    'ObjID': fields.String,
    'ip': fields.String,
    'port': fields.String,
    'type': fields.String,
    'protocol': fields.String,
    'score': fields.String,
    'response_time': fields.String,
}
