class BasePage(object):
    def __init__(self, context):
        self.context = context

    def logout(self):
        self.context.driver.get(self.context.env["url"]+self.context.env['port']+"logout")
        from .StrevusLoginPage import LoginPage
        self.context.page = LoginPage(self.context)
        self.context.page.check_login_page()