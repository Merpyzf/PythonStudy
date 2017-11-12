# coding:utf-8
import os
import xlrd
from datetime import date, datetime

if __name__ == '__main__':
    # 获取当前脚本所在的路径
    curr_path = os.getcwd()
    excel_path = curr_path + '/data/' + 'students.xlsx'

    workbook = xlrd.open_workbook(excel_path)

    sheet1 = workbook.sheet_by_index(0)

    print sheet1.name, sheet1.ncols, sheet1.nrows

    for t in xrange(1, sheet1.nrows):
        for x in xrange(0, sheet1.ncols):
            # 对应单元格中不同数据类型 ctype :  0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
            ctype = sheet1.cell(t, x).ctype
            cell_value = sheet1.cell(t, x).value
            # 表示数字类型
            if ctype == 2:
                print int(cell_value)
            # 表示日期类型
            elif ctype == 3:
                date_value = xlrd.xldate_as_tuple(cell_value, workbook.datemode)
                str_data = date(*date_value[:3]).strftime('%Y/%m/%d')
                print str_data
            else:
                print cell_value
