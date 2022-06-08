# coding:utf-8
import shipindizhi
def bofang(idd):
    spurl = shipindizhi.shipinpaly(idd)
    a = '<script src="https://static.guanqi.xyz/libs/dplayer/1.26.0/js/DPlayer.min.js"></script>'
    b = '<link class="dplayer-css" rel="stylesheet" href="https://cdn.bootcdn.net/ajax/libs/dplayer/1.9.1/DPlayer.min.css">'
    c = '<div id="dplayer"></div>'
    d = "<script type=\"text/javascript\">const dp = new DPlayer({container: document.getElementById('dplayer'),video: {url: '"
    e = "',},});</script>"
    # 该消息平台如果用JavaScript，会屏蔽，也就是去掉JavaScript代码，故用H5 原生<video>标签实现
    zz = a + b + c + d + spurl + e
    
    
    ff='<video src="'
    gg='" controls="controls" muted></video>'
    

    kkkk=ff+spurl+gg

    # print(zz)
    return kkkk
