import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import HTMLTestRunner
import os

driver_path = 'E:\chromedriver_win32\chromedriver.exe'


class BaiDu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.driver.get('https://www.baidu.com')
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def tearDown(self):
        self.driver.quit()

    # @unittest.skipUnless(False,'条件为假跳过')
    def test_search_cat(self):
        self.driver.find_element(By.ID, 'kw').send_keys('猫')
        self.driver.find_element(By.ID, 'su').click()
        title = self.driver.title
        self.assert_(title, '猫_百度搜索')

    # @unittest.skip('无条件跳过')
    def test_search_dog(self):
        self.driver.find_element(By.ID, 'kw').send_keys('狗')
        self.driver.find_element(By.ID, 'su').click()
        title = self.driver.title
        self.assert_(title, '狗_百度搜索')

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
        self.assert_(title, '熊猫_百度搜索')

    def test_search_pig(self):
        self.driver.find_element(By.ID, 'kw').send_keys('小猪')
        self.driver.find_element(By.ID, 'su').click()
        title = self.driver.title
        self.assertEqual(title, '小猪_百度搜索')


#
# def suite():
#     suite = unittest.TestSuite()  # 套件
#     suite.addTest(BaiDu('test_search_dog'))
#     suite.addTest(BaiDu('test_search_cat'))
#     suite.addTest(BaiDu('test_search_rabbit'))
#     suite.addTest(BaiDu('test_search_panda'))
#     suite.addTest(BaiDu('test_search_pig'))
#     return suite

if __name__ == '__main__':
    suite = unittest.TestSuite()  # 套件
    suite.addTest(BaiDu('test_search_dog'))
    suite.addTest(BaiDu('test_search_cat'))
    suite.addTest(BaiDu('test_search_rabbit'))
    suite.addTest(BaiDu('test_search_panda'))
    suite.addTest(BaiDu('test_search_pig'))
    now = time.strftime('%Y-%m-%d_%H_%M_%S ', time.localtime(time.time()))
    report_path = 'C:\\Users\\ytt\\PycharmProjects\\pythonProject\\report\\' \
                  'TestReport_' + now + '.html'
    fp = open(report_path, 'w', encoding='utf-8')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="测试报告",
                                           description="用例执行情况")
    runner.run(suite)
