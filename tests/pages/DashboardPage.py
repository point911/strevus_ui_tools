from lettuce import world
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(object):
    def __init__(self):
        self.env = world.env
        self.driver = world.driver
        world.page = self

