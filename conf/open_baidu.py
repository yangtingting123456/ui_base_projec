import os, time
from selenium import webdriver
from conf.config_utils import config
from logs.log_utils import logs_obj

driver_path = os.path.join(os.path.dirname(__file__), '../driver/chromedriver.exe')
driver = webdriver.Chrome(executable_path=driver_path)
logs_obj.info('加载浏览器')
driver.maximize_window()
logs_obj.info('浏览器最大化')
try :
    driver.get(config.get_baidu_url())
    logs_obj.info('加载url')
except:
    logs_obj.info('加载url失败')
finally:
    logs_obj.info('捕获异常结束')

time.sleep(5)
logs_obj.info('等待5s')
driver.quit()
logs_obj.info('关闭浏览器')
