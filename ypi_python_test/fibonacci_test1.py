# coding:utf-8
# 递归实现斐波那契数列
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

if __name__ == '__main__':
    print fib(20)
