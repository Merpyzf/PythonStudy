# -*- coding:utf-8 -*-
import xlrd
import xlwt

"""
学习Excel文件的写入  
官方文档--> http://xlwt.readthedocs.io/en/latest/development.html
CSDN --> http://blog.csdn.net/Tulaimes/article/details/71172778
"""

if __name__ == "__main__":
    # 创建工作簿
    wbk = xlwt.Workbook('utf-8')
    # 创建工作表
    sheet1 = wbk.add_sheet('Sheet1', cell_overwrite_ok=True)

    font = xlwt.Font()

    # 设置单元格中标题文字的显示样式
    style_title = xlwt.easyxf('font:height 420;')  # 36pt,类型小初的字号
    alignment_title = xlwt.Alignment()  # Create Alignment
    alignment_title.horz = xlwt.Alignment.HORZ_CENTER  # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
    style_title.alignment = alignment_title
    # 设置第二列和第四列的宽度

    # 设置单元格的宽度
    for i in xrange(0, 6):
        print i
        if i % 2 == 0:
            sheet1.col(i).width = 256 * 15
        else:
            sheet1.col(i).width = 256 * 20
    # 标题
    sheet1.write_merge(0, 0, 0, 4, '名佳英语学员信息表', style_title)

    # 设置正文文本再单元格中的显示样式
    style_content = xlwt.easyxf('font:height 280;')
    alignment_content = xlwt.Alignment()
    alignment_content.horz = xlwt.Alignment.WRAP_AT_RIGHT
    style_content.alignment = alignment_content


    borders = xlwt.Borders()
    borders.top = xlwt.Borders.DOUBLE
    borders.top_colour = 0x40

    style_border = xlwt.XFStyle()
    style_border.borders = borders


    startLine = 3


    for i in xrange(0, 5):
        sheet1.write(startLine+1, i, "", style_border)

    sheet1.write(startLine+2, 0, '打印时间:', style_content)

    sheet1.write(startLine+2, 1, '2017/10/20 11:54', style_content)

    sheet1.write(startLine+4, 0, '学号:', style_content)

    sheet1.write(startLine+4, 1, '20', style_content)

    sheet1.write(startLine+4, 2, '姓名:', style_content)

    sheet1.write(startLine+4, 3, '王珂', style_content)

    sheet1.write(startLine+6, 0, '性别:', style_content)

    sheet1.write(startLine+6, 1, '男', style_content)

    sheet1.write(startLine+6, 2, '学校:', style_content)

    sheet1.write(startLine+6, 3, '育才小学', style_content)

    sheet1.write(startLine+8, 0, '入校时间:', style_content)

    sheet1.write(startLine+8, 1, '2015/9/1', style_content)

    sheet1.write(startLine+8, 2, '年级:', style_content)
    sheet1.write(startLine+8, 3, '3', style_content)

    sheet1.write(startLine+10, 0, '班级:', style_content)

    sheet1.write(startLine+10, 1, '5', style_content)

    sheet1.write(startLine+10, 2, '联系电话:', style_content)

    sheet1.write(startLine+10, 3, '17714574929', style_content)

    sheet1.write(startLine+12, 0, '备注:', style_content)

    sheet1.write(startLine+12, 1, '这是一个备注信息', style_content)


    for i in xrange(0, 5):
        sheet1.write(startLine+14, i, "", style_border)

    sheet1.write(startLine+17, 0, '所在班次:', style_content)
    sheet1.write(startLine+17, 1, '老罗新概念:', style_content)

    sheet1.write(startLine+19, 0, '任课教师:', style_content)
    sheet1.write(startLine+19, 1, '罗永浩', style_content)

    sheet1.write(startLine+21, 0, '教师电话:', style_content)
    sheet1.write(startLine+21, 1, '17714574929', style_content)

    sheet1.write(startLine+23, 0, '上课地点:', style_content)
    sheet1.write(startLine+23, 1, '1号教室 - 文昌阁校区', style_content)

    sheet1.write(startLine+25, 0, '班次时间:', style_content)
    sheet1.write(startLine+25, 1, '周六17:00', style_content)

    sheet1.write(startLine+27, 0, '报名时间:', style_content)
    sheet1.write(startLine+27, 1, '2017-10-4', style_content)

    sheet1.write(startLine+29, 0, '班次备注:', style_content)
    sheet1.write(startLine+29, 1, '这是一个备注信息', style_content)

    wbk.save('test2.xls')
