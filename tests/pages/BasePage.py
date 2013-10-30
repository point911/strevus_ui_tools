import imp


class BasePage(object):
    def __init__(self, context):
        self.context = context

    def logout(self):
        self.context.driver.get(self.context.env["url"]+self.context.env['port']+"logout")
        LoginPage = imp.load_source('LoginPage', './pages/StrevusLoginPage.py')
        #from .StrevusLoginPage import LoginPage
        self.context.page = LoginPage.LoginPage(self.context)
        self.context.page.check_login_page()