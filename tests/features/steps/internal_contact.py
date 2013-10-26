# -*- coding: utf-8 -*-

from behave import *

@step('I check "{entity}" legal entity detail')
def i_check_legal_entity_detail(context, entity):
    pass
    #context.page.click_on_entity(entity)

@step('I see myself "{log_in_entity_type}" assigned in contacts')
def i_see_myself_assigned_in_contacts(context, log_in_entity_type):
    pass
    #context.page.click_on_contacts()
    #context.page.check_myself_as_assigned_contact(log_in_entity_type)

@step('I see not my legal entity "{entity}"')
def i_see_no_my_legal_entity(context, entity):
    pass
    #context.page.on_entity_click_not_my_account(entity)

@step('I remove my relation with this entity in simple way')
def i_remove_my_relation_with_this_entity_in_simple_way(context):
    pass
    #context.page.click_not_my_account()
