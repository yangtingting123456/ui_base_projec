# -- coding: utf-8 --
# @Time : 2022/6/20 11:35
from selenium import webdriver
import time,os
from homework.homework_20220619.handle_excel import HandleExcel

excel_path = os.path.join(os.path.abspath(__file__), "../data/zentao_login_cookies.xlsx")
cl = HandleExcel(file_name=excel_path,sheet_name='zentao_cookies')

driver_path = os.path.join(os.path.abspath(__file__),'../../../driver/chromedriver.exe')
print(driver_path)
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login ')
#将登录之后的cookis添加进来
# driver.find_element(By.CSS_SELECTOR,'input[type="text"]').send_keys("test01")
# driver.find_element(By.CSS_SELECTOR,'input[type="password"]').send_keys("newdream123")
# driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()

for i in cl.get_excel_test_case():
    driver.add_cookie(i)
time.sleep(3)
driver.refresh()