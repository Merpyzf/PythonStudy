# coding:utf-8
import xlrd
import xlwt
from xlwt import Pattern


def countNum():
    category = {}
    categoryNum = {
        u'单选题-容易': 20,
        u'单选题-中等': 15,
        u'单选题-困难': 15,

        u'多选题-容易': 12,
        u'多选题-中等': 9,
        u'多选题-困难': 9,

        u'真假题-容易': 8,
        u'真假题-中等': 6,
        u'真假题-困难': 6,

    }
    result = {}
    work_book = xlrd.open_workbook('../data/rubrics.xls')
    sheet = work_book.sheet_by_index(0)
    for row in range(3, sheet.nrows):
        # 科目
        subject = sheet.cell(row, 3).value
        # 题目类型
        type = sheet.cell(row, 2).value
        # 难度
        level = sheet.cell(row, 4).value
        rubric_type = subject + '-' + type + '-' + level;
        if category.has_key(rubric_type):
            num = category.get(rubric_type)
            num = num + 1;
            category.update({rubric_type: num})
        else:
            category[rubric_type] = 1

    for k in category:
        # print k + ' : ' + str(category[k])
        for j in categoryNum:
            if j in k:
                need = categoryNum[j] - category[k];
                if need <= 0:
                    need = 0
                result[k] = str(category[k]) + '|' + str(need) + '|' + str(categoryNum[j])

    # 科目
    subjects = (u'鉴定',
                u'性能鉴定',
                u'综合业务部',
                u'制样',
                u'化验',
                u'煤炭检测',
                u'水尺计重',
                u'煤炭采样',
                u'采样'
                )

    types = (u'单选题',
             u'多选题',
             u'真假题',
             )

    levels = (u'容易',
              u'中等',
              u'困难'
              )

    work_book = xlwt.Workbook(encoding='ascii')
    work_sheet = work_book.add_sheet('sheet1')
    style = xlwt.XFStyle()
    pattern = Pattern()  # 创建一个模式
    pattern.pattern = Pattern.SOLID_PATTERN  # 设置其模式为实型
    pattern.pattern_fore_colour = 5
    # 设置单元格背景颜色 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta,  the list goes on...
    style.pattern = pattern
    work_sheet.write(0, 0, label=u'试题类型')
    work_sheet.write(0, 1, label=u'当前题库中存在的试题个数')
    work_sheet.write(0, 2, label=u'总共需要的试题个数')
    work_sheet.write(0, 3, label=u'需要补充的试题个数')
    index = 1
    total = 0;
    for subject in subjects:
        for type in types:
            for level in levels:
                stl = subject + '-' + type + '-' + level
                if result.has_key(stl):
                    print "*********"
                    print stl
                    print result.get(stl)
                    data = (result.get(stl)).split('|')

                    work_sheet.write(index, 0, stl)
                    total = total+int(data[0])
                    work_sheet.write(index, 1, data[0])
                    work_sheet.write(index, 2, data[2])
                    work_sheet.write(index, 3, data[1])
                    index = index + 1

                else:
                    for j in categoryNum:
                        if j in stl:
                            for q in categoryNum:
                                if q in j:
                                    print stl
                                    print categoryNum[q]
                                    print '不存在'
                                    work_sheet.write(index, 0, label=stl)
                                    work_sheet.write(index, 1, label=0)
                                    work_sheet.write(index, 2, label=categoryNum[q])
                                    work_sheet.write(index, 3, label=categoryNum[q])
                                    index = index + 1

    work_book.save('out.xls')
    print total


if __name__ == '__main__':
    countNum()
