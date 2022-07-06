# -- coding: utf-8 --
# @Time : 2022/7/6 13:42
# @Author : siyu.yang
# 自动化测试  框架简介
# 框架的概念：
#     在系统开发过程中，框架是指对特定应用领域中的应用系统的部分设计和实现
# 子系统的整体结构。
#     框架将应用系统划分类和对象，定义类和对象的责任，类和对象如何相互协助，
# 以及对象之间的控制线程。这些共有的设计因素由框架预定义，应用开发人员只需关注于
# 特定的应用系统特有部分。
# 自动化测试框架定义为：
#     由一个或多个自动化测试基础模块、自动化测试管理模块、自动化测试统计模块
# 等组成的工具集合。
#     . 按框架的定义来分，自动化测试框架可分为：基础功能测试框架、管理执行框架；
#     . 按不同的测试类型来分，可以分为：功能自动化测试框架、性能自动化测试框架；
#     . 按组成结构来分，可以分为：单一自动化测试框架、综合自动化测试框架；
#     . 按部署方式来分，可以分为：单机自动化测试框架、分布式自动化测试框架。
#   熟悉Unittest测试框架是后续使用python 进行自动化测试基础，Unittest框架（又名Pyunit框架），
# 为python语言的单元测试框架。https://docs.python.org/2.7/library/unittest.html#module-unittest
# Unittest测试框架使用介绍：
#     a)用import语句引入unittest模块
#     b)让所有执行测试的类都继承于TestCase类,可以将TestCase看成是对特定类进行测试的方法的集合
#     c)setUp()方法中进行测试前的初始化工作，teardown()方法中执行测试后的清除工作，它们都是TestCase中的方法
#     d)编写测试的方法最好以test开头（可以直接运行）def test_add(self) 、def test_sub(self)等，可以编写多个测试用例对被测对象进行测试
#     e)在编写测试方法过程中，使用TestCase class提供的方法测试功能点，比如：assertEqual等
#     f)调用unittest.main()方法运行所有以test开头的方法


# unittest中常用的assert语句:
# assertEqual(a, b)                  a == b
# assertNotEqual(a, b)           a != b
# assertTrue(x)                         bool(x) is True
# assertFalse(x)                        bool(x) is False
# assertIs(a, b)                          a is b
# assertIsNot(a, b)                   a is not b
# assertIsNone(x)                    x is None
# assertIsNotNone(x)             x is not None
# assertIn(a, b)                         a in b
# assertNotIn(a, b)                  a not in b
# assertIsInstance(a, b)         isinstance(a, b)
# assertNotIsInstance(a, b)  not isinstance(a, b)
# assertGreater(a, b)               a > b
# assertGreaterEqual(a, b)    a >= b
# assertLess(a, b)                     a < b
# assertLessEqual(a, b)          a <= b
# assertNotEqual(a, b)           a != b
# assertTrue(x)                         bool(x) is True
# assertFalse(x)                        bool(x) is False
# assertIs(a, b)                          a is b
# assertIsNot(a, b)                   a is not b
# assertIsNone(x)                    x is None
# assertIsNotNone(x)             x is not None
# assertIn(a, b)                         a in b
# assertNotIn(a, b)                  a not in b
# assertIsInstance(a, b)         isinstance(a, b)
# assertNotIsInstance(a, b)  not isinstance(a, b)
# assertGreater(a, b)               a > b
# assertGreaterEqual(a, b)    a >= b
# assertLess(a, b)                     a < b
# assertLessEqual(a, b)          a <= b


# unittest构建测试套件（测试用例集合）：
# 前提Tester是继承了unittest.TestCase的子类方式一：
# Suite = unittest.TestSuite()Suite.addTest(Tester('test_default_size'))
# Suite.addTest(Tester('test_resize'))
# 方式二（推荐）：
# def suite():
#     suite = unittest.TestSuite()
#     suite.addTest(Tester('test_default_size'))
#     suite.addTest(Tester('test_resize'))
#     return suite
# 方式三（推荐）：
# def suite():
#     tests = ['test_default_size', 'test_resize']
#     return unittest.TestSuite(map(Tester, tests))


# unittest忽略测试用例：
#      Python 2.7支持忽略部分测试用例不执行，分无条件忽略和有条件忽略,
# 通过装饰器实现。
# 使用unitest.skip装饰器族跳过test method或者test class,这些装饰器包括:
# ①@unittest.skip(reason):无条件跳过测试，reason描述为什么跳过测试
# ②@unittest.skipIf(conditition,reason):condititon为true时跳过测试
# ③@unittest.skipUnless(condition,reason):condition不是true时跳过测试
# ④@expected failure:使用@unittest.expectedFailure装饰器，如果test失败了，
# 这个test不计入失败的case数目
# 举例：
# def testsub(self):  #具体的测试用例
#     self.assertEqual(self.testnum.sub(),-1,"testing sub")
#     @unittest.skip("test skipping")        #跳过测试用例
#     def testmulti(self):  #具体的测试用例
#         self.assertEqual(self.testnum.multi(),12,"testing multi")



