# -*- coding: utf-8 -*-

from behave import *
from tests.pages.StrevusLoginPage import *


@step('I am signed in as "{user_type}"')
def i_am_signed_in_as(context, user_type):
    context.log.info("Step sign in as {0} begins...".format(user_type))
    LoginPage(context)
    context.page.fill_in_credentials(context.users[user_type]["email"], context.users[user_type]["pswd"])
    context.page.sign_in(user_type)
    context.log.info("Step sign in as {0} ended.".format(user_type))

@step('I should see "{landing_page}"')
def then_i_should_see_landing_page(context, landing_page):

    if landing_page == "Dashboard":
        
        dashboard = context.driver.find_element_by_css_selector(".dashboard-home")
        if not dashboard.is_displayed():
           context.log.info("No dashboard is presented.")
           raise AssertionError

    elif landing_page == "Internal Contact Entities":
        entities = WebDriverWait(context.driver, 60).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                            ".entities-list")))

        #dashboard = world.driver.find_element_by_css_selector(".entities-list")
        if not entities.is_displayed():
            context.log.info("No internal contact entities page is presented.")
            raise AssertionError
