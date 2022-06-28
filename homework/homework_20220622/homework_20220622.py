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
driver.implicitly_wait(10)
#1 登录
driver.find_element(By.CSS_SELECTOR,'input[type="text"]').send_keys("test01")
driver.find_element(By.CSS_SELECTOR,'input[type="password"]').send_keys("newdream123")
driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
#2 进入测试-bug-提bug模块
driver.find_element(By.LINK_TEXT,'测试').click()

#3 输入bug信息
driver.find_element(By.CSS_SELECTOR,'li[data-id="bug"]').click()
driver.find_element(By.LINK_TEXT,'提Bug').click()
#4 选择项目
driver.find_element(By.CSS_SELECTOR,'div#product_chosen').click()
driver.find_elements(By.CSS_SELECTOR,'div.chosen-drop ul.chosen-results li:nth-child(3)')[0].click()
#5 所属模块
time.sleep(1)
driver.find_elements(By.CSS_SELECTOR,'div#moduleIdBox div')[0].click()
driver.find_element(By.CSS_SELECTOR,'ul.chosen-results li:nth-child(7)').click()
#6 所属项目
driver.find_element(By.CSS_SELECTOR,'span#projectIdBox').click()
driver.find_elements(By.CSS_SELECTOR,'div.chosen-drop ul.chosen-results li:nth-child(2)')[2].click()
#影响版本
driver.find_elements(By.CSS_SELECTOR,'ul.chosen-choices')[0].click()
driver.find_elements(By.CSS_SELECTOR,'ul.chosen-results li.active-result')[16].click()


# bug_text = driver.find_element(By.CSS_SELECTOR,'iframe.ke-edit-iframe')
# driver.switch_to.frame(bug_text)
time.sleep(30)
driver.quit()