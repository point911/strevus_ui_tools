__author__ = 'point'

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestStrevusLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS('/usr/local/bin/phantomjs')
        self.driver.get('http://localhost:1025/')

    def testTitle(self):
        self.assertIn('Strevus', self.driver.title)

    def testLogIn(self):
        username = self.driver.find_element_by_name("username")
        username.send_keys("fred@fd.com")
        password = self.driver.find_element_by_id("password")
        password.send_keys("pswd")
        button = self.driver.find_element_by_id("submitLogin")
        button.click()
        time.sleep(1)
        print(self.driver.current_url)
        #self.driver.execute_script("data-main")
        #self.driver.close()
        #time.sleep(1)
        #print(self.driver.title)


        #print(login_promt.send_keys("test@email"))
        #print(login_promt.send_keys(Keys.RETURN))


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)

