CHINA_AREA = ['河北', '山东', '辽宁', '黑龙江', '吉林', '甘肃', '青海', '河南', '江苏', '湖北', '湖南',
              '江西', '浙江', '广东', '云南', '福建', '台湾', '海南', '山西', '四川', '陕西',
              '贵州', '安徽', '重庆', '北京', '上海', '天津', '广西', '内蒙', '西藏', '新疆', '宁夏', '香港', '澳门']

splash_url = 'http://192.168.0.220:8050'
REDIS_HOST = '192.168.0.220'
REDIS_PORT = 6379
'''
ip，端口，类型(0高匿名，1透明)，protocol(0 http,1 https),ischina(0 国内，1 国外),updatetime(更新时间)
'''
parserList = [
    {
        'urls': ['http://www.66ip.cn/%s.html' % n for n in range(1, 12)],
        'type': 'xpath',
        'pattern': ".//*[@id='main']/div/div[1]/table/tbody/tr[position()>1]",
        'position': {'ip': './td[1]', 'port': './td[2]', 'type': './td[4]', 'protocol': '', 'ischina': 0},
        'from_website': 'http://www.66ip.cn'
    },
    {
        'urls': ['http://www.66ip.cn/areaindex_%s/%s.html' % (m, n) for m in range(1, 35) for n in range(1, 10)],
        'type': 'xpath',
        'pattern': ".//*[@id='footer']/div/table/tbody/tr[position()>1]",
        'position': {'ip': './td[1]', 'port': './td[2]', 'type': './td[4]', 'protocol': '', 'ischina': 0},
        'from_website': 'http://www.66ip.cn'
    },
    {
        'urls': ['http://cn-proxy.com/', 'http://cn-proxy.com/archives/218'],
        'type': 'xpath',
        'pattern': ".//table[@class='sortable']/tbody/tr[position()>1]",
        'position': {'ip': './td[1]', 'port': './td[2]', 'type': '', 'protocol': '', 'ischina': 0},
        'from_website': 'http://cn-proxy.com/,http://cn-proxy.com/archives/218'
    },
    {
        'urls': ['http://www.mimiip.com/gngao/%s' % n for n in range(1, 10)],
        'type': 'xpath',
        'pattern': ".//table[@class='list']/tr[position()>1]",
        'position': {'ip': './td[1]', 'port': './td[2]', 'type': './td[4]', 'protocol': './td[5]', 'ischina': 0},
        'from_website': 'http://www.mimiip.com'
    },
    # {
    #     'urls': ['https://proxy-list.org/english/index.php?p=%s' % n for n in range(1, 10)],
    #     'type': 'module',
    #     'moduleName': 'proxy_listPraser',
    #     'pattern': 'Proxy\(.+\)',
    #     'position': {'ip': 0, 'port': -1, 'type': -1, 'protocol': 2, 'ischina': 1}
    #
    # },
    # {
    #     'urls': ['https://hidemy.name/en/proxy-list/%s#list' % n for n in
    #              ([''] + ['?start=%s' % (64 * m) for m in range(1, 10)])],
    #     'type': 'xpath',
    #     'pattern': ".//table[@class='proxy__t']/tbody/tr",
    #     'position': {'ip': './td[1]', 'port': './td[2]', 'type': '', 'protocol': ''}
    #
    # },
    {
        'urls': ['http://www.kuaidaili.com/proxylist/%s/' % n for n in range(1, 11)],
        'type': 'xpath',
        'pattern': ".//div[@id='freelist']/table/tbody/tr",
        'position': {'ip': './td[1]', 'port': './td[2]', 'type': './td[3]', 'protocol': './td[4]'},
        'from_website': 'http://www.kuaidaili.com'
    },
    {
        'urls': ['http://www.kuaidaili.com/free/%s/%s/' % (m, n) for m in ['inha', 'intr', 'outha', 'outtr'] for n
                 in
                 range(1, 11)],
        'type': 'xpath',
        'pattern': ".//*[@id='list']/table/tbody/tr[position()>0]",
        'position': {'ip': './td[1]', 'port': './td[2]', 'type': './td[3]', 'protocol': './td[4]'},
        'from_website': 'http://www.kuaidaili.com'
    },
    {
        'urls': ['http://www.ip181.com/daili/%s.html' % n for n in range(1, 11)],
        'type': 'xpath',
        'pattern': ".//div[@class='row']/div[3]/table/tbody/tr[position()>1]",
        'position': {'ip': './td[1]', 'port': './td[2]', 'type': './td[3]', 'protocol': './td[4]'},
        'from_website': 'http://www.ip181.com'
    },
    {
        'urls': ['http://www.xicidaili.com/%s/%s' % (m, n) for m in ['nn', 'nt', 'wn', 'wt'] for n in range(1, 8)],
        'type': 'xpath',
        'pattern': ".//*[@id='ip_list']/tbody/tr[position()>1]",
        'position': {'ip': './td[2]', 'port': './td[3]', 'type': './td[5]', 'protocol': './td[6]'},
        'from_website': 'http://www.xicidaili.com'
    },
]
