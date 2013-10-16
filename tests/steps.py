__author__ = 'point'
# -*- coding: utf-8 -*-

import time
import logging
import imp

from lettuce import *

driver_module = imp.load_source('driver', '/Users/strevus/PycharmProjects/StrevusLoginTest/tests/lib/driver.py')


steps_log_config = logging.basicConfig(filename='steps.log',
                               filemode='w',
                               level=logging.INFO)

steps_logger = logging.getLogger(steps_log_config)

driver_factory = driver_module.LoadDriver("phantomjs")


@step(u'Given I have login url "([^"]*)"')
def given_i_have_login_url(step, string):
    steps_logger.info("Running step: I have login url...")
    driver = driver_factory.getDriver()
    driver.get('http://localhost:1025/')

    if "Strevus" in driver.title:
        steps_logger.info("Step I have login url PASSED")
    else:
        steps_logger.info("Step I have login url FAILED")
        raise AssertionError
    driver.close()
    steps_logger.info("="*20)


@step(u'When I login through phantomjs')
def when_i_login_through_phantomjs(step):
    steps_logger.info("Running step: When I login through phantomjs...")
    driver = driver_factory.getDriver()
    driver.get('http://localhost:1025/')
    username = driver.find_element_by_name("username")
    username.send_keys("fred@fd.com")
    password = driver.find_element_by_id("password")
    password.send_keys("pswd")
    button = driver.find_element_by_id("submitLogin")
    button.click()
    driver.implicitly_wait(1)
    steps_logger.info("Step: When I login through phantomjs PASSED")
    steps_logger.info("="*20)


@step(u'Then I see dashboard url "([^"]*)"')
def then_i_see_page_title(step, string):
    steps_logger.info("Running step: Then I see dashboard url...")

    driver = driver_factory.getDriver()
    driver.get('http://localhost:1025/')
    username = driver.find_element_by_name("username")
    username.send_keys("fred@fd.com")
    password = driver.find_element_by_id("password")
    password.send_keys("pswd")
    button = driver.find_element_by_id("submitLogin")
    button.click()
    #driver.implicitly_wait(1)
    time.sleep(1)
    steps_logger.info(string)
    steps_logger.info(driver.current_url)
    if string in driver.current_url:
        steps_logger.info("Step: Then I see dashboard url PASSED")
    else:
        steps_logger.info("Step: Then I see dashboard url FAILED")
        raise AssertionError
    driver.close()
    steps_logger.info("="*20)

