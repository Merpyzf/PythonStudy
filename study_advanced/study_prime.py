#!coding=utf-8
num1 = input("请输入一个数：")
num2 = input("请输入一个数：")


def is_prime(num):
    """
    判断质数的方法，如果是质数返回True不是质数返回Fale
    :param num:
    :return:
    """
    if num1 > 1:
        for i in range(2, num1):
            if (num1 % i) == 0:
                print num1, u'不是质数'
                return False
        else:
            return True
    else:
        print num1, u'不是质数'
        return False


if __name__ == "__main__":

    if is_prime(num1) and is_prime(num2):
        sum = num1 + num2
        h = num2 - num1
        q = num2 / num1
        r = num2 % num1
        print u'和是:', sum
        print u'差是:', h
        print u'商是:', q
        print u'余是:', r
    else:

        print '有一个数不是质数无法进行计算！'
