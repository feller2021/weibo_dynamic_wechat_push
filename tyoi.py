import json
import sys
import time
from pprint import pprint

import requests
import re
from lxml import etree

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://m.weibo.cn/u/'  # 这个需要改成所要爬取用户主页的手机版本下的url
}
# 4719775370709123
def isshipiin(idd):
    id = idd
    realurl = 'https://m.weibo.cn/status/%s' % id
    res = requests.get(realurl, headers=header)

    res.encoding = 'utf-8'
    root = etree.HTML(res.content)

    gameList = root.xpath("/html/body/script[1]/text()")

    for i in gameList:

        i = i.replace('\n', '').replace('\r', '')
        list1 = re.findall('data = \[(.*?)\]\[0\]', i)
        for j in list1:
            # pprint(type(j))
            # print(j)
            # j = j.replace("\'", '"')
            objson = json.loads(j)
            k = objson['status']
            t = 'retweeted_status'
            try:
                if t not in k:
                    # print("原创视频")
                    ycsp = k['page_info']['type']
                    # print(type(ycsp))
                    if ycsp == 'video':

                        ycspp = '原创视频'
                        return ycspp
                    else:
                        return ""






                else:
                    ycsp = k['retweeted_status']['page_info']['type']
                    if ycsp == 'video':

                        ycspp = '转发视频'
                        return ycspp
                    else:
                        return ""
            except Exception as e:
                return ""
                sys.exit()

def echoMsg(self, level, msg):
    if level == 'Info':
        print('[Info] %s' % msg)
    elif level == 'Error':
        print('[Error] %s' % msg)







#
# if __name__ == '__main__':
#     # isshipiin(4669819553058321)
#     sd=isshipiin(4719775370709123)
#
#     print(sd)
