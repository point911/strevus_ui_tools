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


# Iinit Global test environment
sp = InitWorld()

# Import page objects
world.log.info("3 WORLD IN STEPS.PY {0}".format(world))

@step(u'TearDown')
def TearDown(step):
    world.page.logout()

@before.outline
def setup_tearup_outline(feature, *args):
    world.log.info("OUTLINER ARGUMENTS ARE: {0}".format(args))

@before.each_scenario
def setup_tearup_features(feature):
    world.log.info("4 WORLD IN BEFORE ALL {0}".format(world))
    world.log.info("5 INITIALIZING STEP")
    world.log.info("PHANTOM")
    world.driver = world.init_driver("phantomjs")
    world.log.info(world.driver)
    world.log.info("6 BEFORE ALL END")

@after.outline
def setup_teardown_outline(feature, *args):
    world.page.logout()


@after.each_scenario
def setup_teardown_feature(feature):
    world.page.logout()
    world.driver.delete_all_cookies()
    world.driver.close()
    sp.tear_down_world()
    world.log.info("PHANTOM KILLED")

@step(u'I am signed in as "([^"]*)"')
def given_i_have_login_url(step, email):
    LoginPage()
    world.log.info("9 IN FIRST STEP")
    world.log.info("10 WORLD IN FIRST STEP: {0}".format(world))
    world.log.info(world)
    world.log.info("Running step: I have login url...")

    world.page.fill_in_credentials(email, "pswd")

    world.page.sign_in()

    # driver.set_page_load_timeout(1)
    world.log.info("="*20)

@step(u'I should see "([^"]*)"')
def then_i_should_see_landing_page(step, landing_page):

    if landing_page == "Dashboard":
       dashboard = world.driver.find_element_by_css_selector(".dashboard-home")
       if not dashboard.is_displayed():
           world.log.info("No dashboard is presented.")
           raise AssertionError
    elif landing_page == "Internal Contact Entities":
        dashboard = WebDriverWait(world.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                         ".entities-list")))
        # dashboard = world.driver.find_element_by_css_selector(".entities-list")
        if not dashboard.is_displayed():
            world.log.info("No internal contact entities page is presented.")
            raise AssertionError


@step(u'I want to remember my login nick@fd.com after sign in')
def i_want_to_remember_my_login_after_sign_in(step):
    LoginPage()
    world.page.fill_in_credentials("nick@fd.com", "pswd")
    world.page.remember_pass()
    world.page.sign_in()

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
    world.log.info("Login name is: {0}".format(b))
    world.log.info(type(b))
    if "nick@fd.com" not in b:
        world.log.info("Login name is not correct")
        raise AssertionError


@step(u'I check "([^"]*)" legal entity detail')
def i_check_legal_entity_detail(step, user):
    world.page.click_on_entity()