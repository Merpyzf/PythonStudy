# -*- coding: utf-8 -*-

import time

myDict = dict()

myDict['ToUserName'] = "小明"
myDict['ToUserName'] = "小莉"
myDict['CreateTime'] = int(time.time())
myDict['Content'] = "这是一个内容"

print str(time.time())



XmlForm = """
        <xml>
        <ToUserName><![CDATA[{ToUserName}]]></ToUserName>
        <FromUserName><![CDATA[{ToUserName}]]></FromUserName>
        <CreateTime>{CreateTime}</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[{Content}]]></Content>
        </xml> """

print XmlForm.format(**myDict)