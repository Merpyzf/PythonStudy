# coding:utf-8

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def factorial2(n):
    result = 1
    for x in range(1, n + 1):
        result = result * x
    return result


if __name__ == '__main__':
    print factorial(10)
    print factorial2(10)
