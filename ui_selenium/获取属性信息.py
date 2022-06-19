from selenium import  webdriver
driver = webdriver.Chrome(executable_path='E:\chromedriver_win32\chromedriver.exe')
driver.get('http://www.baidu.com')

driver.maximize_window()
input_text = driver.find_element_by_id("kw")

print('1',input_text.size)
print('',input_text.get_attribute())
# print('',input_text.is_displayed())
# print('',input_text.is_enabled())
# print('',input_text.is_selected())