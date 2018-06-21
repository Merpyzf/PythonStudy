# coding:utf-8
import MySQLdb
import xlrd
import xlwt
import os
import chardet

souce_file_dir = 'D:\\first';
dest_file_dir = ''
# 试题难度

choice = {u'是': 1, u'否': 0}
rubric_list = [];
total = 0;
fill_rubric_num = 0;
incomplete_rubric_num = 0;


def read_excel_content(excelPath):
    global total, fill_rubric_num, incomplete_rubric_num
    work_book = xlrd.open_workbook(excelPath)
    for sheet_name in work_book.sheet_names():
        sheet_work_book = work_book.sheet_by_name(sheet_name=sheet_name)
        for row in xrange(1, sheet_work_book.nrows):
            subject = (sheet_work_book.cell(row, 0).value).strip()
            level = (sheet_work_book.cell(row, 1).value).strip()
            author = (sheet_work_book.cell(row, 2).value).strip()
            type = (sheet_work_book.cell(row, 3).value).strip()
            question = (sheet_work_book.cell(row, 4).value).strip()
            A = sheet_work_book.cell(row, 5).value
            B = sheet_work_book.cell(row, 6).value
            C = sheet_work_book.cell(row, 7).value
            D = sheet_work_book.cell(row, 8).value
            E = sheet_work_book.cell(row, 9).value
            answer = sheet_work_book.cell(row, 10).value
            total = total + 1
            if subject == '' or level == '' or type == '' or question == '' or answer == '':
                incomplete_rubric_num = incomplete_rubric_num + 1
                continue
            if type == u'填空题':
                fill_rubric_num = fill_rubric_num + 1
                continue

            if type == u'真假题':
                answer = choice.get(answer)
            if level == u'简单' or level == u'很容易':
                level = u'容易'
            elif level == u'中':
                level = u'中等'
            elif level == u'难' or level == u'很难':
                level = u'困难'

            if subject.startswith(u'煤炭检测'):
                subject = '煤炭检测'

            rubric_list.append({
                'subject': subject,
                'level': level,
                'author': author,
                'type': type,
                'question': question,
                'A': A,
                'B': B,
                'C': C,
                'D': D,
                'E': E,
                'answer': answer
            })


if __name__ == "__main__":
    levels = {u"容易": 1, u"中等": 2, u"困难": 3}
    # 试题类型
    types = {u'单选题': 1, u'多选题': 2, u'真假题': 3}
    rubric_subject = {}
    db = MySQLdb.connect("127.0.0.1", "root", "wangke0310", "qdm168138350_db", charset="utf8")
    cursor = db.cursor()

    sql_get_subjects = "select *from ex_rubric_subject"
    cursor.execute(sql_get_subjects)
    db.commit()
    for subject in cursor.fetchall():
        rubric_subject[subject[1]] = subject[0]

    souce_file_dir = 'D:\\first';
    # 读取所有试题
    for file in os.listdir(souce_file_dir):
        excelPath = os.path.join(souce_file_dir, file)
        read_excel_content(excelPath)
    #
    for rubric in rubric_list:
        choice_list = [];
        subject = rubric['subject']
        level = rubric['level']
        author = rubric['author']
        type = rubric['type']
        question = rubric['question']
        choice_list.append(rubric['A'])
        choice_list.append(rubric['B'])
        choice_list.append(rubric['C'])
        choice_list.append(rubric['D'])
        choice_list.append(rubric['E'])
        answer = rubric['answer']

        print question

        if not rubric_subject.has_key(subject):
            add_subject_sql = "insert into ex_rubric_subject (name) VALUES ('%s')" % (subject)
            cursor.execute(add_subject_sql)
            subject_id = db.insert_id()
            rubric_subject[subject] = subject_id
            db.commit()
        level_id = levels.get(level.strip())
        type_id = types.get(type)
        subject_id = rubric_subject[subject]

        if type == u'真假题':
            add_tf_sql = "insert into ex_rubric (author, question, rightAnswer, rubric_type_id, rubric_subject_id,rubric_level_id) " \
                         "VALUES ('%s', '%s', '%s',%d,%d,%d)" % (
                             author, question, answer, type_id, subject_id, level_id);
            cursor.execute(add_tf_sql)
            db.commit()
        else:
            add_choice_sql = "insert into ex_rubric (author, question, rightAnswer, rubric_type_id, rubric_subject_id,rubric_level_id) " \
                             "VALUES ('%s', '%s', '%s',%d,%d,%d)" % (
                                 author, question, answer, type_id, subject_id, level_id);
            cursor.execute(add_choice_sql)
            rubric_id = db.insert_id();
            db.commit()
            # 插入选项
            option_index = 0
            for choice in choice_list:
                if choice == '':
                    continue
                add_option_sql = "insert into ex_option (rubric_id,option_id,option_content) VALUES (%d,%d, '%s')" % (
                    rubric_id, option_index, choice
                )
                option_index = option_index + 1
                cursor.execute(add_option_sql)
                db.commit()

    print '总共-> ' + str(total) + ' \n填空题-> ' + str(fill_rubric_num) + '\n数据不完整-> ' + str(incomplete_rubric_num)
