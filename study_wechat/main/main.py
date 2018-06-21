# -*- coding:utf-8 -*-
import web

import verify
import replay
import receive

urls = (

    '/wx', 'handle',

)


class handle(object):
    def GET(self):
        data = web.input()
        print "GET: ", data
        return verify.check_token(data)

    def POST(self):
        data = web.data()
        print "POST: ", data
        # 处理消息，将事件中的内容封装成一个对象返回
        msg = receive.handle_msg(data)

        if msg.MsgType == 'text':
            replay_msg = replay.TextMsg(msg.FromUserName, msg.ToUserName, "https://www.baidu.com")
            return replay_msg.send()
        elif msg.MsgType == 'event':
            if msg.Event == 'CLICK':
                replay_msg = replay.TextMsg(msg.FromUserName, msg.ToUserName, msg.EventKey)
                print "回复消息"
                return replay_msg.send()

        return 'success'


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
