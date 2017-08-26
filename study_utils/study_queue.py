# -*- coding:utf-8 -*-
import Queue
from multiprocessing import Process


# 测试 Queue中的join方法对调用进程的阻塞

def fun_process():
    print "fun_process ==> 子进程"
    while not fifo_queue.empty():
        # get 从队列中返回并移除一个数据,参数作用于get类似
        print fifo_queue.get()
        # 返回队列中元素的数量
        print '队列中元素的数量：', fifo_queue.qsize()
        fifo_queue.task_done()


fifo_queue = Queue.Queue(10);

if __name__ == '__main__':

    for x in range(10):
        # 带有阻塞的添加，如果在添加的过程中队列已经装满，此时将阻塞5秒钟，如果队列任然没有空间则会抛出 Queue.full异常
        fifo_queue.put(x, True, 5)
    # 创建一个子进程
    process = Process(target=fun_process, );
    process.start()
    # fifo_queue.join()  # 阻塞调用线程，直到队列中的任务全都被处理掉

    print "执行完毕"


# queue的put方法:

#   fifo_queue.put(item, block ,timeout)
#     1.如果可选参数block为True且timeout为空对象(默认情况，阻塞调用，无超时)
#     2.如果timeout是个正整数，阻塞调用进程最多timeout秒，如果一直无空空间可用，抛出Full异常（带超时的阻塞调用）
#     3.如果block为False，如果有空闲空间可用将数据放入队列，否则立即抛出Full异常    Queue.Full
