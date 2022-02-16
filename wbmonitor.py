#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : B1ain
# Action    : 微博
# Desc      : 微博主模块

import requests, json, sys
import getpic
import content
import htmljiexi


class weiboMonitor():
    def __init__(self, ):
        self.reqHeaders = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Referer': 'https://passport.weibo.cn/signin/login',
            'Connection': 'close',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3'
        }
        self.uid = ['6395178860', '1906286443', '6626748101', '6626748101', '5663590461', '5594559637',
                    '7031421269', '7505006312', '7209505250', '6064752668', '3654410557', '5652423635', '2731935637', '5923121748', '5661268657', '2919901662','1739243731', '5404268788', '2408800551', '7595006312', '2385341970', '1887816474', '2471768860', '2205641702','7519401668', '2345988380', '5276062970', '1044475047','7651711775','6371457043','6375460788','6666213760','6371458040','7470197961','3224794192']  # 这里添加关注人的uid

    # 获取访问连接
    def getweiboInfo(self):
        try:
            self.weiboInfo = []
            for i in self.uid:
                userInfo = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=%s' % (i)
                res = requests.get(userInfo, headers=self.reqHeaders)
                for j in res.json()['data']['tabsInfo']['tabs']:
                    if j['tab_type'] == 'weibo':
                        self.weiboInfo.append(
                            'https://m.weibo.cn/api/container/getIndex?type=uid&value=%s&containerid=%s' % (
                                i, j['containerid']))
        except Exception as e:
            self.echoMsg('Error', e)
            sys.exit()

    # 收集已经发布动态的id
    def getWBQueue(self):
        try:
            self.itemIds = []
            for i in self.weiboInfo:
                res = requests.get(i, headers=self.reqHeaders)
                with open('wbIds.txt', 'a') as f:
                    for j in res.json()['data']['cards']:
                        if j['card_type'] == 9:
                            f.write(j['mblog']['id'] + '\n')
                            self.itemIds.append(j['mblog']['id'])
            self.echoMsg('Info', '微博数目获取成功')
            self.echoMsg('Info', '目前有 %s 条微博' % len(self.itemIds))
        except Exception as e:
            self.echoMsg('Error', e)
            sys.exit()

    # 开始监控
    def startmonitor(self, ):
        returnDict = {}  # 获取微博相关内容，编辑为邮件
        try:
            itemIds = []
            with open('wbIds.txt', 'r') as f:
                for line in f.readlines():
                    line = line.strip('\n')
                    itemIds.append(line)
            for i in self.weiboInfo:
                res = requests.get(i, headers=self.reqHeaders)
                for j in res.json()['data']['cards']:
                    if j['card_type'] == 9:
                        if str(j['mblog']['id']) not in itemIds:
                            with open('wbIds.txt', 'a') as f:
                                f.write(j['mblog']['id'] + '\n')
                            self.echoMsg('Info', '发微博!')
                            self.echoMsg('Info', '目前有 %s 条微博' % (len(itemIds) + 1))
                            idd = str(j['mblog']['id'])
                            # 以下输出微博内容

                            txt = j

                            createtime = j['mblog']['created_at']
                            sourcel = j['mblog']['source']
                            fasname = j['mblog']['user']['screen_name']
                            # deit = j['mblog']['edit_config']['edited']
                            try:
                                deit = j['mblog']['edit_config']['edited']

                            except:
                                deit = False

                            reposts = j['mblog']['reposts_count']
                            attitudes = j['mblog']['attitudes_count']
                            comments = j['mblog']['comments_count']
                            picnum = j['mblog']['pic_num']
                            content.wbcontent(txt, createtime, sourcel, fasname, deit, reposts, attitudes, comments,
                                              idd)
                            # 以下输出微博图片
                            htmljiexi.getpiclast(idd)

                            # urll = i
                            # getpic.getweibopic(idd, urll)
                            # print("这是微博id" + str(j['mblog']['id']))  # 这是微博id
                            # print("这是微博url的链接" + i)  # 这是微博url的链接
                            # print(j)  # 这是微博的【】内容是list
                            returnDict['created_at'] = j['mblog']['created_at']
                            returnDict['text'] = j['mblog']['text']
                            returnDict['source'] = j['mblog']['source']
                            returnDict['nickName'] = j['mblog']['user']['screen_name']
                            return returnDict
        except Exception as e:
            self.echoMsg('Error', e)
            sys.exit()

    # 格式化输出
    def echoMsg(self, level, msg):
        if level == 'Info':
            print('[Info] %s' % msg)
        elif level == 'Error':
            print('[Error] %s' % msg)



# if __name__ == '__main__':
#     w = weiboMonitor()
#     w.getweiboInfo()
#     with open('wbIds.txt', 'r') as f:
#         text = f.read()
#         if text == '':
#             w.getWBQueue()
#     newWB = w.startmonitor()

