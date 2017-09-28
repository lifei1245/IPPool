# coding=utf-8
# @Time : 2017/9/28 11:10
# @Author : 李飞
from getIpWeb.IPPool import app, start_server
from getIPSpider import main
from multiprocessing import Process

if __name__ == '__main__':
    p_server = Process(target=start_server)
    p0 = Process(target=main.startCrawl, args=('Spider1Log.csv',))
    p1 = Process(target=main.startCrawl, args=('Spider2Log.csv',))
    p2 = Process(target=main.startCrawl, args=('Spider3Log.csv',))
    p_server.start()
    p0.start()
    p1.start()
    p2.start()
