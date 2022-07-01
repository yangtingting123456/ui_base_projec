# -- coding: utf-8 --
# @Time : 2022/7/1 9:13
# @Author : siyu.yang
# 定位到元素后，需要对元素进行曹祖，常见的有鼠标点击、键盘操作等
# 这取决于我们定位到的对象支撑那些操作。一般来说，所有与页面交互的
# 的操作都是通过WebElement接口
import os,time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver_path = os.path.join(os.path.dirname(__file__),'../driver/chromedriver.exe')
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com')
driver.set_window_size(1920,1080)
driver.implicitly_wait(30)
# webdriver 中常用的操作元素的方法有如下几个：
# clear() 清除对象的内容     send_keys()在对象上模拟按键输入
kw = driver.find_element(By.ID,'kw')
kw.send_keys('webdriver 常用api操作')
time.sleep(1)
kw.clear()
# click() 单机对象，强调对象的独立性
driver.find_element(By.LINK_TEXT,'更多').click()
# submit() : 提交表单，要求对象必须是表单
driver.find_element(By.ID,'form').submit()
kw = driver.find_element(By.CSS_SELECTOR,'input#su')
print('返回对象的尺寸：',kw.size)
print('获取对象文本：',kw.text)
print('获取对象属性值：',kw.get_attribute('class'))
print('判断对象是否可见：',kw.is_displayed())
print('判断读写是否被禁用：',kw.is_enabled())
print('判断对象是被选中：',kw.is_selected())
print('获取对象标签名：',kw.tag_name)
print('获取对象标签名称：',kw.location)
print('获取元素坐标：',kw.location)





time.sleep(10)
driver.close()
driver.quit()



