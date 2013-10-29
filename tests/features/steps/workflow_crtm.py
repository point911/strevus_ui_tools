# -*- coding: utf-8 -*-

from behave import *

@step('I click on entities tab')
def i_click_on_entity_tab(context):
    context.page.click_on_entity_tab()

@step('I make choice on outreach status "{status}"')
def i_make_choice_on_outreach_status(context, status):
    context.page.click_on_status(status)

@step('I see four doughunt charts')
def i_see_four_doughunt_charts(context):
    context.page.check_doughunt_charts(4)