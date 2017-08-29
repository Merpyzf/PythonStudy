# -*- coding:utf-8 -*-
import multiprocessing
import threading


# 测试死循环对cpu的占用

def loop():
    x = 0
    while True:
        x = x * x


if __name__ == '__main__':
    # 四核的cpu
    for i in range(multiprocessing.cpu_count()):
        t = threading.Thread(target=loop)
        t.start()
