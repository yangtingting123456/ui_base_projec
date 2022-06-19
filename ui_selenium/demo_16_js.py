import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome(executable_path='E:\chromedriver_win32\chromedriver.exe')
# driver.get('https://www.baidu.com')
#弹框
# driver.execute_script('alert("测试alert弹框")')
# time.sleep(3)
# 2.添加边框
# input_text = driver.find_element(By.ID,'kw')
# driver.execute_script('arguments[0].style.border = "5px dashed red"',input_text)
#3.控制滚动条
driver.get('https://www.baidu.com')
but = driver.find_element(By.ID,"su")
# driver.execute_script('document.documentElement.scrollTop=10000')
#移除属性
js = 'arguments[0].removeAttribute("value")'
driver.execute_script(js)
#修改属性
js = 'arguments[0].setAttribute("value","学习测试")'
driver.execute_script(js,but)