# -*- coding: utf-8 -*-
import time


if __name__ == "__main__":
    print (time.time())
    curr_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    print curr_time

