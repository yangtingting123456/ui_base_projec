import unittest

class Test_Info(unittest.TestCase):
    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    #普通的测试方法
    def test_case_01(self):
        print('test_case_01')

    def test_case_02(self):
        print('test_case_02')

    def test_case_03(self):
        print('test_case_03')

