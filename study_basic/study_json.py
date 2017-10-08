import json


class Student(object):
    def __init__(self, name, pwd):
        self.name = name
        self.pwd = pwd


class UserEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Student):
            return obj.name
        return json.JSONEncoder.default(self, obj)


if __name__ == '__main__':
    s = Student("wangke", "wangke0310")
    json_str = json.dumps(s, default=lambda o: o.__dict__)
    print json_str
