from selenium import webdriver
import os
driver_path = os.path.join(os.path.abspath(__file__),'../../driver/chromedriver.exe')
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com')
#1.通过id定位
driver.find_element_by_id()
#2.通过name定位
driver.find_element_by_name()
#3.通过classname 定位
driver.find_element_by_class_name()
#4.通过 tagname 定位，是最不准的定位，因为一个网上上同一个tag那么重复的可能性很大
driver.find_element_by_class_name()
#5.通过link_text 定位
driver.find_element_by_link_text()
#6.通过partial_link_text 定位
driver.find_element_by_partial_link_text()
#7.通过css定位
driver.find_element_by_css_selector()
#8.通过xpath 定位
driver.find_element_by_xpath()