# coding:utf-8

def fun(*args, **kwargs):
    print type(args)  # 元组类型
    print args
    print type(kwargs)  # 字典类型
    print kwargs


if __name__ == '__main__':
    fun(1, 2, 3, 4, name='hello');
