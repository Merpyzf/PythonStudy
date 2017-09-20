# coding: utf-8
# WSGI python内置服务器程序的使用
from wsgiref.simple_server import make_server
from Hello import application

# 创建一个服务器，处理函数是application
httpd = make_server('127.0.0.1', 8000, application)
print 'Serving HTTP on port 8000...'
# 开始监听Http请求
httpd.serve_forever()
# 无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。
# HTTP请求的所有输入信息都可以通过environ获得,HTTP响应的输出都可以通过start_response()加上函数返回值作为Body。
# 复杂的Web应用程序，光靠一个WSGI函数来处理还是太底层了，我们需要在WSGI之上再抽象出Web框架，进一步简化Web开发。



