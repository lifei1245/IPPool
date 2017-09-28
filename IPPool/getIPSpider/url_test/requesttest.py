# coding=utf-8
# @Time : 2017/9/22 14:01
# @Author : 李飞
import requests

r = requests.get('http://127.0.0.1:5000', proxies={
    'http': 'http://36.250.94.162:3128',
    'https': 'http://36.250.94.162:3128',
})
print(r)
