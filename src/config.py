import configparser
import os


def get_config(section, option):
    # 获取当前项目的路径
    rootDir = os.path.dirname(os.getcwd())
    # 获取路径到config.ini
    configFilePath = os.path.join(rootDir, 'ConfigParser\config.ini')
    # 根据section, option 获取配置文件下的值
    conf = configparser.ConfigParser()
    conf.read(configFilePath)
    value = conf.get(section, option)
    return value

