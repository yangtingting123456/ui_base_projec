# -- coding: utf-8 --
# @Time : 2022/7/1 9:13
# @Author : siyu.yang
# 在实际的web产品测试中，对于鼠标的操作，不单单只有click(),有时候还要用到
# 右击、双击、拖动等操作，这些操作包含在ActionChains 类中。
# context_click() :右击
# double_click()      :双击
# drag_and_drop()      :拖动
# move_to_element()    :鼠标移动到一个元素上
# click_and_hold()     : 按下鼠标左键在一个元素上
# 鼠标右击导包
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


driver_path = os.path.join(os.path.dirname(__file__), '../driver/chromedriver.exe')
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com')
driver.maximize_window()
driver.implicitly_wait(30)
# 鼠标操作
# setting = driver.find_element(By.CSS_SELECTOR, 'span#s-usersetting-top')
# ActionChains(driver).click(setting).release(setting).perform()
# time.sleep(3)
# 在实际的web测试中，需要配合键盘按键来操作，webdriver的keys类提供键盘上所有按键的操作，
# 还可以模拟组合键ctrl+a,ctrl+c/v等
driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys(Keys.TAB)
time.sleep(1)
#利用ActionChains去进行按键操作
ActionChains(driver).send_keys(Keys.TAB).perform()
time.sleep(1)
# 组合键操作：ctrl+cctrl+v
ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
time.sleep(1)
driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys('selenium ui 自动化测试')
ActionChains(driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
time.sleep(1)
ActionChains(driver).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
time.sleep(1)
driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys('444444')
time.sleep(3)
ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
# 备注：
# 1、在使用修饰键的时候需要key_down()和key_up()方法修饰键包含ctrl   alt   shift
# 2、类似alt+F4  ctrl+alt+delete不能使用鼠标键盘事
time.sleep(5)
driver.quit()
