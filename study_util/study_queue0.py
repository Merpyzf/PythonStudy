# -*- coding:utf-8 -*-
import Queue


# Queue是python标准库中的线程安全的队列（FIFO）实现,提供了一个适用于多线程编程的先进先出的数据结构，即队列，用来在生产者和消费者线程之间的信息传递

# FIFO (First in First out) 先进先出
def fun_fifo_queue():
    q = Queue.Queue()

    for i in range(6):
        q.put(i)

    while not q.empty():
        print q.get()

        # 表示之前入队的一个任务执行完成。由队列的消费者线程调用。每一个get()调用得到一个任务，接下来的task_down()调用告诉队列
        # 该任务已经处理完毕
        q.task_done()


# LIFO （Last in First out）后进先出
def fun_lifo_queue():
    q = Queue.LifoQueue()
    for i in range(5):
        q.put(i)

    while not q.empty():
        print q.get()
        q.task_done()


if __name__ == '__main__':
    # 先进先出
    # fun_fifo_queue()

    # 后进先出
    fun_lifo_queue()
