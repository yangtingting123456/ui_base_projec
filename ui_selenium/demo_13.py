import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path='E:\chromedriver_win32\chromedriver.exe')
driver.get('https://graph.qq.com/oauth2.0/show?which=Login&display=pc&response_type=code&state=E71828D9C44F6DB179EB672C7DA8BDB70D987366C4EDD457282578933F5FD0E563CEE789AE21ECBB72C9F9AE450AEECD&client_id=100273020&redirect_uri=https%3A%2F%2Fqq.jd.com%2Fnew%2Fqq%2Fcallback.action%3Fview%3Dnull%26uuid%3Da4e44b4e8cca4508abbe324e7d7deabb')
driver.maximize_window()
#切框架，通过id或name,
# driver.switch_to.frame('ptlogin_iframe')
#没有id，name如何定位那个？
f = driver.find_element(By.CSS_SELECTOR,'iframe[frameborder="0"]')
driver.switch_to.frame(f)
#切出框架
driver.switch_to.default_content()