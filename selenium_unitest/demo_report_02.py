import unittest, HTMLTestRunner, time

if __name__ == '__main__':
    case_path = 'C:\\Users\\ytt\\PycharmProjects\\pythonProject\\selenium_unitest'
    all_case = unittest.defaultTestLoader.discover(start_dir=case_path,
                                                   pattern='test_*.py',
                                                   top_level_dir=None)
    main_suit = unittest.TestSuite()
    main_suit.addTest(all_case)
    fp = open('C:\\Users\\ytt\\PycharmProjects\\pythonProject\\report\\TestReport_' +
              time.strftime('%Y-%m-%d_%H_%M_%S ', time.localtime(time.time())) + '.html', 'w', encoding='utf-8')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="测试报告",
                                           description="用例执行情况")
    runner.run(main_suit)
