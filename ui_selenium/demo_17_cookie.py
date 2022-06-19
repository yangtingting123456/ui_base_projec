import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='E:\chromedriver_win32\chromedriver.exe')
driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login ')
#将登录之后的cookis添加进来
# driver.find_element(By.CSS_SELECTOR,'input[type="text"]').send_keys("test01")
# driver.find_element(By.CSS_SELECTOR,'input[type="password"]').send_keys("newdream123")
# driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
driver.add_cookie({ "name":"zentaosid","value":"l97vmm6ovptiq8c47s6unb2e31","Domain":"47.107.178.45","path":"/"})
driver.add_cookie({"name":"theme","value":"default","Domain":"47.107.178.45","path":"/zentao/www/",})
driver.add_cookie({"name":"device","value":"desktop","Domain":"47.107.178.45","path":"/zentao/www/",})
driver.add_cookie({"name":"lang","value":"zh-cn","Domain":"47.107.178.45","path":"/zentao/www/"})
time.sleep(3)
driver.refresh()