__author__ = 'point'

driver_config_path = "/Users/strevus/PycharmProjects/StrevusLoginTest/tests/config/driver.json"

import json
from selenium import webdriver

'''
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
'''

class LoadWebdriver(object):
    def __new__(cls, path):
        return webdriver.PhantomJS(path)

class LoadConfig(object):
    def __new__(cls, name, path=driver_config_path):
        with open(path, 'r') as dcf:
            config = json.load(dcf)
        return LoadWebdriver(config[name]["path"])

class Driver(object):
    #__metaclass__ = Singleton
    def __new__(cls, name):
        return LoadConfig(name)