import time
from lettuce import world
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EntitiesInternalPage(object):
    def __init__(self):
        world.page = self

    def logout(self):
        world.driver.get(world.env["url"]+world.env['port']+"logout")
        from . import StrevusLoginPage
        world.page = StrevusLoginPage.LoginPage()

    def click_on_entity(self, name):
        if name == "any":

            entity_fields = world.driver.find_elements_by_css_selector(".list-item")
            world.log.info(len(entity_fields))

            sub = entity_fields[0].find_elements_by_css_selector("td a")
            world.log.info(len(sub))

            entity_name = sub[1].text

            world.log.info(u"ENTITY NAME: {0}".format(sub[1].text))
            world.log.info(u"ENTITY CLASS NAME: {0}".format(sub[1].text.__class__))
            # selenium.webdriver.remote.webelement.WebElement
            # WebElement.get_attribute("value")
            # world.log.info("ENTITY NAME: {0}".format(sub[1].text))#get_attribute("value"))

            sub[1].click()
            time.sleep(3)

            self.check_le_name(entity_name)

    def check_le_name(self, entity_name):

        el_real_entity = world.driver.find_element_by_css_selector(".js-outreach-head h3")
        world.log.info(u"REAL NAME: {0}".format(el_real_entity.text))

        if entity_name != el_real_entity.text:
            world.log.info("LE Name is NOT correct")
            raise AssertionError

