#读取配置文件
import configparser, os

config_path = os.path.join(os.path.dirname(__file__), '../conf/config.ini')


class ConfigUtils:
    def __init__(self, cof_path):
        self.config_path = cof_path
        self.conf = configparser.ConfigParser()
        self.conf.read(self.config_path, encoding='utf-8')

    '''
    获取所有的组
    '''

    def get_sections(self):
        return self.conf.sections()

    '''
    获取一组数据
    '''

    def get_items(self, item):
        return self.conf.items(item)

    '''
    获取配置文件指定的内容
    '''

    def get_values(self, key, value):
        return self.conf.get(key, value)

    '''
    获取配置文件某组的key
    '''

    def get_options(self, key):
        return self.conf.options(key)

    def get_baidu_url(self):
        return self.conf.get('baidu_url','url')

    def get_username(self,key,value):
        return self.conf.get(key, value)

    def get_password(self,key,value):
        return self.conf.get('baidu_url','url')

config = ConfigUtils(config_path)
if __name__ == '__main__':
    config = ConfigUtils(config_path)
    print(config.get_sections())
    print(config.get_items('baidu_url'))
    print(config.get_values('baidu_url', 'url'))
    print(config.get_options('name'))
    print(config.get_baidu_url())
    print(config.get_username('name','name1'))
    print(config.get_password('password','password1'))
