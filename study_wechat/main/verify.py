# -*- coding:utf-8 -*-
import hashlib


def check_token(data):
    '''
    验证token
    :param data:
    :return:
    '''


    try:
        print data
        # 没有从get请求中获取参数列表，表示不是从微信公众号后台服务器发起的请求
        if len(data) == 0:
            return "hello, this is handle view"

        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        print "echostr: ", echostr
        token = "merpyzf"

        list = [token, timestamp, nonce]
        list.sort()

        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()

        print "验证token -> handle/GET func: hashcode,signature", hashcode, signature

        if hashcode == signature:
            return echostr
        else:
            print "验证失败"
            return ""

    except Exception, Argument:
        return Argument
