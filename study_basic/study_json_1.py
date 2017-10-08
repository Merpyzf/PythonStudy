import json
import datetime


class Student(object):
    def __init__(self, name, pwd, pet):
        self.name = name
        self.pwd = pwd
        self.nowdate = datetime.time()
        self.pet = pet


class Pet(object):
    def __init__(self, name, type):
        self.name = name
        self.type = type


if __name__ == '__main__':
    dog = Pet('xiaobai', 'dog')
    s = Student('wangke', 'wangke0310', dog)

    a = [
        {'group_id': {'name': 'wangke', 'age': 20, 'dataTime': datetime.time()}, 'group_name': 'group_1', 'item_id': 1,
         'item_name': 'test_1'},
        {'group_id': 1, 'group_name': 'group_1', 'item_id': 2, 'item_name': 'test_2'},
        {'group_id': 1, 'group_name': 'group_1', 'item_id': 3, 'item_name': 'test_3'},
        {'group_id': 2, 'group_name': 'group_2', 'item_id': 4, 'item_name': 'test_4'},
        {'group_id': 2, 'group_name': 'group_2', 'item_id': 5, 'item_name': 'test_5'},
        {'group_id': 2, 'group_name': 'group_2', 'item_id': 6, 'item_name': 'test_6'},
    ]

    s = json.dumps(a)
    print s
