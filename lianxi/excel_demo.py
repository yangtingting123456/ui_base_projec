import os,xlrd,xlwt
excel_path = os.path.join(os.path.abspath(__file__),'../data/zentao_login_cookies.xlsx')
#读取excel
workbook = xlrd.open_workbook(excel_path)
sheet = workbook.sheet_by_name('zentao_cookies')
print('获取总行数：',sheet.nrows)
print('获取总列数：',sheet.ncols)
print('某一行的数据：',sheet.row(1))
print('具体单元格内容：',sheet.cell_value(0,0))
print('单元格数据类型：',sheet.cell_type(2,3))
#0 empty  , 1 string   ,2 number, 3 data  ,4 boolean  ,5 error

# 写入excel
work_book = xlwt.Workbook(encoding='utf-8')
work_sheet = work_book.add_sheet('student_info')
work_sheet.write(0,0,'学号')
work_book.save(excel_path)
