# -*- coding:utf-8 -*-
import os, time, random
import Queue
from multiprocessing import Process, Queue, Pool


# pool进程池的使用
def long_time_process(name):
    start = time.time()
    time.sleep(random.random() * 3)
    if not my_queue.empty():
        # 每一个子进程从队列中读取数据
        print "long_time_process%s（进程ID %s）从队列中取出的数 %s" % (name, os.getpid(), my_queue.get())
    else:
        print "到%s进程时，队列中的数据读取完毕" % name
    end = time.time()
    print '任务执行消耗的时间：%s' % (end - start)


# 队列数据结构 先进先出
my_queue = Queue(maxsize=10)

if __name__ == '__main__':
    # 创建一个队列，测试子进程是否能够公用父进程中的数据
    my_queue = Queue(maxsize=10)
    for x in xrange(10):
        my_queue.put(x)

    # p的默认大小为cpu的核数
    p = Pool()
    for i in xrange(11):
        p.apply_async(func=long_time_process, args=(i,))

    print "等待所有的子进程执行结束"
    p.close()  # 调用 join之前必须先调用close，之后不能再添加进程任务方法
    p.join()  # 等待所有的子线程执行完毕才会继续向下执行
    print "所有的子进程已经执行结束"
