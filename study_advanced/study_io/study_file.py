# -*- coding:utf-8 -*-
import sys
import io
import os
import fileinput


# 打开文件以读写的方式打开
def open_file(file_name):
    file = open(file_name, 'r+|w+')
    return file


def read_file(file):
    print '未进行文件操作时的文件指针的位置->', file.tell()
    # 读取一行文件
    print file.readline()
    # 使用seek进行文件指针的移动
    file.seek(-file.tell(), io.SEEK_CUR)
    # 获取当前文件指针的位置
    print '文件操作后的文件指针的位置->', file.tell()

    # 使用迭代器读取文件 iter方法，文件指针后移
    for line in iter(file):
        print 'iter=>' + line

    file.close()


def test_io():
    # 获取输入的命令行参数的值是一个list的形式,第一个值为文件本身，后面的值才
    print type(sys.argv)
    print sys.argv


def write_file(file):
    # for num in range(1, 10000):
    #     file.write('test write' + str(num)+"\n")

    print file.readlines()
    file.close()



if __name__ == '__main__':
    test_io()
    # read_file(open_file('test_io'))
    # write_file(open_file('test_io'))
    # f = open_file('test_io')
    #
    #
    # print os.getcwd()
    # print getdir('/Users/wangke')
    
    print os.path.isdir('/Users/wangke/test_io')