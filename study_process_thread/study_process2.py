# -*- coding:utf-8 -*-
import os, time, random
import Queue
from multiprocessing import Process, Queue, Pool


# 使用Queue来完成进程间通信

# 写数据进程执行的代码
def write(q):
    for value in ['A', 'B', 'C']:
        print 'put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())


def read(q):
    while True:
        # 阻塞住的,如果设置成False则表示不阻塞执行，如果调用get获取不到数据时候，会报出Empty异常
        value = q.get(False)
        print 'get %s from queue' % value


if __name__ == '__main__':
    q = Queue()
    # 开启一个写入的子进程
    pw = Process(target=write, args=(q,))
    # 开启一个读取的子进程
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()
    pw.join()
    # pr进程里执行的是死循环，无法等待其结束，只能够强行终止
    pr.terminate()


# 总结: 在Unix/Linux下可以使用fork()调用实现多线程。
# 要实现跨平台的多进程，可以使用 multiprocessing模块
# 进程间通信是通过 Queue、Pipes等 来实现的