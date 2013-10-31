# -*- coding: utf-8 -*-

import time

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .BasePage import BasePage

class EntitiesInternalPage(BasePage):
    def __init__(self, context):
        super(EntitiesInternalPage, self).__init__(context)
        context.page = self

    def check_entities_page(self):
        try:
            entities = WebDriverWait(self.context.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                                    ".entities-list")))
        except TimeoutException:
            self.context.log.info("Internal contact entities page is NOT presented.")
            raise AssertionError

#=====
    def click_on_entity(self, name):
        if name == "any":
            entity_fields = self.context.driver.find_elements_by_css_selector(".list-item")
            sub = entity_fields[0].find_elements_by_css_selector("td a")
            entity_name = sub[1].text

            sub[1].click()
            time.sleep(3)

            self.check_le_name(entity_name)

    def check_le_name(self, entity_name):
        el_real_entity = self.context.driver.find_element_by_css_selector(".js-outreach-head h3")
        self.context.log.info(u"REAL NAME: {0}".format(el_real_entity.text))

        if entity_name != el_real_entity.text:
            self.context.log.info("LE Name is NOT correct")
            raise AssertionError

    def click_on_contacts(self):
        els_left_menu = self.context.driver.find_elements_by_css_selector(".js-tab-item")

        for el_menu in els_left_menu:
            if el_menu.get_attribute("data-tab-type") == u"contacts":
                el_menu.click()
                time.sleep(1)

    def check_myself_as_assigned_contact(self, login_user_type):
        self.context.log.info(self.context.users[login_user_type])

        full_name = self.context.users[login_user_type]["fname"] + " " + self.context.users[login_user_type]["sname"]
        self.context.log.info("FULL NAME IS: {0}".format(full_name))

        assigned_contacts = self.get_assigned_internal_contacts()
        self.context.log.info("ASSIGNED CONTACTS ARE: {0}".format(assigned_contacts))
        f_flag = False

        for contact in assigned_contacts:
            if full_name in contact:
                f_flag = True

        if not f_flag:
            self.context.log.info("CONTACT NOT FOUND")
            raise AssertionError

    def get_assigned_internal_contacts(self):
        full_names = []
        contact_cards = self.context.driver.find_elements_by_css_selector(".contact-card")
        self.context.log.info("CONTACT CARDS ARE: {0}".format(contact_cards))
        for card in contact_cards:
            try:
                sub = card.find_element_by_css_selector(".info-name")
                full_names.append(sub.text)
                self.context.log.info("SUB TEXT IS {0}".format(sub.text))
            except:
                pass

        return full_names

    def on_entity_click_not_my_account(self, entity):
        if entity == "name":
            entity_fields = self.context.driver.find_elements_by_css_selector(".list-item")
            sub = entity_fields[0].find_elements_by_css_selector("td a")
            self.entity = entity_fields[0]
            self.entity_name = sub[1].text

            '''
            self.click_not_my_account(entity_fields[0])

            all_names = []

            entity_fields = world.driver.find_elements_by_css_selector(".list-item")
            for entity in entity_fields:
                sub = entity.find_elements_by_css_selector("td a")
                all_names.append(sub[1].text)

            if entity_name in all_names:
                world.log.info("ENTITY STILL PRESENT")
                # raise AssertionError
            '''

    def click_not_my_account(self):
        sub = self.entity.find_elements_by_css_selector("td a")
        sub[3].click()

        time.sleep(1)
        #self.click_i_dont_know()

        self.check_entity_existance()

    def click_i_dont_know(self):
        delete_link = self.context.driver.find_element_by_css_selector(".js-dont-know-link")
        delete_link.click()
        time.sleep(1)

    def check_entity_existance(self):
        all_names = []

        entity_fields = self.context.driver.find_elements_by_css_selector(".list-item")
        for entity in entity_fields:
            sub = entity.find_elements_by_css_selector("td a")
            all_names.append(sub[1].text)

        if self.entity_name in all_names:
            self.context.log.info("ENTITY STILL PRESENT")
            # raise AssertionError
