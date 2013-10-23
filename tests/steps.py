# -*- coding: utf-8 -*-
# import logging

import lettuce
import time
from lettuce import *
from alternate import *
from pages.StrevusLoginPage import LoginPage


# Iinit Global test environment
sp = InitWorld()

# Import page objects
world.log.info("3 WORLD IN STEPS.PY {0}".format(world))

@before.each_scenario
def setup_all_features(feature):
    world.log.info("4 WORLD IN BEFORE ALL {0}".format(world))
    world.log.info("5 INITIALIZING STEP")
    world.log.info("PHANTOM")
    world.driver = world.init_driver("phantomjs")
    world.log.info(world.driver)
    world.log.info("6 BEFORE ALL END")

@after.each_scenario
def teardown_features(feature):
    world.log.info("11 AFTER ALL")
    world.page.logout()
    world.driver.delete_all_cookies()
    world.driver.close()
    sp.tear_down_world()
    world.log.info("PHANTOM KILLED")

@step(u'I am signed in as single user')
def given_i_have_login_url(step):
    page = LoginPage(world.env)
    world.log.info("9 IN FIRST STEP")
    world.log.info("10 WORLD IN FIRST STEP: {0}".format(world))
    world.log.info(world)
    world.log.info("Running step: I have login url...")

    page.fill_in_credentials("fred@fd.com", "pswd")
    page.sign_in()

    time.sleep(2)
    # driver.implicitly_wait(1)
    # driver.set_page_load_timeout(1)
    world.log.info("="*20)

@step(u'I should see landing page')
def then_i_should_see_landing_page(step):

    world.log.info("Current URL is:".format(world.driver.current_url))

    if "dashboard" in world.driver.current_url:
        world.log.info("Step: Then I see dashboard url PASSED")
    else:
        world.log.info("Step: Then I see dashboard url FAILED")
        raise AssertionError


@step(u'I want to remember my login nick@fd.com after sign in')
def i_want_to_remember_my_login_after_sign_in(step):
    page = LoginPage(world.env)
    page.fill_in_credentials("nick@fd.com", "pswd")
    page.remember_pass()
    page.sign_in()

