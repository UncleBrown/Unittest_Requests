#读取config.ini文件的配置，并返回文件内容
import os
import configparser #内置函数，支持.conf/ini文件
from testFile import getpathInfo #导入统计模块有坑，注意领悟（import getpathInfo error）

path = getpathInfo.get_path()
config_path = os.path.join(path,'config.ini') #os.path.join(path1[,path2,..])将多个路径组合返回
print(f"config_path:{config_path}")

config=configparser.ConfigParser()
config.read(config_path, encoding='utf-8')

class ReadConfig():
    
    def get_http(self,name):
        value = config.get('HTTP',name) #name为str
        return value
        
    def get_email(self,name):
        value = config.get('EMAIL',name)
        return value
    
    def get_mysql(self,name):
        value = config.get('DATABASE',name) 
        return value
        
if __name__ == "__main__":
    print(f'HTTP[baseurl]:{ReadConfig().get_http("baseurl")}')
    print(f'EMAIL[on_off]:{ReadConfig().get_email("on_off")}')