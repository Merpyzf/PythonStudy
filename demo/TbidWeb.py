# -*-coding:utf-8-*-

import sys
from time import sleep
from lxml import etree

reload(sys)
sys.setdefaultencoding('utf8')

import MySQLdb
import MySQLdb.cursors
import random

import requests
import BeautifulSoup
from urllib import urlopen
import uuid
import json
import time
import datetime

timeT = 0
proxies = {}
getProxiestimeT = 0
flag = 2
# 放公司详情的列表
bidDetailList = []
# 解析完成的中标公司详情
endbidDetailList = []


def getConnDb():
    db = MySQLdb.connect(host='192.200.200.236',
                         user='root',
                         passwd='root',
                         db='ecrservice',
                         charset='utf8',
                         port=3306,
                         use_unicode=True)
    return db;


def close(db, cursor):
    cursor.close()
    db.close()


def get_random_ip(ip_list):
    #     ip_list = ['60.255.230.185:808','120.76.55.49:8088','117.78.51.231:3128','110.72.17.122:8123','218.15.25.153:808','110.73.5.33:8123',
    #                '58.221.179.234:8081','113.200.220.137:8123','110.73.0.42:8123','110.73.40.177:8123','121.31.101.104:8123','59.40.50.4:8010',
    #                '121.12.42.216:61234']
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies


def getUserAgent():
    USER_AGENTS = [
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    ]

    return random.choice(USER_AGENTS)


# 将信息写入数据库中
def getNamelist():
    db = getConnDb()
    cursor = db.cursor()
    # 将爬取的数据插入到数据库中
    sql = 'insert into bid_view(bidnotic,bidurl,bidtime,procurement,agency,address,category,) VALUES ()'
    # sql = 'select url,name,engorg FROM company_url a JOIN (select id from company_url where type=0 limit 0, 100) b ON a.ID = b.id'
    num = cursor.execute(sql)  # 返回查询数量
    # info = cursor.fetchmany(num)#利用返回的数量查找相应的数据
    db.commit()
    close(db, cursor)
    # return info#返回查找到数据库的数据（url等信息）


def crawlBid(url):
    web_data = requests.get(url, headers=headers, proxies=proxies, timeout=10)
    html = etree.HTML(web_data.text)
    # print web_data.text

    # html = unicode(html, 'utf-8')
    # 中标公告
    bidNotic = html.xpath('*//ul[@class="vT-srch-result-list-bid"]/li/a/text()')
    # 中标链接
    bidNoticURL = html.xpath('*//ul[@class="vT-srch-result-list-bid"]/li/a/@href')
    # 中标详情
    bidDetail = html.xpath('*//ul[@class="vT-srch-result-list-bid"]/li/span/text()')
    # 中标地址
    bidAddress = html.xpath('*//ul[@class="vT-srch-result-list-bid"]/li/span/a//text()')
    # 中标类型
    bidCategory = html.xpath('*//ul[@class="vT-srch-result-list-bid"]/li/span/strong[2]//text()')
    print "bidNoticURL is length:", len(bidNoticURL)
    print "bidNotic is length:", len(bidNoticURL)
    print "bidDetail is length:", len(bidDetail)
    # 通过循环将网页的空白数据过滤，将整块有用信息放入bidDetailList
    for num in range(0, 100, 5):
        item = bidDetail[num].strip()
        bidDetailList.append(item)
    print len(bidDetailList)

    for item in bidDetailList:
        # biditem是一个列表
        biditem = item.split("|")
        # 把biditem列表放入最终列表中
        endbidDetailList.append(biditem)

    data_len = len(bidDetailList)

    for num in xrange(0, data_len):
        notic = bidNotic[num]
        notic_url = bidNoticURL[num]
        detail = bidDetailList[num]
        address = bidAddress[num]
        category = bidCategory[num]
        date = endbidDetailList[num][0]
        purchaser = endbidDetailList[num][1]
        proxy = endbidDetailList[num][2];

        print notic
        print notic_url
        print detail
        print address
        print category
        print date
        print purchaser
        print proxy
        print '***********'

        # 插入数据库













        # for itembidNotic in bidNotic:

        # print "@@@@", biditem[1].strip()

        # for itembidNotic in bidCategory:
        #     print itembidNotic.strip()
        # getNamelist()





        # itembidNotic 从列表中取出中标公告
        # itembidNoticURL 从列表中取出中标URL
        # itembidDetailList 整体列表中的单个详情列表
        # for itembidNotic,itembidNoticURL,itemendbidDetailList,itembidAddress,itembidCategory in bidNotic,bidNoticURL,endbidDetailList,bidAddress,bidCategory:
        #     #时间
        #     timeDetail = itemendbidDetailList[0]
        #     #代理人
        #     procurement = itemendbidDetailList[2]
        #     #机构
        #     agency = itemendbidDetailList[3]
        #     print itembidNotic
        #     print itembidNoticURL
        #     print timeDetail
        #     print procurement
        #     print agency
        #     print itembidAddress
        #     print itembidCategory



        # getNamelist()

        # print bidDetailList[1]


if __name__ == '__main__':
    userAgent = getUserAgent()
    headers = {
        'User-Agent': userAgent,
        'Cookie': '111'
    }
    url = 'http://search.ccgp.gov.cn/bxsearch?searchtype=1&page_index=1&bidSort=0&buyerName=&projectId=&pinMu=&bidType=7&dbselect=bidx&kw=&start_time=2018%3A03%3A15&end_time=2018%3A03%3A15&timeType=6&displayZone=&zoneId=&pppStatus=0&agentName='
    crawlBid(url)
    # web_data = requests.get(url)

    # print bidDetailList
    # for it in bidDetailList:
    #     print it
    # with open(r'D:\aCrawlerTextTest\bidTest.txt','a') as f:
    #     f.write(item)
    # f.close

    # for item in bidNoticURL:
    #     with open(r'D:\aCrawlerTextTest\bidTest.txt','a') as f:
    #         f.write(item)
    #     f.close

    # for item in bidNotic:
    #     with open(r'D:\aCrawlerTextTest\bidTest.txt','a') as f:
    #         f.write(item)
    #
    # f.close
    # print bidDetail[2]
    # print "@@@@@@@@@@@@@"
    # print bidDetail
