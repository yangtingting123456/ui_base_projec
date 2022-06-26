#读取 ini文件
import os,configparser

# 创建对象
conf = configparser.ConfigParser()
#读取整个in文件
config_path = os.path.join(os.path.abspath(__file__),'../config.ini')
conf.read(config_path,encoding='utf-8')

print('所有的组：',conf.sections())
print('一组的数据',conf.items('password'))
print('取指定的内容：',conf.get('name','name1'))
print('某组所有的key',conf.options('password'))

#实际应用：将百度搜索自动化做成从ini配置文件读取url地址
baidu_url = conf.get('baidu_url','url')
print(baidu_url)