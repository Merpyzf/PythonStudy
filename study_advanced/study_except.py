# coding: utf-8
# python异常处理
# python中常见的异常类型
# AssertionError assert语句失败
# AttributeError 试图访问一个对象没有的属性
# IOError 输入异常, 基本是无法打开文件
# ImportError 无法引入包或者包,基本上是路径问题
# IndentationError 语法错误,代码缩进的问题
# IndexError 下表索引超出序列边界
# KeyError 试图访问字典中不存在的键
# KeyboardInterrupt Ctrl+C 被按下,程序强制退出
# NameError 使用一个还未赋予对象的变量
# SyntaxError  python代码逻辑语法出错不能执行
# TypeError 传入的对象类型于要求的不符合
# UnboundLocalError 试图访问一个还未设置的全局变量,基本上是由于另一个同名的全局变量
# ValueError 传入一个不被期望的值,即使类型正确

# 使用Exception捕捉全局的错误

def fun_io_error():
    f = open('test.txt', 'r')
    # 异常的抛出机制:

    # 1. 如果运行时发生异常,解释器会查找相应的异常处理语句
    # 2. 要是在当前函数中没有找到,它会将异常逐次传递给上层的调用函数,如果在最外层中还没有找到的话，解释器就会退出，同时打印出traceback
    #    以便让用户找到错误产生的原因。


def fun_test():
    try:
        fun_io_error()  # 此处的函数内出现异常如果函数内未被处理,它会将异常传递给上层调用的函数,看看调用处是否可以进行处理
        print aa  # name 'aa' is not defined
        f = open('test.txt', 'r')
        # 打开一个不存在的文件，出错 IOError: [Errno 2] No such file or directory: 'test.txt'
        # 为了避免程序出错需要对异常进行捕获
    except IOError, e:
        print type(e)  # <type 'exceptions.IOError'>
        print e  # 打印错误的信息
    except NameError, e:
        print type(e)  # <type 'exceptions.IOError'>
        print e  # 打印错误的信息
    finally:
        print '无论是否出错，最终都要执行的代码'


if __name__ == '__main__':
    # fun_test()
    name = raw_input("please input your filename:")
    if name == 'hello':
        raise NameError('input file name error!') # 使用raise关键字来抛出一个异常,注意这里定义的异常类型必须是python所提供的



