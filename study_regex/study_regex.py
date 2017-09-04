# -*- coding:utf-8 -*-



# python正则表达式使用学习
import re

s1 = "hELlo world"

# re.I设置忽略大小写
# 1.先获取一个Pattern对象
pattern = re.compile(r"hello")

# 2.调用match方法进行匹配字符串
match = pattern.match(s1)

# ************使用正则对单个字符的匹配*******************

# “.”   匹配任意字符
# “[a-z]” 匹配字符集 a-z
# ma = re.match(r"\[[\w]\]", "[a]")


# ma = re.match(r"{[a-z]}", "{b}")
# ma = re.match(r"{[a-zA-Z0-9]}", "{0}")


# "\d" 匹配数字
# "\D" 匹配非数字

# "\s" 匹配空白
# "\S" 匹配非空白

# "\w" 匹配单词字符 [a-zA-Z0-9]
# "\W" 匹配非单词字符


#  ************使用正则表达式匹配多个字符*******************

# "*"匹配前一个字符0次或者无限次
# ma = re.match(r'A[a-z0-9]*', "Assdsesdefded1243")

# "+"匹配前一个字符1次或者无限次
# ma = re.match(r'[_a-zA-Z]+[\w]*', 'Aa_a')

# "?"匹配前一个字符0次或者1次
# ma = re.match(r'[1-9]?[0-9]', '99')

# {m} 匹配前一个字符m次

# {m,n}匹配前一个字符出现m-n次
# ma = re.match(r'[\d]{1,10}@[a-z]*.com', '1052060838@qq.com')

# "?"将匹配模式变为非贪婪模式

# "*?" 匹配前一个字符最多0次
# ma = re.match(r'[a-z][\d]*?', 'a1')

# "+?" 匹配前一个字符最多1次
# ma = re.match(r'[\w][\d]+?', 'a25')

# "??" 匹配前一个字符最多0次
# ma = re.match(r'[\w][\d]??', 'a4')


#  ************使用正则表达式进行边界匹配*******************

# "^" 匹配字符串的开头
# "$" 匹配字符串的结尾
# ma = re.match(r'^[\d]{1,10}@qq.com$', '1052045838@qq.com')

# "\A" 指定的字符串必须出现在开头
# "\Z" 指定的字符串必须出现在结尾


# "|" 匹配左右任意一个表达式

# ma = re.match(r'[1-9]?[\d]$|100', '100')  # 匹配1-100间的任意字符

# "(ab)" 括号中的表达式作为一个分组
# ma = re.match(r'[\w]{4,6}@(163|126|qq).com', '102345@qq.com')

# "\<number>"应用编号为number的分组匹配到的字符串
ma = re.match(r'<([\w]+>)[\w]+</\1', '<book>python</book>')
print ma.groups()


if ma != None:
    print ma.group()
else:
    print "匹配失败"
