# coding:utf-8
# 递归实现斐波那契数列(非递归)

def fib(n):
    fib_list = [1, 1]
    for i in range(n-2):
        fib_list.append(fib_list[-1]+fib_list[-2])
    return fib_list[-1]

if __name__ == '__main__':
    print fib(20)
