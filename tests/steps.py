# -*- coding: utf-8 -*-
# import logging


import lettuce
import time
from lettuce import *
from alternate import *
from pages.StrevusLoginPage import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""""
# Iinit Global test environment
sp = InitWorld()

@before.outline
def setup_tearup_outline(feature, *args):
    pass

@before.each_scenario
def setup_tearup_features(scenario):
    world.log.info(scenario)
    world.driver = world.init_driver("firefox")

@after.outline
def setup_teardown_outline(feature, *args):
    world.page.logout()
    world.log.info("="*20)

@after.each_scenario
def setup_teardown_feature(scenario):
    world.page.logout()
    world.driver.delete_all_cookies()
    world.driver.close()
    sp.tear_down_world()
    world.log.info("="*20)

@step(u'I am signed in as "([^"]*)"')
def i_am_signed_in_as(step, user_type):
    LoginPage()
    world.log.info("Running step: I have login url...")
    world.page.fill_in_credentials(world.users[user_type]["email"], world.users[user_type]["pswd"])
    world.page.sign_in(user_type)


@step(u'I should see "([^"]*)"')
def then_i_should_see_landing_page(step, landing_page):

    if landing_page == "Dashboard":
       dashboard = world.driver.find_element_by_css_selector(".dashboard-home")
       if not dashboard.is_displayed():
           world.log.info("No dashboard is presented.")
           raise AssertionError
    elif landing_page == "Internal Contact Entities":
        dashboard = WebDriverWait(world.driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                         ".entities-list")))

        #dashboard = world.driver.find_element_by_css_selector(".entities-list")
        if not dashboard.is_displayed():
            world.log.info("No internal contact entities page is presented.")
            raise AssertionError



@step(u'I want to remember my login nick@fd.com after sign in')
def i_want_to_remember_my_login_after_sign_in(step):
    LoginPage()
    world.page.fill_in_credentials("nick@fd.com", "pswd")
    world.page.remember_pass()
    world.page.sign_in(u"Internal Contact")

@step(u'I sign out from application')
def i_sign_out_form_application(step):
    time.sleep(1)
    world.page.logout()

@step(u'I see login page with pre-populated email nick@fd.com')
def i_see_login_page_with_pre_populated_email(step):
    time.sleep(3)
    world.page.isLoginPage()
    world.page.check_remember_pass()
    b = world.page.getLoginName()

    if "nick@fd.com" not in b:
        world.log.info("Login name is not correct")
        raise AssertionError


@step(u'I check "([^"]*)" legal entity detail')
def i_check_legal_entity_detail(step, entity):
    world.page.click_on_entity(entity)

@step(u'I see myself "([^"]*)" assigned in contacts')
def i_see_myself_assigned_in_contacts(step, log_in_entity_type):
    world.page.click_on_contacts()
    world.page.check_myself_as_assigned_contact(log_in_entity_type)

@step(u'I see not my legal entity "([^"]*)"')
def i_see_no_my_legal_entity(step, entity):
    world.page.on_entity_click_not_my_account(entity)

@step(u'I remove my relation with this entity in simple way')
def i_remove_my_relation_with_this_entity_in_simple_way(step):
    world.page.click_not_my_account()
"""

