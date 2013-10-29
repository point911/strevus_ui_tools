# -*- coding: utf-8 -*-

from behave import *

@step('I check "{entity}" legal entity detail')
def i_check_legal_entity_detail(context, entity):
    context.log.info("Step I check {0} legal entity detail begins...".format(entity))
    context.page.click_on_entity(entity)
    context.log.info("Step I check {0} legal entity detail ended".format(entity))

@step('I see myself "{log_in_entity_type}" assigned in contacts')
def i_see_myself_assigned_in_contacts(context, log_in_entity_type):
    context.log.info("Step I see myself {0} assigned in contacts begins...".format(log_in_entity_type))
    context.page.click_on_contacts()
    context.page.check_myself_as_assigned_contact(log_in_entity_type)
    context.log.info("Step I see myself {0} assigned in contacts ended".format(log_in_entity_type))

@step('I see not my legal entity "{entity}"')
def i_see_no_my_legal_entity(context, entity):
    context.log.info("Step I see not my legal entity {0} begins...".format(entity))
    context.page.on_entity_click_not_my_account(entity)
    context.log.info("Step I see not my legal entity {0} ended...".format(entity))

@step('I remove my relation with this entity in simple way')
def i_remove_my_relation_with_this_entity_in_simple_way(context):
    context.log.info("Step I remove my relation with this entity in simple way begins...")
    context.page.click_not_my_account()
    context.log.info("Step I remove my relation with this entity in simple way ended")
