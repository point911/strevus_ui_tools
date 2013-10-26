from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage(object):
    def __init__(self, context):
        self.context = context
        context.page = self

    def logout(self):
        self.context.driver.get(self.context.env["url"]+self.context.env['port']+"logout")
        from .StrevusLoginPage import LoginPage
        self.context.page = LoginPage(self.context)

    def check_dashboard_page(self):

        try:
            el_dash = WebDriverWait(self.context.driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                                                  ".dashboard-home")))
            # if not el_dash.is_displayed():
        except TimeoutException:
            self.context.log.info("No dashboard is presented.")
            raise AssertionError


