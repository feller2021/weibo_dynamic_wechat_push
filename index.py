#!/usr/bin/python3
#coding=utf-8

import wbmonitor
import requests
import urllib.parse
import time

spkey = '88806f3e51f72337714104837f800677'

def trans_format(time_string, from_format, to_format='%Y.%m.%d %H:%M:%S'):
    """
    @note 时间格式转化
    :param time_string:
    :param from_format:
    :param to_format:
    :return:
    """
    time_struct = time.strptime(time_string,from_format)
    times = time.strftime(to_format, time_struct)
    return times

#推送函数
# def notify(text):
#     flag = True
#     try:
#         qs = urllib.parse.urlencode(
#             dict(
#                 #一键免费推送信息到手机https://sre24.com/
#                 token="e874c767e46379511d9d566909b2ce92",  #token对应微信
#                 msg=text,
#             ))
#         rs = requests.get(url="https://sre24.com/api/v1/push?" + qs).json()
#         assert int(rs["code"] / 100) == 2, rs
#     except Exception as e:
#         print(e)
#         flag = False
#     return flag
#
# def wbweixin(dicts):
#
#     created_at1=dicts['created_at']
#     format_time = trans_format(created_at1, '%a %b %d %H:%M:%S +0800 %Y', '%Y-%m-%d %H:%M:%S')
#     # dicts['created_at']
#     text = "" + "@"+ dicts['nickName'] + "发微博了\n" + "发送时间: " + format_time + "\n" + dicts['text']
#     flag = notify(text)
#     return flag


# def bzweixin(dicts):
#     text = "" + dicts['nickName'] + "更新B站\n"
#     flag = notify(text)
#     return flag
#
#
# def dyweixin(dicts):
#     text = "" + dicts['nickName'] + "更新抖音\n"
#     flag = notify(text)
#     return flag




def main(*args):
    #微博部分
    w = wbmonitor.weiboMonitor()
    w.getweiboInfo()
    with open('wbIds.txt', 'r') as f:
        text = f.read()
        if text == '':
            w.getWBQueue()
    newWB = w.startmonitor()
    if newWB is not None:
        print("wbweixin(newWB)")  #推送成功则输出True
    # #B站部分
    # b = bzmonitor.bzMonitor()
    # b.getbzurl()
    # with open('bilibili.txt', 'r') as f2:
    #     text = f2.read()
    #     if text == '':
    #         b.getBZQueue()
    # newBZ = b.startbzmonitor()
    # if newBZ is not None:
    #     print(bzweixin(newBZ))
    # #抖音部分
    # d = dymonitor.dyMonitor()
    # with open('douyin.txt', 'r') as f3:
    #     text = f3.read()
    #     if text == '':
    #         d.getDYQueue()
    # newDY = d.startdymonitor()
    # if newDY is not None:
    #     print(dyweixin(newDY))


if __name__ == '__main__':
    main()
