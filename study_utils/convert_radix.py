# coding:utf-8
"""
进制转换工具 10进制 -> 36进制
"""
import time
def get_chars():
    chars = []
    for x in range(97, 123):
        chars.append(chr(x))
    return chars


def convert(num):
    """
    进制转换函数 10 -> 36
    :param num:
    :return:
    """
    radix = 36
    chars = get_chars()
    results = []
    while True:
        mod = num % radix
        num = num / radix
        if (mod >= 10):
            results.append(chars[mod - 10])
        else:
            results.append(mod)
        if (num == 0):
            break
    results.reverse()
    result = ""
    for i in range(0, results.__len__()):
        results[i] = str(results[i])
    result = "".join(results)
    return result


if __name__ == '__main__':

    t = int(round(time.time()*1000))
    print t
    result = convert(t)
    print result
