# -*- coding:utf-8 -*-
import xlrd
import xlwt
"""
学习Excel文件的写入  
官方文档--> http://xlwt.readthedocs.io/en/latest/development.html
"""


if __name__ == "__main__":
    wbk = xlwt.Workbook(encoding='utf-8', style_compression=0)
    # 第二个参数用于确认同一个cell单元格是否可以重设值
    sheet = wbk.add_sheet('sheet_1', cell_overwrite_ok=True)
    sheet.write(0,0,'some text')
    style = xlwt.XFStyle()
    font = xlwt.Font();
    font.name = 'Times New Roman'
    font.bold = True
    style.font = font
    sheet.write(0,1, 'some text2 hahaha', style)
    wbk.save('test.xls')




