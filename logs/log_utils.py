import logging, os

logs_path = os.path.join(os.path.dirname(__file__), 'python.log')


class LogUtils:
    def __init__(self, log_path=logs_path):
        self.logger = logging.getLogger('写入日志')
        self.logger.setLevel(level=logging.INFO)
        file_log = logging.FileHandler(log_path, encoding='utf-8')
        formatter = logging.Formatter("%(asctime)s -- %(filename)s -- %(levelname)s -- %(message)s")
        file_log.setFormatter(formatter)
        self.logger.addHandler(file_log)

    def info(self, message):
        return self.logger.info(message)

    def error(self, message):
        return self.logger.error(message)

    def debug(self, message):
        return self.logger.debug(message)

    def critical(self,message):
        return self.logger.critical()

    def warning(self,message):
        return self.logger.warning(message)

logs_obj = LogUtils()
if __name__ == '__main__':
    logs_obj.info('ee')
