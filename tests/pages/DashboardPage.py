from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from BasePage import BasePage


class DashboardPage(BasePage):
    def __init__(self, context):
        super(DashboardPage, self).__init__(context)
        #self.context = context
        context.page = self

    def check_dashboard_page(self):
        try:
            el_dash = WebDriverWait(self.context.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                                  ".dashboard-home")))

        except TimeoutException:
            self.context.log.info("No dashboard is presented.")
            raise AssertionError

    def find_entity(self, entity_name):
        try:
            el_find = WebDriverWait(self.context.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                                  ".input-block-level")))
            if entity_name == "any":
                self.click_on_total_entities()
                sample_name = self.get_first_entity_name()

            el_find.clear()
            el_find.send_keys(sample_name)

            find_result = self.check_entity_presence(sample_name)

            if find_result != sample_name:
                self.context.log.info("Input name and find name are nor equal")
                raise AssertionError

            self.context.log.info("FIND RESULT IS {0}".format(find_result))

        except TimeoutException:
            self.context.log.info("No find filed is presented.")

    def click_on_total_entities(self):
        try:
            WebDriverWait(self.context.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                        ".campaign-stats-region")))
        except TimeoutException:
            self.context.log.info("Statuses are not presented!")
            raise AssertionError

        el_stats = self.context.driver.find_elements_by_css_selector(".campaign-stats-region .row-fluid.sub-item")

        for status in el_stats:
            status_name = status.find_element_by_css_selector(".span10")
            self.context.log.info("STATUS NAME IS {0}".format(status_name.text))
            if status_name.text == u"Total entities":
                status_link = status.find_element_by_css_selector(".attent-value")
                status_link.click()
                break

            #self.context.log.info("STATUS NAME IS {0}".format(status.text))

        self.context.log.info("STATS ARE: {0}".format(el_stats))

    def get_first_entity_name(self):

        try:
            entities = WebDriverWait(self.context.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                        ".js-results-items")))
        except TimeoutException:
            self.context.log.info("Entities are not presented!")
            raise AssertionError

        first_entity = entities.find_element_by_css_selector("tr")
        first_entity_link = first_entity.find_elements_by_css_selector("td")[4]
        first_entity_name = first_entity_link.find_element_by_css_selector("a").text
        self.context.log.info("ENTITY NAME IS {0}".format(first_entity_name))

        return first_entity_name

    def check_entity_presence(self, entity_name):
        try:
            search_results = WebDriverWait(self.context.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                        ".js-results-items")))
        except TimeoutException:
            self.context.log.info("Search result is empty!")
            raise AssertionError

        first_entity = search_results.find_element_by_css_selector("tr")
        first_entity_link = first_entity.find_elements_by_css_selector("td")[4]
        first_entity_name = first_entity_link.find_element_by_css_selector("a").text

        return first_entity_name

    def click_on_entity_tab(self):
        el_entity = self.context.driver.find_elements_by_css_selector(".nav.nav-pills.pull-right > li")[1]
        el_entity_link = el_entity.find_element_by_css_selector("a")
        el_entity_link.click()

    def click_on_status(self, status):
        try:
            el_statuses = WebDriverWait(self.context.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                        "#filter-group-outreachStatus")))
        except TimeoutException:
            self.context.log.info("There are no statuses!")
            raise AssertionError

        self.context.log.info("STATUS IS: {0}".format(status))

        el_sub_statuses = el_statuses.find_elements_by_css_selector(".radio")
        for el_sub_status in el_sub_statuses:
            if status in el_sub_status.text:
                el_sub_status.click()
                break

    def check_doughunt_charts(self, number):
        try:
            donuts = WebDriverWait(self.context.driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                        ".donut-item")))
        except TimeoutException:
            self.context.log.info("There are no donuts!")
            raise AssertionError

        el_donuts = self.context.driver.find_elements_by_css_selector(".donut-item")

        if len(el_donuts) != number:
            self.context.log.info("Quantity of donats is wrong!")
            raise AssertionError