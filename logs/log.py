# python 日志
import logging, os

logger = logging.getLogger('print log')

# logging模块日志级别有DEBUG < INFO < WARNING < ERROR < CRITICAL 五种。
#
# DEBUG - 调试模式，应用场景是问题诊断；
# INFO - 通常只记录程序中一般事件的信息，用于确认工作一切正常；
# WARNING - 打印警告信息，系统还在正常运行；
# ERROR - 错误导致某些功能不能正常运行时记录的信息；
# CRITICAL - 当发生严重错误，导致应用程序不能继续运行时记录的信息

logger.setLevel(level=logging.INFO)  #设置日志级别
# 1.在控制台打印日志
console = logging.StreamHandler()   #创建控制台输出对象
# %(levelno)s：打印日志级别的数值             %(levelname)s：打印日志级别的名称
# %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
# %(filename)s：打印当前执行程序名            %(funcName)s：打印日志的当前函数
# %(lineno)d：打印日志的当前行号              %(asctime)s：打印日志的时间
# %(thread)d：打印线程ID                    %(threadName)s：打印线程名称
# %(process)d：打印进程ID                   %(message)s：打印日志信息
formatter = logging.Formatter("%(asctime)s -- %(filename)s -- %(levelname)s -- %(message)s")
console.setFormatter(formatter)
logger.addHandler(console)  #在控制台打印
logger.info('控制台输出info级别日志')
logger.error('控制台输出error级别日志')
logger.debug('控制台输出debug级别日志')


# 2.将日志写入文件
log_path = os.path.join(os.path.dirname(__file__),'python.log')
file_log = logging.FileHandler(log_path,encoding='utf-8')
formatter = logging.Formatter("%(asctime)s -- %(filename)s -- %(levelname)s -- %(message)s")
file_log.setFormatter(formatter)
logger.addHandler(file_log)
logger.info('文件输出info级别日志')
logger.error('文件输出error级别日志')
logger.debug('控制台输出debug级别日志')

#将日志做成类然后使用
