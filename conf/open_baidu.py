import os,time
from selenium import webdriver
from conf.config_utils import config

driver_path = os.path.join(os.path.dirname(__file__),'../driver/chromedriver.exe')
driver = webdriver.Chrome(executable_path=driver_path)
driver.maximize_window()
driver.get(config.get_baidu_url())
time.sleep(5)
driver.close()