# coding:utf-8
import MySQLdb
import xlrd


def read_excel_content():
    """
    读取excel文件中的内容
    """
    levels = {'容易': 1, "中等": 2, "困难": 3};
    types = {'单选题': 1, '多选题': 2, '真假题': 3};
    db = MySQLdb.connect("127.0.0.1", "root", "wangke0310", "exam", charset="utf8")
    cursor = db.cursor()

    excel1 = "D:\PythonCode\PythonStudy\demo\data\excel8.xls"
    workbook = xlrd.open_workbook(excel1)
    ques_sheet = workbook.sheet_by_index(1)
    # workbook.get_sheets()
    
    for r in xrange(1, ques_sheet.nrows):

        # 题目的难易程度
        level = (ques_sheet.cell(r, 3).value).encode('utf-8')

        if level != "":
            if level == '很容易':
                level = '容易'
            elif level == '简单':
                level = '容易'
            elif level == '很难':
                level = '困难'
            elif level == '难':
                level = "困难"
            elif level == '中':
                level = "中等"

            # 部门
            department = (ques_sheet.cell(r, 1).value).encode('utf-8')
            # 作者
            author = (ques_sheet.cell(r, 4).value).encode('utf-8')
            # 试题类型
            exam_type = (ques_sheet.cell(r, 5).value).encode('utf-8')
            # 题干
            question = (ques_sheet.cell(r, 6).value).encode('utf-8')

            options = [];
            for x in range(9, 13):
                options.append(ques_sheet.cell(r, x).value)

            cursor.execute("select *from department where name = '%s' " % (department))
            results_d = cursor.fetchall()
            if len(results_d) == 0:
                print "插入部门-->", department
                cursor.execute("insert into department (name) VALUES ('%s')" % (department));
                db.commit()
            cursor.execute("select *from department where name = '%s' " % (department))
            results_d = cursor.fetchall()
            if not len(results_d) == 1:
                print "可能出错请注意！"
            # 部门id
            department_id = results_d[0][0]

            #
            if exam_type == '单选题':
                right_answer = (ques_sheet.cell(r, 14).value).encode('utf-8')
                print exam_type, level

                int_type = types[exam_type]
                int_level = levels[level]

                add_sql = "insert into exam (author, question, rightAnswer, type_id, department_id,level_id) VALUES ('%s','%s','%s', %d,%d,%d)" % (
                    author, question, right_answer, int_type, department_id, int_level)
                print "addsql:", add_sql
                cursor.execute(add_sql)
                db.commit()
                # 读取已插入题干的id

                get_exam_id_sql = "select *from exam where question = '%s'" % (question)
                cursor.execute(get_exam_id_sql)
                results = cursor.fetchall()
                # 题干id
                exam_id = results[0][0]

                print exam_id, "个数->" + str(len(results))

                index = 0;
                for option in options:
                    add_option_sql = "insert into exam_option (exam_id,option_id,option_content) VALUES (%d,%d, '%s')" % (
                        exam_id, index, option
                    )
                    index += 1;
                    cursor.execute(add_option_sql)
                    db.commit()



            elif exam_type == '真假题':
                right_answer = (ques_sheet.cell(r, 14).value).encode('utf-8')
                if (right_answer == "是"):
                    right_answer = 1
                elif (right_answer == '否'):
                    right_answer = 0

                add_sql = "insert into exam (author, question, rightAnswer, type_id, department_id,level_id) VALUES ('%s','%s','%s', %d,%d,%d)" % (
                    author, question, str(right_answer), types[exam_type], department_id, levels[level])

                cursor.execute(add_sql)
                db.commit()


# 先将试题难度表和部门插入到外键惯量的表中


if __name__ == "__main__":
    read_excel_content()
# read_excel_content()

# 插入语句 insert into user(name, pwd)VALUES ('wangke', 'wangke0310')
# 查询语句
