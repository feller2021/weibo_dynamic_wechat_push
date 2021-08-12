#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : B1ain
# Action    : 微博
# Desc      : 微博主模块
import time
from datetime import datetime, timedelta

import requests, json, sys
import re


def trans_format(time_string, from_format, to_format='%Y.%m.%d %H:%M:%S'):
    """
    @note 时间格式转化
    :param time_string:
    :param from_format:
    :param to_format:
    :return:
    """
    time_struct = time.strptime(time_string, from_format)
    times = time.strftime(to_format, time_struct)
    return times
    global a

def wbcontent(txt, createtime, sourcel, fasname, deit, reposts, attitudes, comments, picnum, idd):
    AAA = txt['mblog']['text']
    span = re.sub('<span(.*?)</span>', '', AAA)
    atab = re.sub('<a(.*?)</a>', '', span)
    img = re.sub('<img alt(.*?)/>', '', atab)
    bra = re.sub('<br />', '', img)
    # print(bra)
    format_time = trans_format(createtime, '%a %b %d %H:%M:%S +0800 %Y', '%Y-%m-%d %H:%M:%S')
    # print(format_time)
    # print(sourcel)
    # print(fasname)
    if deit == True:
        deit = '已编辑'
    else:
        deit = ''

    # print(deit)
    #
    # print(reposts)
    # print(comments)
    # print(attitudes)
    # print(picnum)
    # https://m.weibo.cn/status/4669358909428804
    detalurl = "https://m.weibo.cn/status/" + idd

    # print(type(deit))

    reposts2 = str(reposts)
    comments2 = str(comments)
    attitudes2 = str(attitudes)
    picnum2 = str(picnum)

    # print(type(reposts2))
    # print(type(comments2))
    # print(type(attitudes2))
    # print(type(picnum2))
    # print(type(format_time))

    now = datetime.now()
    a= now + timedelta(hours=16)
    # a = now
    dc = a.strftime("%H:%M:%S")
    tzshj = dc
    print("github通知时间是："+tzshj)
    d1=a.strftime('%Y-%m-%d %H:%M:%S')
    print("github时间d1是："+d1)
    d3 = datetime.strptime(d1, '%Y-%m-%d %H:%M:%S')
    print(d3)

    d2 = datetime.strptime(format_time, "%Y-%m-%d %H:%M:%S")

    timedelay = d3 - d2

    # timedelay=timedelay.strftime("%H:%M:%S")

    # delay11 = timedelay.strftime('%M')
    # print(type(timedelay))
    timedelay=str(timedelay)
    print(timedelay)

    imgpost = 'https://push.bot.qw360.cn/send/e54011f0-f9aa-11eb-806f-9354f453c154'
    headers = {'Content-Type': 'application/json'}
    fasongneir = '@' + fasname + '\n' + format_time + ' ' + '来自 ' + sourcel + ' ' + '\n' + '✔' + picnum2 + '张图' + ' ' + '\n' + '✔' + deit + reposts2 + '转' + ' ' + attitudes2 + '赞' + ' ' + comments2 + '评' + ' ' + '\n' + '✔' + '推送时间：' + tzshj + ' ' + '\n' + '✔' + '延时推送：' + timedelay  + ' ' + '\n' + '✔' + '原博链接：' + detalurl + ' ' + '\n' + '\n' + '◕‿-｡　｡◕‿◕' + '\n' + bra + '\n' + '◕‿-｡　｡◕‿◕'
    print(fasongneir)
    postdata = json.dumps({"msg": fasongneir})
    time.sleep(4)
    repp = requests.post(url=imgpost, data=postdata, headers=headers)

#
# if __name__ == '__main__':
#     wbcontent(1)
