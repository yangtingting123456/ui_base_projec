from selenium_unitest.test_demo_calc import CaCl
import unittest
class Test_CaCl(unittest.TestCase):
    def setUp(self) -> None:
        print('\n')
        print('setUp')

    def tearDown(self) -> None:
        print('tearDown')

    def test_add(self):
        self.assertEqual(CaCl.add(2,3),5)
        print('test_add')

    def test_sub(self):
        self.assertEqual(CaCl.sub(2,3),-1)
        print('test_sub')

    def test_mul(self):
        self.assertEqual(CaCl.mul(2,3),6)
        print('test_mul')

    def test_div(self):
        self.assertEqual(CaCl.div(3,2),1.5)
        print('test_div')

    def test_True(self):
        a = True
        self.assertTrue(a)
        print('test_True')

    def test_False(self):
        b = False
        self.assertFalse(b)
        print('test_False')

    def test_In(self):
        self.assertIn('2','123')
        print('test_in')

    def test_Greater(self):
        self.assertGreater(5,2)
        print('test_Greater')

    def t_in(self):  #普通方法不以test开头，则不会执行
        print('t_in')



