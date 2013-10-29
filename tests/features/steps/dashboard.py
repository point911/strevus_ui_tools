# -*- coding: utf-8 -*-

from behave import *

@step('I put "{any_name}" entity name to search field')
def i_put_entity_name_to_search_field(context, any_name):
    context.page.find_entity(any_name)


@step('I found "{any_name}" entity in search result')
def i_found_entity_in_search_result(context, any_name):
    if any_name == "any":
        pass