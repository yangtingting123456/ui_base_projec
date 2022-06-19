import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path='E:\chromedriver_win32\chromedriver.exe')
driver.get('file:///C:/Users/ytt/Desktop/p14%E7%8F%AD%E8%AF%BE%E7%A8%8B%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/element_samples.html')
#下拉框操作
#1.直接定位
driver.find_element(By.CSS_SELECTOR,'option[value="mango"]').click()
#2.共通过select对象获取
selects = driver.find_element(By.CSS_SELECTOR,'select[id="Selector"]')
s = Select(selects)
#通过索引
s.select_by_index(4)
time.sleep(2)
#通过value
s.select_by_value('orange')
time.sleep(2)
#通过文本
s.select_by_visible_text('香蕉')
time.sleep(3)
driver.quit()