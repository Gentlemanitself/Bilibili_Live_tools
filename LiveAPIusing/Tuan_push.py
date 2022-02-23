import requests
from bilibili_api import live
import time


def send_wechat(title, content):
    """Send Message."""
    payload = {
        "summary": title,
        "content": content,
        "appToken": "AT_xx",
        "contentType": 1,
        "topicIds": [1411],
        "url": "https://live.bilibili.com/34027"
    }

    url = 'http://wxpusher.zjiecode.com/api/send/message'
    return requests.post(url, json=payload).json()


status = 0
while True:
    v = live.get_room_play_info(room_display_id=34027)
    if(v['live_status'] == 1 and status == 0):
        send_wechat(title='团子开播了！！！', content="久等了！快去直播间看小团子酱Dango吧！！！")
        status = 1
    elif(v['live_status'] != 1 and status == 1):
        status = 0
    time.sleep(100)
