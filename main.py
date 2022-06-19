import json
class SeleniumBaseCase:
    def __int__(self,base_pase):
        self.base_pase = base_pase

    def errors(self):
        errors = self._outcome.errors  #获取当前用例执行的回溯错误信息
        for test,exc_info in errors:
            if exc_info:   #回溯的错误信息是一个元素，元素的第二个元素如果为none,
                           # 表示用例执行成功，所以可以通过if判断，是否需要截图
                self.base_pase.wait()
                self.base_pase.screenshot_as_file()

