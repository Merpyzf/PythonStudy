#!/usr/bin/env python
# encoding: utf-8
import xlrd
import MySQLdb
import MySQLdb
import chardet

"""
@version: 1.0
@author: wangke
@contact: merpyzf@qq.com
@software: PyCharm
@file: SupplementRubric.py
@time: 2018/6/21 19:35
"""


def conn_db():
    db = MySQLdb.connect('127.0.0.1', 'root', 'wangke0310', 'qdm168138350_db', charset='utf8')
    return db


# 获取需要补充的试题类型
def get_need_add_rubric():
    work_book = xlrd.open_workbook('out.xls')
    work_sheet = work_book.sheet_by_index(1)

    need_support = [];
    # count = 0
    for row_index in range(1, work_sheet.nrows):
        split = ((work_sheet.cell(row_index, 0).value).encode('utf-8')).split('-')
        subject = split[0]
        type = split[1]
        level = split[2]
        supplement_rubric_num = work_sheet.cell(row_index, 3).value
        if int(supplement_rubric_num) > 0:
            need_support.append(
                {'subject': subject, 'type': type, 'level': level, 'supplement_rubric_num': supplement_rubric_num})

    return need_support


# 获取试题所有的难度等级
def get_rubric_leve():
    cursor = db.cursor()
    cursor.execute('select *from ex_level')
    db.commit()
    levels = {}
    for item in cursor.fetchall():
        levels[item[1]] = item[0]
    return levels


# 获取试题的科目类型
def get_rubric_subject():
    cursor = db.cursor()
    cursor.execute('select *from ex_rubric_subject')
    db.commit()
    subjects = {}
    for item in cursor.fetchall():
        subjects[item[1]] = item[0]
    return subjects


def get_rubric_type():
    cursor = db.cursor()
    cursor.execute('select *from ex_rubric_type')
    db.commit()
    types = {}
    for item in cursor.fetchall():
        types[item[1]] = item[0]
    return types


# 向数据库写入模拟的试题
def write_simulate_rubric(db, rubrics_num):
    levels = get_rubric_leve()
    subjects = get_rubric_subject()
    types = get_rubric_type()

    for rubricInfo in rubrics_num:
        subject_name = rubricInfo.get('subject')
        type_name = rubricInfo.get('type')
        level_name = rubricInfo.get('level')

        supplement_rubric_num = rubricInfo['supplement_rubric_num']
        subject_id = subjects.get(subject_name.decode('utf-8'))
        type_id = types.get(type_name.decode('utf-8'))
        level_id = levels.get(level_name.decode('utf-8'))
        cursor = db.cursor()

        for i in xrange(int(supplement_rubric_num)):
            question = "这是一道用于补充题库不足的测试样题[%s - %s - %s]" % (subject_name, type_name, level_name)
            answer = ''
            if subject_id == 3:
                answer = '真'
            elif subject_id == 1:
                answer = 'A'
            elif subject_id == 2:
                answer = 'AB'

            add_choice_sql = "insert into ex_rubric (author, question, rightAnswer, rubric_type_id, rubric_subject_id,rubric_level_id) " \
                             "VALUES ('%s', '%s', '%s',%d,%d,%d)" % (
                                 'merpyzf', question, answer, type_id, subject_id, level_id);
            cursor.execute(add_choice_sql)
            rubric_id = db.insert_id()
            db.commit()

            if not subject_id == 3:
                for option_id in xrange(4):
                    add_option_sql = "insert into ex_option (rubric_id,option_id,option_content) VALUES (%d,%d, '%s')" % (
                        rubric_id, option_id, "这是一条测试样题的选项")
                    cursor.execute(add_option_sql)
                    db.commit()


if __name__ == '__main__':
    db = conn_db()
    rubrics_num = get_need_add_rubric()
    print rubrics_num
    write_simulate_rubric(db, rubrics_num)
