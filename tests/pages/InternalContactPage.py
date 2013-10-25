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

    def click_on_contacts(self):
        els_left_menu = world.driver.find_elements_by_css_selector(".js-tab-item")
        world.log.info(len(els_left_menu))

        for el_menu in els_left_menu:
            if el_menu.get_attribute("data-tab-type") == u"contacts":
                el_menu.click()
                time.sleep(1)


    def check_myself_as_assigned_contact(self, login_user_type):
        world.log.info(world.users[login_user_type])

        full_name = world.users[login_user_type][u"fname"] + u" " + world.users[login_user_type][u"sname"]
        world.log.info("FULL NAME IS: {0}".format(full_name))

        assigned_contacts = self.get_assigned_internal_contacts()

        f_flag = False

        for contact in assigned_contacts:
            if full_name in contact:
                f_flag = True

        if not f_flag:
            world.log.info("CONTACT NOT FOUND")
            raise AssertionError

    def get_assigned_internal_contacts(self):
        full_names = []
        contact_cards = world.driver.find_elements_by_css_selector(".contact-card h4")
        for card in contact_cards:
            full_names.append(card.text)
            world.log.info(card.text)

        return full_names
