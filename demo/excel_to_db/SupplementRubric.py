#!/usr/bin/env python
# encoding: utf-8
import xlrd
import MySQLdb

"""
@version: 1.0
@author: wangke
@contact: merpyzf@qq.com
@software: PyCharm
@file: SupplementRubric.py
@time: 2018/6/21 19:35
"""




if __name__ == '__main__':
    work_book = xlrd.open_workbook('out.xls')
    work_sheet = work_book.sheet_by_index(0)


