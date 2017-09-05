# coding: utf-8
fibs = [0, 1]


def fib(n):
    """
    递归获取斐波那契数列
    :param n:
    :return:
    """
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':

    # for x in range(0, 8):
        print fib(2)
