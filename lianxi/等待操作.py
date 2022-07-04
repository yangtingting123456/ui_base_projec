# -- coding: utf-8 --
# @Time : 2022/7/1 9:14
# @Author : siyu.yang
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
# 为了保证脚本的稳定性，有时候需要引入等待时间，等待页面加载元素后进行操作，selenium
# 提供了三种等待时候设置。
# 1.sleep():固定休眠时间设置，pyhton的time包里提供了休眠方法sleep，
# 导入包后就能使用；
# sleep()方法以秒为单位，如果超过设置小于1秒，可以使用小数
import time
time.sleep(0.5)

# 2.implicitylyWait():implicitlyWait()方法比sleep()方法智能，sleep()方法只能
# 在一个固定的时间等待，而implicitlyWait()可以在一个时间范围内等待，称为隐式等待
driver.implicityl_wait(100)
element = driver.find_element(By.CSS_SELECTOR,'div.red_box')
# 备注：设置等待100s，页面上的元素怒5s后出现，只等待5s。不会等待100秒

# 3.WebDriverWait():显示等待，语法格式如下：
# WebDriverWait(driver,timeout,poll_frequency=0.5,ignore_exceptions=None)
# driver:WebDriverWait的驱动程序（IE，火狐，谷歌或远程）
# timeout：最长等待时间，默认以秒为党委
# poll_frequency:休眠时间的间隔（步长）时间，默认为0.5秒（即每500毫秒扫描一次页面）
# ignore_exceptions:超时后的异常信息，默认情况下抛出NoSuchElementException 异常
# 举例：
from selenium.webdriver.support.ui import WebDriverWait

# 引入WebDriverWait类
element = WebDriverWait(driver,3).until(lambda x:x.find_element_by_css_selector("div.red_box"))



