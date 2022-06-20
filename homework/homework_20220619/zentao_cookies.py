# -- coding: utf-8 --
# @Time : 2022/6/20 11:35
from selenium import webdriver
import time,os
from homework.homework_20220619.excel_uitls import ExcelUtils
ecl_util = ExcelUtils()
driver_path = os.path.join(os.path.abspath(__file__),'../../../driver/chromedriver.exe')
print(driver_path)
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login ')
#将登录之后的cookis添加进来
# driver.find_element(By.CSS_SELECTOR,'input[type="text"]').send_keys("test01")
# driver.find_element(By.CSS_SELECTOR,'input[type="password"]').send_keys("newdream123")
# driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
# print(ecl_util.list_to_change_dic()[0])
for i in range(0, 4):
    driver.add_cookie(ecl_util.list_to_change_dic()[i])

# driver.add_cookie({ "name":"zentaosid","value":"l97vmm6ovptiq8c47s6unb2e31","Domain":"47.107.178.45","path":"/"})
# driver.add_cookie({"name":"theme","value":"default","Domain":"47.107.178.45","path":"/zentao/www/",})
# driver.add_cookie({"name":"device","value":"desktop","Domain":"47.107.178.45","path":"/zentao/www/",})
# driver.add_cookie({"name":"lang","value":"zh-cn","Domain":"47.107.178.45","path":"/zentao/www/"})
time.sleep(3)
driver.refresh()