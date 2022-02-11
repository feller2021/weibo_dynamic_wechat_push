import json
import time
from pprint import pprint

import requests
import re
from lxml import etree
import datetime
from django.template.defaultfilters import striptags



header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://m.weibo.cn/u/'  # 这个需要改成所要爬取用户主页的手机版本下的url
}

# 4677399825875715

def getgy(urlid):

    id = urlid
    #'https://m.weibo.cn/status/4725600311578496'
    realurl = 'https://m.weibo.cn/status/%s' % (id)
    res = requests.get(realurl, headers=header)

    res.encoding = 'utf-8'
    root = etree.HTML(res.content)


    gameList = root.xpath("/html/body/script[1]/text()")
    # print(gameList)
    for i in gameList:

        i = i.replace('\n', '').replace('\r', '')
        list1 = re.findall('data = \[(.*?)\]\[0\]', i)
    return list1

def gy(urlid):
    urlid = urlid


    for j in getgy(urlid):
        # print(j)
        objson = json.loads(j)
    return objson

def zhuanjson(urlid):
    urlid = urlid
    h = gy(urlid)
    h = str(h)
    jj = eval(h)
    j = json.dumps(jj)

    return j


def lasttxt(urlid):
    urlid = urlid
    g = zhuanjson(urlid)
    js = json.loads(g)
    dd = js['status']['text']

    content = striptags(dd)
    return content



if __name__ == '__main__':
    gt=lasttxt(4735729542370183)
    print(type(gt))
    print(gt)





