# -*- coding: utf-8 -*-
import json
import requests
from wxpy import *


# 调用图灵机器人API，发送消息并获得机器人的回复
def auto_reply(text):
    url = "http://www.tuling123.com/openapi/api"
    api_key = "cc3404645cf64e38876f4fd99aa7d955"
    payload = {
        "key": api_key,
        "info": text,
        "userid": "123456"
    }
    r = requests.post(url, data=json.dumps(payload))
    result = json.loads(r.content)
    print result["text"]
    return result["text"]

bot = Bot(cache_path=True)
friend_group = bot.groups().search(u'白老师大讲堂')[0]
print friend_group
friend_name = friend_group.search(u'李扬')[0]
print friend_name

girl_friend = bot.friends().search(u'胖儿')[0]
print girl_friend

@bot.register([friend_group])
def forward_message(msg):
    print msg
    # if msg.member == u"ok绷":
    return auto_reply(msg.text)


embed()  # get_groups(bot)

