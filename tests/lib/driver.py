__author__ = 'point'

driver_config_path = "./tests/config/driver.json"

import json
from selenium import webdriver


class LoadWebdriver(object):
    def __new__(cls, name, config):
        if name == "phantomjs":
            return webdriver.PhantomJS(config[name]["path"])
        elif name == "firefox":
            return webdriver.Firefox()
        else:
            print("NO SUCH DRIVER")
            exit(1)


class LoadConfig(object):
    def __new__(cls, name, path=driver_config_path):
        with open(path, 'r') as dcf:
            config = json.load(dcf)
        return LoadWebdriver(name, config)


class Driver(object):
    def __new__(cls, name):
        return LoadConfig(name)