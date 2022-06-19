import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='E:\chromedriver_win32\chromedriver.exe')
driver.get('file:///C:/Users/ytt/Desktop/p14%E7%8F%AD%E8%AF%BE%E7%A8%8B%E5%AD%A6%E4%B9%A0%E8%B5%84%E6%96%99/element_samples.html')
#定位一组元素
# checkbooks = driver.find_elements(By.CSS_SELECTOR,'input[type = "checkbox"]')
# for i in checkbooks:
#     i.click()
#层级定位
ck = driver.find_element(By.CSS_SELECTOR,'div#checkbox').find_elements(By.CSS_SELECTOR,'input[type = "checkbox"]')
for i in ck:
    i.click()
time.sleep(3)