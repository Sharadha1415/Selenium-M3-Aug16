# import time
# import pytest
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# @pytest.fixture(scope='class')
# def setup():
#     driver = webdriver.Chrome(opts)
#     driver.get('https://demowebshop.tricentis.com/')
#     time.sleep(2)
#     yield driver
#     driver.close()
#
# class TestLogin:
#
#     def test_login_link(self, setup):
#         setup.find_element('xpath', '//a[text()="Log in"]').click()
#         time.sleep(2)
#
#     def test_login_email(self, setup):
#         setup.find_element('xpath', '//input[@id="Email"]').send_keys('shailaja@gmail.com')
#
#     def test_login_pwd(self, setup):
#         setup.find_element('xpath', '//input[@id="Password"]').send_keys('shailaja@12345')
#
############################################################################################################

import time

class TestLogin:

    def test_login_link(self, setup):
        setup.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(2)

    def test_login_email(self, setup):
        setup.find_element('xpath', '//input[@id="Email"]').send_keys('shailaja@gmail.com')

    def test_login_pwd(self, setup):
        setup.find_element('xpath', '//input[@id="Password"]').send_keys('shailaja@12345')
























