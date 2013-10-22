class LoginPage(object):
    def __init__(self, env, world):
        print("7 INIT OF PAGE OBJECT")
        print("8 WORLD IN PAGEOBJECT {0}".format(world))
        self.env = env
        self.driver = world.driver
        self.LoadPage()

    def LoadPage(self):
        self.driver.get(self.env["url"]+self.env['port'])

    def set_username(self, user):
        el_username = self.driver.find_element_by_name("username")
        el_username.send_keys(user)

    def set_password(self, password):
        el_password = self.driver.find_element_by_id("password")
        el_password.send_keys(password)


# Public interface
    def fill_in_credentials(self, user, pswd):
        self.set_username(user)
        self.set_password(pswd)

    def sign_in(self):
        el_login_button = self.driver.find_element_by_id("submitLogin")
        el_login_button.click()
