#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from datetime import datetime, timedelta
import htmljiexi
import tyoi
from django.template.defaultfilters import striptags
import requests, json, sys
import re
import wbtxt


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


def wbcontent(txt, createtime, sourcel, fasname, deit, reposts, attitudes, comments, idd):
    global a
    AAA = txt['mblog']['text']
    AAA = str(AAA)
    bra = striptags(AAA)

    #     span = re.sub('<span(.*?)</span>', '', AAA)
    #     atab = re.sub('<a(.*?)</a>', '', span)
    #     img = re.sub('<img alt(.*?)/>', '', atab)
    #     bra = re.sub('<br />', '', img)
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
    braa = wbtxt.lasttxt(idd)

    # print(type(deit))

    reposts2 = str(reposts)
    comments2 = str(comments)
    attitudes2 = str(attitudes)
    shuliang = htmljiexi.mun(idd)
    picnum2 = str(shuliang)
    ycwb = htmljiexi.isyuanchuang(idd)
    isyuanchuang = str(ycwb)
    isycsp1 = tyoi.isshipiin(idd)
    isycsp = str(isycsp1)

    now = datetime.now() + timedelta(hours=8)

    dc = now.strftime("%H:%M:%S")
    tzshj = dc
    print("github通知时间是：" + tzshj)
    d1 = now.strftime('%Y-%m-%d %H:%M:%S')
    print("github时间d1是：" + d1)
    d3 = datetime.strptime(d1, '%Y-%m-%d %H:%M:%S')
    print(d3)

    d2 = datetime.strptime(format_time, "%Y-%m-%d %H:%M:%S")

    timedelay = d3 - d2

    timedelay = str(timedelay)
    print(timedelay)

    
    lianjie = ''
    pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # 匹配模式

    # string = 'Its after 12 noon, do you know where your rooftops are? http://tinyurl.com/NYCRooftops '
    url = re.findall(pattern, detalurl)
    for urll in url:
        # print(urll)
        lianjie = urll
    lianjie2 = "<a href = " + lianjie + ">点击该链接</a>"

    imgpost = 'https://push.bot.qw360.cn/send/3325bea0-9939-11ec-9d03-6b5ca40f70fe'
    # e54011f0-f9aa-11eb-806f-9354f453c154
    # 3325bea0-9939-11ec-9d03-6b5ca40f70fe

    # headers = {'Content-Type': 'application/json'}
    # fasongneir = '@' + fasname + '\n' + format_time + ' ' + '来自 ' + sourcel + ' ' + '\n' + '▷' + isyuanchuang + '微博' + ' ' + isycsp + '\n' + '▷' + picnum2 + '张图' + ' ' + '\n' + '▷' + deit + ' ' + reposts2 + '转' + ' ' + attitudes2 + '赞' + ' ' + comments2 + '评' + ' ' + '\n' + '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay + ' ' + '\n' + '▷' + '原博链接：' + lianjie2 + ' ' + '\n' + '------------------------' + '\n' + braa + '\n' + '------------------------'
    # print(fasongneir)
    fasongneir = '@' + fasname + '\n'+'消息类型：普通推送'+ '<br>' + format_time + ' ' + '来自 ' + sourcel + ' ' + '<br>' + '▷' + isyuanchuang + '微博' + ' ' + isycsp + '<br>' + '▷' + picnum2 + '张图' + ' ' + '<br>' + '▷' + deit + ' ' + reposts2 + '转' + ' ' + attitudes2 + '赞' + ' ' + comments2 + '评' + ' ' + '<br>' + '▷' + '推送时间：' + tzshj + ' ' + '<br>' + '▷' + '延时推送：' + timedelay + ' ' + '<br>' + '▷' + '原博链接：' + lianjie2 + ' ' + '<br>' + '------------------------' + '<br>' + braa + '<br>' + '------------------------'
    # postdata = json.dumps({"msg": fasongneir})
    time.sleep(4)
    # repp = requests.post(url=imgpost, data=postdata, headers=headers)

    huanghang = "<br />"
    tupianxianshi = '<meta name="referrer" content="no-referrer" />'
    tu = htmljiexi.getpiclast(idd)
    content = fasongneir + huanghang + tupianxianshi + tu
    content = content.replace('"', '\"')
    content = content.replace('\ "', '\"')

    # print(content)
    url = 'http://wxpusher.zjiecode.com/api/send/message'
    HEADERS = {'Content-Type': 'application/json'}
    FormData = {
        "appToken": "AT_iaPxpUE0FLNUECu1zFnKhFR7R9NU5K8e",
        "content": content,
        "summary": f"[普通]@" +fasname + '\n' +'微博发送时间：'+format_time +'\n'+ '▷'+isyuanchuang + '微博' + ' ' + isycsp + '\n' + '▷'+ picnum2 + '张图' +  '\n' + '▷' + '推送时间：' + tzshj + ' ' + '\n' + '▷' + '延时推送：' + timedelay,
        "contentType": 2,

        "topicIds": [

        ],
        "uids": [
            "UID_noWsar4x3r0zd4WqjCaoD5CIX9Xi"
        ],
        "url": ""
    }
    res = requests.post(url=url, json=FormData, headers=HEADERS)
    print(res.text)

#
# if __name__ == '__main__':
#     wbcontent(1)
