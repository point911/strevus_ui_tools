# -*- coding: utf-8 -*-
# import logging

from lettuce import *
import time

# Load terrain
steps_logger = world.log
env = world.env

# print("INIT DRIVER")
# world.driver = world.init_driver("phantomjs")

# Import page objects
from pages.StrevusLoginPage import LoginPage

print("3 WORLD IN STEPS.PY {0}".format(world))

@before.each_feature
def setup_all_features(feature):
    print("4 WORLD IN BEFORE ALL {0}".format(world))
    print("5 INITIALIZING WORLD")
    world.driver = world.init_driver("phantomjs")
    print("6 BEFORE ALL END")



@after.each_feature
def teardown_features(feature):
    print("11 AFTER ALL")
    world.driver.close()

@step(u'I am signed in as single user')
def given_i_have_login_url(step):
    page = LoginPage(env, world)
    print("9 IN FIRST STEP")
    print("10 WORLD IN FIRST STEP: {0}".format(world))
    steps_logger.info(world)


    steps_logger.info("Running step: I have login url...")

    page.fill_in_credentials("fred@fd.com", "pswd")
    page.sign_in()

    time.sleep(1)
    # driver.implicitly_wait(1)
    # driver.set_page_load_timeout(1)
    steps_logger.info("="*20)



@step(u'I should see landing page')
def then_i_should_see_landing_page(step):

    if "dashboard" in world.driver.current_url:
        steps_logger.info("Step: Then I see dashboard url PASSED")
    else:
        steps_logger.info("Step: Then I see dashboard url FAILED")
        raise AssertionError
