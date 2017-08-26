# -*- coding:utf-8 -*-
import os
from multiprocessing import Process

num = 10


# 使用fork()函数创建进程
def fun_fork():
    print 'Process(%s)start.....' % os.getpid()
    pid = os.fork()
    if pid == 0:
        print 'I am child process(%s) and my parent is %s' % (os.getpid(), os.getppid())
    else:
        print 'I (%s) just create a child process(%s).' % (os.getpid(), pid)


# 子进程要执行的代码
def run_proc(name):
    print num
    print '运行在子线程%s (%s) .' % (name, os.getpid())


if __name__ == '__main__':
    print "父线程 %s ." % os.getpid()
    # 创建一个子进程 需要传递的参数（方法名， 方法中的参数 ）
    p = Process(target=run_proc, args=('wangke',))
    p.start()
    p.join()  # join()方法可以等待子线程的执行结束后再继续往下执行，通常用于进程间同步
    print '线程执行结束'
