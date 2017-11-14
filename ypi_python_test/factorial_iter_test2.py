# coding:utf-8

class factorial:
    def __init__(self):
        self.a = 1
        self.b = 1

    def next(self):
        self.a, self.b = self.a * self.b, self.b + 1
        return self.a

    def __iter__(self):
        return self


class factorial1:
    def __init__(self):
        self.a = 1
        self.b = 1

    def next(self):
        self.a, self.b = self.a * self.b, self.b + 1
        return self.a

    def __iter__(self):
        return self


if __name__ == '__main__':
    f = factorial()
    r = 10
    for i in range(11):
        f.next()
        if i == 10:
            pass
            # print f.next()
        else:
            pass
            # print f.next()
