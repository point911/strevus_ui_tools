import time

class EntitiesInternalPage(object):
    def __init__(self, context):
        self.context = context
        context.page = self

    def logout(self):
        self.context.driver.get(self.context.env["url"]+self.context.env['port']+"logout")
        from .StrevusLoginPage import LoginPage
        self.context.page = LoginPage(self.context)

"""
    def click_on_entity(self, name):
        if name == "any":
            entity_fields = world.driver.find_elements_by_css_selector(".list-item")
            sub = entity_fields[0].find_elements_by_css_selector("td a")
            entity_name = sub[1].text

            sub[1].click()
            time.sleep(3)

            self.check_le_name(entity_name)

    def check_le_name(self, entity_name):
        el_real_entity = world.driver.find_element_by_css_selector(".js-outreach-head h3")
        world.log.info(u"REAL NAME: {0}".format(el_real_entity.text))

        if entity_name != el_real_entity.text:
            world.log.info("LE Name is NOT correct")
            raise AssertionError

    def click_on_contacts(self):
        els_left_menu = world.driver.find_elements_by_css_selector(".js-tab-item")

        for el_menu in els_left_menu:
            if el_menu.get_attribute("data-tab-type") == u"contacts":
                el_menu.click()
                time.sleep(1)

    def check_myself_as_assigned_contact(self, login_user_type):
        world.log.info(world.users[login_user_type])

        full_name = world.users[login_user_type][u"fname"] + u" " + world.users[login_user_type][u"sname"]
        world.log.info("FULL NAME IS: {0}".format(full_name))

        assigned_contacts = self.get_assigned_internal_contacts()

        f_flag = False

        for contact in assigned_contacts:
            if full_name in contact:
                f_flag = True

        if not f_flag:
            world.log.info("CONTACT NOT FOUND")
            raise AssertionError

    def get_assigned_internal_contacts(self):
        full_names = []
        contact_cards = world.driver.find_elements_by_css_selector(".contact-card h4")
        for card in contact_cards:
            full_names.append(card.text)

        return full_names

    def on_entity_click_not_my_account(self, entity):
        if entity == "name":
            entity_fields = world.driver.find_elements_by_css_selector(".list-item")
            sub = entity_fields[0].find_elements_by_css_selector("td a")
            self.entity = entity_fields[0]
            self.entity_name = sub[1].text

            '''
            self.click_not_my_account(entity_fields[0])

            all_names = []

            entity_fields = world.driver.find_elements_by_css_selector(".list-item")
            for entity in entity_fields:
                sub = entity.find_elements_by_css_selector("td a")
                all_names.append(sub[1].text)

            if entity_name in all_names:
                world.log.info("ENTITY STILL PRESENT")
                # raise AssertionError
            '''

    def click_not_my_account(self):
        sub = self.entity.find_elements_by_css_selector("td a")
        sub[3].click()

        time.sleep(1)
        #self.click_i_dont_know()

        self.check_entity_existance()

    def click_i_dont_know(self):
        delete_link = world.driver.find_element_by_css_selector(".js-dont-know-link")
        delete_link.click()
        time.sleep(1)

    def check_entity_existance(self):
        all_names = []

        entity_fields = world.driver.find_elements_by_css_selector(".list-item")
        for entity in entity_fields:
            sub = entity.find_elements_by_css_selector("td a")
            all_names.append(sub[1].text)

        if self.entity_name in all_names:
            world.log.info("ENTITY STILL PRESENT")
            # raise AssertionError
"""