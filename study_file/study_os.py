# coding:utf-8
import os


def del_files(parent):
    path_dirs = os.listdir(parent)
    if path_dirs.__len__() > 0:
        for f in path_dirs:
            os.remove(parent_path + f)

if __name__ == "__main__":

    # 获取当前脚本所在的目录路径
    print os.getcwd()
    parent_path = 'test_file'
    del_files(parent_path)




