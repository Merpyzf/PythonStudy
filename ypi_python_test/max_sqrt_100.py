import math
def max_sqrt(num):
    for n in range(num-1, 0, -1):
        max = math.sqrt(n)
        if max == int(max):
            print n
            break


if __name__ == '__main__':
    max_sqrt(100)
