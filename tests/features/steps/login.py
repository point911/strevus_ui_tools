# -*- coding: utf-8 -*-

from behave import *
from tests.pages.StrevusLoginPage import LoginPage


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
        context.page.check_dashboard_page()

    elif landing_page == "Internal Contact Entities":
        context.page.check_entities_page()


@step('I want to remember my login nick@fd.com after sign in')
def i_want_to_remember_my_login_after_sign_in(context):
    LoginPage(context)
    context.page.fill_in_credentials("nick@fd.com", "pswd")
    context.page.remember_pass()
    context.page.sign_in("Internal Contact")

@step('I sign out from application')
def i_sign_out_form_application(context):
    context.page.logout()

@step('I see login page with pre-populated email nick@fd.com')
def i_see_login_page_with_pre_populated_email(context):
    context.page.check_login_page()
    context.page.check_remember_pass()
    b = context.page.getLoginName()

    if "nick@fd.com" not in b:
        context.log.info("Login name is not correct")
        raise AssertionError
