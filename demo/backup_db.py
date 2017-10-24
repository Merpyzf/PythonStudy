# coding:utf-8
# 备份数据库，并使用邮箱定时发送备份的数据
# 数据库备份命令
# mysqldump -uroot -pwangke0310 mingjia > /root/backup/mingjia_backup.sql
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

    str_cmd = 'mysqldump -u' + username + ' -p' + password + " "+db_name + ' > ' + backup_path + '/mingjia_backup.sql'
    # 转储sql
    os.system(str_cmd)

    # 将sql脚本的路径返回
    return backup_path + '/mingjia_backup.sql'


def sendEmail():
    subject = '2017-10-24日数据库数据备份'
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


if __name__ == "__main__":
    # 数据库备份
    sendEmail()
