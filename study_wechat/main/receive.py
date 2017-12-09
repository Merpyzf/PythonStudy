# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET


def handle_msg(web_data):
    if len(web_data) == 0:
        return None
    xmlData = ET.fromstring(web_data)
    # 获取发送消息的类型
    msg_type = xmlData.find('MsgType').text
    if msg_type == "text":
        return TextMsg(xmlData)
    elif msg_type == 'image':
        print "发送的这是一个图片"
    elif msg_type == 'event':
        return ClickEvent(xmlData)


class Msg(object):
    def __init__(self, xmlData):
        self.ToUserName = xmlData.find('ToUserName').text
        self.FromUserName = xmlData.find('FromUserName').text
        self.CreateTime = xmlData.find('CreateTime').text
        self.MsgType = xmlData.find('MsgType').text


class TextMsg(Msg):
    """
    文本消息类，封装文本消息
    """

    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.content = xmlData.find('Content').text.encode("utf-8")


class ClickEvent(Msg):
    """
    封装点击事件的消息内容
    """

    def __init__(self, xmlData):
        Msg.__init__(self, xmlData)
        self.Event = xmlData.find('Event').text
        self.EventKey = xmlData.find('EventKey').text
