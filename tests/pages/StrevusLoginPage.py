# -*- coding: utf-8 -*-

from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.pages.InternalContactPage import EntitiesInternalPage
from tests.pages.DashboardPage import DashboardPage


class LoginPage(object):
    def __init__(self, context):
        self.context = context
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


    '''
    def logout(self):
        self.driver.get(world.env["url"]+world.env['port']+"logout")
    '''
    # Public interface
    def check_remember_pass(self):

        remember_email_checkbox = self.context.driver.find_element_by_css_selector("#remember")
        if not remember_email_checkbox.is_selected():
            self.context.log.info("Check box remember pass is not selected")
             #raise AssertionError

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
            EntitiesInternalPage(self.context)
        elif user_type == "CustomerOutreachTeamMember" or user_type == "Tax Person":
            DashboardPage(self.context)
        else:
            self.context.log.info("PAGE TYPE {0} IS NOT IMPLEMENTED!".format(user_type))

    def remember_pass(self):
        remember_email_checkbox = self.context.driver.find_element_by_css_selector("#remember")
        remember_email_checkbox.click()

    def getLoginName(self):
        el_username = self.context.driver.find_element_by_name("username")
        return el_username.get_attribute("value")


