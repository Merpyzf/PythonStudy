# -*- coding:utf-8 -*-
# 根据失效时间轮训获取access_token
import web
import requests
import json
import time

# 存放url的元组
urls = (

    '/get_token', 'AccessToken'

)

appId = "wxf2c5236e1f8e9f5f"
appSecret = "972515942a3f093e2c3604acb7dfff79"
failure_time = 0
access_token = ''


def get_token():
    """
    获取token
    :return:
    """
    postUrl = ("https://api.weixin.qq.com/cgi-bin/token?grant_type="
               "client_credential&appid=%s&secret=%s" % (appId, appSecret))
    # 获取access_token的时候需要使用https请求
    urlResp = json.loads(requests.get(postUrl).text)
    global failure_time
    global access_token
    # 将token失效的时间保存在内存中
    failure_time = int(time.time()) + int(urlResp['expires_in'])

    access_token = urlResp['access_token']
    return access_token


class AccessToken(object):
    def GET(self):
        global access_token
        curr_time = int(time.time())
        if curr_time > failure_time:
            print '从微信后台获取token'
            return get_token()

        return access_token


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
