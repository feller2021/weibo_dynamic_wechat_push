# coding:utf-8
import shipindizhi
def bofang(idd):
    spurl = shipindizhi.shipinpaly(idd)
    a = '<script src="https://static.guanqi.xyz/libs/dplayer/1.26.0/js/DPlayer.min.js"></script>'
    b = '<link class="dplayer-css" rel="stylesheet" href="https://cdn.bootcdn.net/ajax/libs/dplayer/1.9.1/DPlayer.min.css">'
    c = '<div id="dplayer"></div>'
    d = "<script>const dp = new DPlayer({container: document.getElementById('dplayer'),video: {url: '"
    e = "',},});</script>"
    zz = a + b + c + d + spurl + e
    print(zz)
    return zz
