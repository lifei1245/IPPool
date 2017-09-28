# @Time : 2017/9/4 17:18
# @Author : 李飞

import sys
import os
from scrapy.cmdline import execute

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def startCrawl(logname):
    s = 'scrapy crawl getIPs --logfile {l} --loglevel INFO'.format(l=logname)
    execute(s.split())

# execute(['scrapy', 'crawl', 'xiecheng'])
