# 爬取微博 Duebass的图片
import json
from urllib import request
import re
import ssl
import time
import pprint


# http://wallpaper.apc.360.cn/index.php?c=WallPaper&a=getAppsByCategory&cid=6&start=6590&count=50 #uid #fid

#需要将下面url里面的 uid&value=后面的数字换成所要爬取用户的uid，，还需要将containerid=这个替换成所要爬取用的的fid
import requests


def getweibopic(idd,urll):

    base_url = urll+'_-_main&page='

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://m.weibo.cn/u/'  # 这个需要改成所要爬取用户主页的手机版本下的url
    }
    imgpost='https://push.bot.qw360.cn/room/62b82c00-993b-11ec-9d03-6b5ca40f70fe'
     # 群 https://push.bot.qw360.cn/room/62b82c00-993b-11ec-9d03-6b5ca40f70fe
    # 个人 https://push.bot.qw360.cn/send/e54011f0-f9aa-11eb-806f-9354f453c154
    headers = {'Content-Type': 'application/json'}

    # 'https://m.weibo.cn/detail/4668413949250061'
    # def getweibopic(id):
    context = ssl._create_unverified_context()
    # 4668413949250061
    for i in range(0, 1):
        realurl = base_url + str(i)
        req = request.Request(url=realurl, headers=header)
        # resp = requests.get(realurl, headers=header)
        resp = request.urlopen(req, context=context).read().decode()
        # print('==============正在下载第' + str(i) + '页的图片===============')
        # 先获取所有的large里面的url，注意观察，大图的url中都包含/large,那么我们获取所有的url然后过虐掉不包含/large的url就行了
        # pat = '"url":"(.*?)"'
        # pat2 = '"id":"(.*?)"'
        # list1 = re.compile(pat).findall(resp)
        # list6 = re.compile(pat2).findall(resp)
        id = idd
        s = '"id":"%s"(.*?)picStatus' % id
        list7 = re.compile(s).findall(resp)
        print(list7)
        tt = ''
        a=[]


    for i in list7:
        tt = tt + i
        # tt=tt.text
        print(tt)
        lucky_num = re.compile('"pic_ids":\[(.*?)\],"').findall(tt)
        print("------------------")

        # print(lucky_num)
        for umg in lucky_num:
            th=umg
            pp=re.compile('"(.*?)"').findall(umg)
            print(type(pp))
            for lis in pp:
                jpg='https://wx4.sinaimg.cn/large/'+lis+'.jpg'
                # print(jpg)
                postdata = json.dumps({"msg": {"type": "image", "url": "%s" % jpg}})
                repp = requests.post(url=imgpost, data=postdata, headers=headers)
                time.sleep(4)
                # print(lis)https://wx4.sinaimg.cn/large/005JVMmmgy1gtf9cxhyuij318z0u0wk3.jpg






        # a = list(filter(lambda url: url.find('/large') != -1, lucky_num))
        # # print(type(a))
        #
        # print(a)
    # imgpost='https://push.bot.qw360.cn/send/e54011f0-f9aa-11eb-806f-9354f453c154'
    # headers = {'Content-Type': 'application/json'}
    # for j in a:
    #     pic_url = j.replace('\/', '/')
    #     # print(pic_url)
    #     imgurl=pic_url
    #     print(imgurl)
    #     postdata=json.dumps({"msg":{"type":"image","url":"%s" % imgurl}})
    #     repp=requests.post(url=imgpost, data=postdata, headers=headers)
    #     # print(repp)
    #     time.sleep(4)
    #
    #



#
#
# if __name__ == '__main__':
#     getweibopic()
