#!/usr/bin/python3
#coding=utf-8

from monitor import wbmonitor, bzmonitor, dymonitor
import requests
import urllib.parse
import json
import time

spkey = '88806f3e51f72337714104837f800677'


#推送函数
def notify(text):
    flag = True
    try:
        qs = urllib.parse.urlencode(
            dict(
                #一键免费推送信息到手机https://sre24.com/
                token="e874c767e46379511d9d566909b2ce92",  #token对应微信
                msg=text,
            ))
        rs = requests.get(url="https://sre24.com/api/v1/push?" + qs).json()
        assert int(rs["code"] / 100) == 2, rs
    except Exception as e:
        print(e)
        flag = False
    return flag

def wbweixin(dicts):
    text = "" + dicts['nickName'] + "发布微博\n"
    text += "发送时间: " + dicts['created_at'] + "\n"
    flag = notify(text)
    return flag


def bzweixin(dicts):
    text = "" + dicts['nickName'] + "更新B站\n"
    flag = notify(text)
    return flag


def dyweixin(dicts):
    text = "" + dicts['nickName'] + "更新抖音\n"
    flag = notify(text)
    return flag




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
        print(wbweixin(newWB))  #推送成功则输出True
    #B站部分
    b = bzmonitor.bzMonitor()
    b.getbzurl()
    with open('bilibili.txt', 'r') as f2:
        text = f2.read()
        if text == '':
            b.getBZQueue()
    newBZ = b.startbzmonitor()
    if newBZ is not None:
        print(bzweixin(newBZ))
    #抖音部分
    d = dymonitor.dyMonitor()
    with open('douyin.txt', 'r') as f3:
        text = f3.read()
        if text == '':
            d.getDYQueue()
    newDY = d.startdymonitor()
    if newDY is not None:
        print(dyweixin(newDY))


if __name__ == '__main__':
    main()
