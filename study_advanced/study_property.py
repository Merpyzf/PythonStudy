# -*- coding:utf-8 -*-
# python中的 property（属性函数）

class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # 获取全名的方法
    @property
    def full_name(self):
        return self.first_name + self.last_name


class Computer(object):
    def __init__(self):
        self._brand = None

    # set方法
    def set_brand(self, brand):
        print 'set_brand被调用'
        self._brand = brand

    # get方法
    def get_brand(self):
        return self._brand

    brand = property(get_brand, set_brand)

    # 添加一个setter方法（相对于使用property装饰器生成属性,在给brand赋值时会先调用，下面的这个使用@brand.setter 创建的setter方法）
    @brand.setter
    def brand(self, brand):
        print 'brand被调用'
        self._brand = brand


if __name__ == '__main__':
    wk = Person('王', '珂')
    # print wk.full_name() 在没有添加 property进行装饰前获取全名需要通过.方法进行获取
    print wk.full_name  # 添加 property进行装饰之后,方法变成了属性
    # wk.full_name = '王娜'  报错 ： AttributeError: can't set attribute 不能以这种方式修改值，改变full_name值得方法只能通过修改
    # first_name 和 last_name 这两个属性值


    #     演示 使用Python property取代setter和getter方法

    # 没有使用 property 前的通常做法
    apple = Computer()
    apple.set_brand('MacBook Pro')
    print apple.get_brand()

    # 使用之后
    ausu = Computer()
    ausu.brand = '华硕笔记本'
    print ausu.brand
