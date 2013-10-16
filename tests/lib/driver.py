__author__ = 'point'

driver_config_path = "/Users/strevus/PycharmProjects/StrevusLoginTest/tests/config/driver.json"

import json
from selenium import webdriver

class LoadDriver(object):
    configPath = driver_config_path

    def __new__(cls, name):
        return super(LoadDriver, cls).__new__(cls)


    def __init__(self, driver_name):
        self.name = driver_name
        self.driver = self.getDriver()

    def getDriver(self):
        with open(self.configPath, 'r') as dcf:
            config = json.load(dcf)

        drv = None
        if self.name == "phantomjs":
            drv = webdriver.PhantomJS(config["phantomjs"]["path"])
        return drv
