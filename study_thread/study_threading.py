# -*- coding:utf-8 -*-
# 线程threading模块使用

import threading
from time import ctime, sleep


def music(func):
    for i in range(2):
        print "I am listening to %s. at %s" % (func, ctime())
        sleep(1)


def moive(func):
    for i in range(2):
        print "I am watching %s. at %s" % (func, ctime())
        sleep(1)


threads = []

t1 = threading.Thread(target=music, args=(u'山阴路的夏天',))
t2 = threading.Thread(target=moive, args=(u'断背山', ))

threads.append(t1)
threads.append(t2)

if __name__ == "__main__":
    for t in threads:
        # 守护进程
        t.setDaemon(True)
        t.start()

    for t in threads:
        t.join()

    print "all over %s" % (ctime())
