import requests
import re
from datetime import datetime

def shipinpaly(idd):
    s = datetime.now()
    resp = requests.get('https://m.weibo.cn/detail/%s' % idd)
    a = resp.text
    
    shipinurl=''
    matchObj = re.match('.*"mp4_720p_mp4": "(.*?)"', a, re.S)
    if matchObj==None:
        matchObj = re.match('.*"stream_url_hd": "(.*?)"', a, re.S)
    else:
        matchObj = re.match('.*"stream_url": "(.*?)"', a, re.S)
        

    if matchObj:
        # print(matchObj.group(1))
        shipinurl=matchObj.group(1)
    return shipinurl


