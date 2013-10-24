import time
from lettuce import world
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EntitiesInternalPage(object):
    def __init__(self):
        self.driver = world.driver
        world.page = self

    def logout(self):
        self.driver.get(world.env["url"]+world.env['port']+"logout")
        from . import StrevusLoginPage
        world.page = StrevusLoginPage.LoginPage()

    def click_on_entity(self, name):
        if name == "any":
            pass
            #el_entities = self.get_entities()
            #self.legal_entity_name = el_entities[0].text
            #el_entities.click()
            #self.check_LE_name()

    def check_LE_name(self):
        el_name = self.driver.find_element_by_css_selector(".span8 h3")
        if not self.legal_entity_name in el_name.text:
            world.log.info("LE Name is not correct")