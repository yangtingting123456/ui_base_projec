import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest,os

driver_path = os.path.join(os.path.dirname(__file__),'../driver/chromedriver.exe')

class BaiDu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get('https://www.baidu.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

    # @unittest.skipUnless(False,'条件为假跳过')
    def test_search_cat(self):
        self.driver.find_element(By.ID, 'kw').send_keys('猫')
        self.driver.find_element(By.ID, 'su').click()
        title=  self.driver.title
        self.assert_(title,'猫_百度搜索')

    # @unittest.skip('无条件跳过')
    def test_search_dog(self):
        self.driver.find_element(By.ID, 'kw').send_keys('狗')
        self.driver.find_element(By.ID, 'su').click()
        title=  self.driver.title
        self.assert_(title,'狗_百度搜索')

    # @unittest.skipIf(True,'条件为真的时候跳过')
    def test_search_rabbit(self):
        self.driver.find_element(By.ID, 'kw').send_keys('兔子')
        self.driver.find_element(By.ID, 'su').click()
        title = self.driver.title
        self.assert_(title, '兔子_百度搜索')

    # @unittest.expectedFailure  #预期失败
    def test_search_panda(self):
        self.driver.find_element(By.ID, 'kw').send_keys('熊猫')
        self.driver.find_element(By.ID, 'su').click()
        title = self.driver.title
        self.assert_(title, '小猪_百度搜索')




