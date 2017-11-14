# coding:utf-8

#  树莓派小车服务端控制程序
import tornado.web

from tornado.options import define, options

define("port", default=8000, help="run on the give port", type=int)


class CarAction(tornado.web.RequestHandler):
    def get(self, input):
        if input == 'up':
                print "向前行驶"
        elif input == 'down':
                print "向后行驶"
        elif input == 'left':
                print "向左行驶"
        elif input == 'right':
                print "向右行驶"


if __name__ == '__main__':
    tornado.options.parse_command_line()
    print "服务开启 >>>>>"
    app = tornado.web.Application(

        handlers=[
            (r"/action/(\w+)", CarAction),
        ]
    )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
