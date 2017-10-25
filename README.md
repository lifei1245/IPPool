# IPPool
简单的一个ip代理池
<br/>
ip都是到一些免费ip代理网站爬取的,验证可用之后才存入数据库,数据库我使用的是mongodb,虽然爬取的验证码网站很多,但是验证大部分都是不可用的,因此爬取代理还是一个漫长的过程~~

爬虫使用的是scrapy,采用了scrapy-redis式的分布式,以及配合了scrapy-splash来处理某些动态加载网站,使用的时候需要在spider_config中设置好splash_url 和redis的host以及port
以及在对应目标机器上开起redis服务以及splash对应的镜像容器scrapinghub/splash(搜索scrapy-splash使用,基本都会讲到这个),使用时运行StartServer后往redis里push
一个初始地址就好(地址随意) 例如
```
redis-cli
lpush getIPs:start_urls https://www.baidu.com
```
getIPs是爬虫name 放进去的url可以正常访问到就行
web使用flask,使用flask-restful提供资源,只有一个资源.提供两种方法,get和post,get获取,post降低对应ip的分数,当分数小宇0的时候会自动删除(我默认把初始分数设置成3).后续可能会继续完善
如果爬取ip需要使用ip,IPmiddleware中有注释掉的代码,看一眼大概就能理解了


---

## API
1. get  参数  page_index 以及page_size 分别对应页码以及每页多少
 例如获取5个ip：http://127.0.0.1:5000/ips?page_index=1&page_size=5
 速度从低到高(越低的越好,数据是由验证ip是否可用处得到),得分由高到低默认排序
2. put 参数 id 即是想要降分的对应id
  例如 curl http://localhost:5000/ips?id="5dad1dadde2da3dda56rg2da" -X PUT -v 即可对对应的数据降分如果得分为0将会自动删除该条数据
