from selenium import webdriver
from selenium.webdriver.common.by import By
import os,time,xlwt,xlrd
driver_path = os.path.join(os.path.abspath(__file__),'../../driver/chromedriver.exe')
print(driver_path)
driver = webdriver.Chrome(executable_path = driver_path)
driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
driver.find_element(By.ID,'account').send_keys('test01')
driver.find_element(By.NAME,'password').send_keys('newdream123')
driver.find_element(By.ID,'submit').click()
cookies = driver.get_cookies()
for cookie in cookies:
    print(cookie)
# 1.写入cookies 到表格中
excel_path = os.path.join(os.path.abspath(__file__),'../data/zentao_login_cookies.xlsx')
# workbook = xlwt.Workbook(encoding='utf-8')
# worksheet = workbook.add_sheet('cookies')
# for i in range(1,len(cookies)+1):
#     worksheet.write(i,0,cookies[i-1]['domain'])
#     worksheet.write(i, 1, cookies[i - 1]['name'])
#     worksheet.write(i,2, cookies[i - 1]['path'])
#     worksheet.write(i, 3, cookies[i - 1]['value'])
# workbook.save(excel_path)

# 2.读取cookies
work_book = xlrd.open_workbook(excel_path)
work_sheet = work_book.sheet_by_name('cookies')


for row_num in range(len(1,work_sheet.nrows)):
    cookie_dict = {}
    cookie_dict['domain'] = work_sheet.cell_value(row_num,0)
    cookie_dict['name'] = work_sheet.cell_value(row_num, 1)
    cookie_dict['path'] = work_sheet.cell_value(row_num,2)
    cookie_dict['value'] = work_sheet.cell_value(row_num,3)
    driver.add_cookie(cookie_dict)

driver.refresh()
time.sleep(5)
driver.quit()
