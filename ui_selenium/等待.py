import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome(executable_path='E:\\chromedriver_win32\\chromedriver.exe')
driver.get('C:\\Users\\ytt\\Desktop\\wait.html')
driver.maximize_window()
from selenium.webdriver.support.ui import WebDriverWait #引入WebDriverWait类
driver.find_element(By.ID,'b').click()
x=WebDriverWait(driver,6).until(lambda d:d.find_element(By.CSS_SELECTOR,"div.red_box"))

#1.固定等待
# time.sleep(3)
#2隐形等待
# driver.implicitly_wait(10)
#3.显示等待
# driver.find_element(By.ID,'b').click()
# WebDriverWait(driver,3).until(lambda x:x.find_element(By.CLASS_NAME,'red_box'))
driver.quit()