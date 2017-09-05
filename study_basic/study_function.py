# coding: utf-8
# python中的函数只能先定义然后再调用,但是从可读性上说，把程序主干放到文件的结尾可读性差,可以把程序的主函数放在开头,然后在程序最后调用main()
# 函数


def main():
    fun()
    fun1()


# python中函数的命名一般使用 小写字母和下划线、数字等组合
def fun():
    print 'hello'


def fun1():
    print 'hello1'


# fun() # python中的函数只能先定义然后再调用


main()
