# coding:utf-8
# 备份数据库，并使用邮箱定时发送备份的数据
# 数据库备份命令
# mysqldump -uroot -pwangke0310 mingjia > /root/backup/mingjia_backup.sql
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import MySQLdb
import time
import datetime

import os


def backup_db(username, password, db_name):
    """
    数据库备份，将数据库转储为sql脚本
    :param uname:
    :param pwd:
    :param db_name:
    :return:
    """
    # 在当前项目下创建存储备份文件的文件夹
    curr_path = os.getcwd()
    backup_path = curr_path + '/back_up'
    if not os.path.exists(backup_path):
        os.mkdir(backup_path)

    str_cmd = 'mysqldump -u' + username + ' -p' + password + " " + db_name + ' > ' + backup_path + '/mingjia_backup.sql'
    # 转储sql
    os.system(str_cmd)

    # 将sql脚本的路径返回
    return backup_path + '/mingjia_backup.sql'


def sendEmail():
    curr_date = datetime.datetime.now().strftime('%Y-%m-%d')
    subject = curr_date + '日名佳英语数据库数据备份'
    smtpserver = 'smtp.qq.com'

    user = '1052060838@qq.com'
    pwd = 'ubcgouydtoznbeag'
    # 接受者的邮箱地址
    receiver = '1052060838@qq.com'

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = user
    msg['To'] = receiver

    part = MIMEText(subject)
    msg.attach(part)

    # 附件部分
    sql_path = backup_db('root', 'wangke0310', 'mingjia')

    part = MIMEApplication(open(sql_path, 'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="mingjia_backup.sql")
    msg.attach(part)
    s = smtplib.SMTP_SSL(smtpserver, timeout=30)  # 连接smtp邮件服务器,端口默认是25
    s.login(user, pwd)  # 登陆服务器
    s.sendmail(user, receiver, msg.as_string())  # 发送邮件
    s.close()


def update_stu_grade():
    """
    更新学生年级
    :return:
    """

    conn = MySQLdb.Connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        passwd='wangke0310',
        db='mingjia',
        charset='utf8'
    )

    cursor = conn.cursor()

    sql_all_students = 'select *from student'

    cursor.execute(sql_all_students)

    rs_students = cursor.fetchall()

    for stu in rs_students:
        # 学号
        stu_id = stu[0]
        stu_entrance_date = stu[4]
        temp_class = calculate_grade(stu_entrance_date)
        # 如果入学时间填写不为空，则去更新学生的信息
        if stu_entrance_date != None:
            sql_update_stu = 'update student set temp_class = ' + str(temp_class) + ' where id = ' + str(stu_id)
            cursor.execute(sql_update_stu)


def calculate_grade(entrance_time):
    """
    根据入学时间计算所在年级
    :param entrance_time:
    :return:
    """
    if entrance_time != None:
        # 获取当前的日期
        todaty = datetime.date.today()
        curr_year = todaty.year
        curr_month = todaty.month
        curr_day = todaty.day
        # 获取入学日期
        year = entrance_time.year
        month = entrance_time.month
        day = entrance_time.day

        # 年级
        grade = curr_year - year
        if month > curr_month:
            pass
        elif month < curr_month:
            grade += 1
        elif curr_month == month:
            if day <= curr_day:
                grade += 1
            elif day > curr_day:
                pass

    return grade


if __name__ == "__main__":
    while True:
        current_time = time.localtime(time.time())
        # 早上八点钟进行登录
        if ((current_time.tm_hour == 11) and (current_time.tm_min == 0) and (current_time.tm_sec == 0)):
            update_stu_grade()
            # 数据库备份
            sendEmail()
