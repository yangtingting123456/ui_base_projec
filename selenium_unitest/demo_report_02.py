import unittest, HTMLTestRunner, time
from send_email import email_utls
if __name__ == '__main__':
    case_path = 'C:\\Users\\ytt\\PycharmProjects\\pythonProject\\selenium_unitest'
    all_case = unittest.defaultTestLoader.discover(start_dir=case_path,
                                                   pattern='test_*.py',
                                                   top_level_dir=None)
    main_suit = unittest.TestSuite()
    main_suit.addTest(all_case)
    report_path = 'C:\\Users\\ytt\\PycharmProjects\\pythonProject\\report\\TestReport_' + time.strftime('%Y-%m-%d_%H_%M_%S ', time.localtime(time.time())) + '.html'
    fp = open(report_path, 'w', encoding='utf-8')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title="测试报告",
                                           description="用例执行情况")
    runner.run(main_suit)
    email_utls.send_email_fujian(report_path,'TestReport_' + time.strftime('%Y-%m-%d_%H_%M_%S ', time.localtime(time.time())) + '.html')

