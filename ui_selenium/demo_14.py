import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='E:\chromedriver_win32\chromedriver.exe')
driver.get('file:///C:/Users/ytt/Desktop/p14%E7%8F%AD%E8%AF%BE%E7%A8%8B%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/element_samples.html')
#alert操作
driver.find_element(By.NAME,'alterbutton').click()
print('文本内存:', driver.switch_to.alert.text)
time.sleep(2)
driver.switch_to.alert.accept()  #确定
# 2. prompt
accept_prompt=driver.find_element(By.NAME,'promptbutton').click()
driver.switch_to.alert.send_keys('自动化输入框')
# time.sleep(3)
driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()