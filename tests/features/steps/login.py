# -*- coding: utf-8 -*-

from behave import *
from tests.pages.StrevusLoginPage import *




@step('I am signed in as "{user_type}"')
def i_am_signed_in_as(context, user_type):
    context.log.info("Step sign in as {0} begins...".format(user_type))
    LoginPage(context)
    context.log.info("Step sign in as {0} ended.".format(user_type))

'''

    world.page.fill_in_credentials(world.users[user_type]["email"], world.users[user_type]["pswd"])
    world.page.sign_in(user_type)
'''
