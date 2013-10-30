# -*- coding: utf-8 -*-

import imp

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#from tests.pages.BasePage import BasePage
#from tests.pages.InternalContactPage import EntitiesInternalPage
#from tests.pages.DashboardPage import DashboardPage

BasePage = imp.load_source('BasePage', './pages/BasePage.py')
InternalContactPage = imp.load_source('InternalContactPage', './pages/InternalContactPage.py')
DashboardPage = imp.load_source('DashboardPage', './pages/DashboardPage.py')


class LoginPage(BasePage.BasePage):
    def __init__(self, context):
        super(LoginPage, self).__init__(context)
        self.LoadPage()
        self.context.page = self

    def LoadPage(self):
        self.context.driver.get(self.context.env["url"]+self.context.env['port'])

    def set_username(self, user):
        el_username = self.context.driver.find_element_by_name("username")
        el_username.clear()
        el_username.send_keys(user)

    def set_password(self, password):
        el_password = self.context.driver.find_element_by_id("password")
        el_password.clear()
        el_password.send_keys(password)

    def check_login_page(self):
        try:
            el_login_page = WebDriverWait(self.context.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                                "form#signin-form")))
        except TimeoutException:
            self.context.log.info("NO LOGINPAGE!")

    # Public interface
    def check_remember_pass(self):
        try:
            remember_email_checkbox = self.context.driver.find_element_by_css_selector("#remember")
            if not remember_email_checkbox.is_selected():
                self.context.log.info("Check box remember pass is not selected")
                raise AssertionError
        except NoSuchElementException:
            self.context.log.info("Check box remember pass is not founded")
            raise AssertionError

    def fill_in_credentials(self, user, pswd):
        self.set_username(user)
        self.set_password(pswd)

    def sign_in(self, user_type):
        el_login_button = self.context.driver.find_element_by_id("submitLogin")
        el_login_button.click()

        try:
            WebDriverWait(self.context.driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                    ".user-modal-form")))

            el_remind_button = self.context.driver.find_element_by_css_selector(".btn-link")
            el_remind_button.click()

        except TimeoutException:
            pass

        if user_type == "Internal Contact":
            InternalContactPage.EntitiesInternalPage(self.context)
        elif user_type == "CustomerOutreachTeamMember" or user_type == "Tax Person":
            DashboardPage.DashboardPage(self.context)
        else:
            self.context.log.info("PAGE TYPE {0} IS NOT IMPLEMENTED!".format(user_type))

    def remember_pass(self):
        remember_email_checkbox = self.context.driver.find_element_by_css_selector("#remember")
        remember_email_checkbox.click()

    def getLoginName(self):
        el_username = self.context.driver.find_element_by_name("username")
        return el_username.get_attribute("value")


