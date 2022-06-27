# 2022-6-22日作业
# 1、完成ini配置文件和日志文件的使用预习
# 2、完成禅道提交bug的脚本(要有附件)
import os,time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver_path = os.path.join(os.path.abspath(__file__),'../../../driver/chromedriver.exe')
print(driver_path)
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login ')
driver.maximize_window()
driver.implicitly_wait(30)
#1 登录
driver.find_element(By.CSS_SELECTOR,'input[type="text"]').send_keys("test01")
driver.find_element(By.CSS_SELECTOR,'input[type="password"]').send_keys("newdream123")
driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
#2 进入测试-bug-提bug模块
driver.find_element(By.LINK_TEXT,'测试').click()
driver.find_element(By.CSS_SELECTOR,'li[data-id="bug"]').click()
driver.find_element(By.LINK_TEXT,'提Bug').click()
#3 输入bug信息
#3.2 选择项目
bug_text = driver.find_element(By.CSS_SELECTOR,'iframe.ke-edit-iframe')
driver.switch_to.frame(bug_text)
driver.find_element(By.ID,'div#product_chosen').click()

time.sleep(30)
driver.quit()