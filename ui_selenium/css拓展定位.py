from selenium import  webdriver
driver = webdriver.Chrome(executable_path='E:\chromedriver_win32\chromedriver.exe')
driver.get('http://www.baidu.com')
# 5.定位后代元素
# 5.1第一个后代元素：first-child
driver.find_element_by_css_selector('div#s-top-left a:first-child').click()