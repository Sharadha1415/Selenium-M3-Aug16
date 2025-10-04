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
# class TestRegister:
#
#     def test_reg_link(self, setup):
#         setup.find_element('xpath', '//a[text()="Register"]').click()
#         time.sleep(2)
#
#     def test_gender_btn(self, setup):
#         setup.find_element('xpath', '//input[@id="gender-female"]').click()
#
#     def test_fname(self, setup):
#         setup.find_element('xpath', '//input[@id="FirstName"]').send_keys('Shailaja')
#
#     def test_lname(self, setup):
#         setup.find_element('xpath', '//input[@id="LastName"]').send_keys('Aralikatti')
#
#     def test_reg_email(self, setup):
#         setup.find_element('xpath', '//input[@id="Email"]').send_keys('shailaja@gmail.com')
#
#     def test_reg_pwd(self, setup):
#         setup.find_element('xpath', '//input[@id="Password"]').send_keys('shailaja@12345')
#
#     def test_confirm_pwd(self, setup):
#         setup.find_element('xpath', '//input[@id="ConfirmPassword"]').send_keys('shailaja@12345')
#         time.sleep(2)

############################################################################################################

import time

class TestRegister:

    def test_reg_link(self, setup):
        setup.find_element('xpath', '//a[text()="Register"]').click()
        time.sleep(2)

    def test_gender_btn(self, setup):
        setup.find_element('xpath', '//input[@id="gender-female"]').click()

    def test_fname(self, setup):
        setup.find_element('xpath', '//input[@id="FirstName"]').send_keys('Shailaja')

    def test_lname(self, setup):
        setup.find_element('xpath', '//input[@id="LastName"]').send_keys('Aralikatti')

    def test_reg_email(self, setup):
        setup.find_element('xpath', '//input[@id="Email"]').send_keys('shailaja@gmail.com')

    def test_reg_pwd(self, setup):
        setup.find_element('xpath', '//input[@id="Password"]').send_keys('shailaja@12345')

    def test_confirm_pwd(self, setup):
        setup.find_element('xpath', '//input[@id="ConfirmPassword"]').send_keys('shailaja@12345')
        time.sleep(2)



















