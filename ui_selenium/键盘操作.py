import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(executable_path='E:\chromedriver_win32\chromedriver.exe')
driver.get('https://www.baidu.com')
time.sleep(2)
input_text = driver.find_element(By.ID,'kw')
#普通按键输入
# ActionChains(driver).send_keys('abcd').perform()
# time.sleep(2)
# ActionChains(driver).send_keys(Keys.TAB).perform()
# time.sleep(2)
# ActionChains(driver).send_keys(Keys.TAB).perform()
# time.sleep(2)
# ActionChains(driver).send_keys(Keys.TAB).perform()
#组合键输入
input_text.send_keys('abcdef')
time.sleep(2)
ActionChains(driver).key_down(Keys.CONTROL).send_keys('s').key_up(Keys.CONTROL).perform()
time.sleep(2)
ActionChains(driver).key_down(Keys.CONTROL).send_keys('x').key_up(Keys.CONTROL).perform()
time.sleep(2)
ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
time.sleep(7)

driver.close()


