# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import re

# BeautifulSoup库使用学习
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title">The Dormouse's story</p>

<p class="story">Once upon a time there were three little sisters; and their names wereand they lived at the bottom of a well.</p>
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;


<p class="story">end……</p>
</html>
"""

if __name__ == '__main__':
    soup = BeautifulSoup(html_doc, "html.parser")
    # 按照标准的缩进结构输出
    # print soup.prettify()
    # for p in soup.find_all('p'):
    # p.string.replace_with('wangke')
    # print unicode(p.string)
    # print type(p.string)
    # print soup.prettify()
    # print soup.head.title

    # all_a = soup.find_all('a')

    # for a in all_a:
    #     print a['class'][0]
    #
    # contents = soup.find_all('html')[0].children
    # print type(soup.find_all('html')[0])
    # print contents
    # print soup.contents


    # 通过tag的.children
    # 生成器, 可以对tag的子节点进行循环:
    # for child in soup.find('html').children:
    #     print child
    #     print '======='



    # for child in soup.find('html').descendants:
    #     print child
    #     print '======='

    # for s in soup.stripped_strings:
    #     print s
    #
    # soup.string

    # print soup.find('title').parent.string

    # tag_a = soup.find('a')
    #
    # next = tag_a.next_sibling.next_sibling

    # print next


    # for tag in soup.find('a').next_siblings:
    #     print tag

    # 找到包含class属性但不包括id属性的标签
    # def has_class_but_no_id(tag):
    #     return tag.has_attr('class') and not tag.has_attr('id')
    #
    #
    # soup.find_all_next()
    #
    # all = soup.find_all(has_class_but_no_id)
    # for x in all:
    #     print x

    # find_all = soup.find_all(class_ ='title')
    #
    # for tag in find_all:
    #     print tag

    select = soup.getText('/', strip=True)
    print select
