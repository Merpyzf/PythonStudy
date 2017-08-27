# -*- coding:utf-8 -*-
import time, threading

# 多线程与多进程之间最大的不同，多进程中，同一个变量，各自有一份拷贝与每个进程中，互不影响，多线程中，所有的变量都由所有的线程共享
# 所以，任何一个变量都可以被任意一个线程修改，因此线程之间共享数据的危险在于多个线程同时改变一个变量，造成线程安全问题。
# 以下面的修改账户余额为例，按道理讲最后的余额应该是0，但是由于多个线程进行操作，于是就产生了线程安全问题，造成结果有时不为0
# 产生的原因是因为：
# 高级语言的一条语句在Cpu执行时是若干条语句，即使一个简单的计算：
# balance = balance + n
# 也分为两步



# 银行存款余额
balance = 0


# 对余额进行更改
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
threading.loc

def run_thread(n):
    for i in range(1000000):

        change_it(n)


if __name__ == '__main__':

    # 创建两个线程对余额同时操作
    t1 = threading.Thread(target=run_thread, args=(10,))
    t2 = threading.Thread(target=run_thread, args=(5, ))

    t1.start()
    t2.start()
    print '余额', balance


