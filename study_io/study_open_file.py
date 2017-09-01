# -*- coding:utf-8 -*-

file = open('../study_net/study_requests.py')
print file.fileno()
print file.mode
print file.tell()
for line in file.readlines():
    print line

    file.close()
