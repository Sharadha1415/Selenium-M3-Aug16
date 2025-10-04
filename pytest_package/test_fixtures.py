# def outer(func):
#     def wrapper(*args, **kwargs):
#         print("Good morning")
#         func(*args, **kwargs)
#     return wrapper
#
# @outer
# def add(a, b):
#     print(a + b)
#
# add(10, 20)
# add(1, 2)
#
# #####################################################################################

import pytest


# @pytest.fixture()
# def greet():
#     print("Good morning")
#
# def test_login(greet):
#     print("login executing")
#
# def test_logout(greet):
#     print("logout executing")
#
# ## collected 2 items
# ## test_fixtures.py::test_login    Good morning        login executing     PASSED
# ## test_fixtures.py::test_logout   Good morning        logout executing    PASSED

##########################################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")
#
# def test_login(greet):
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout(greet):
#     print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login    Good morning        login executing     PASSED
# ## test_fixtures.py::test_signup                       signup executing    PASSED
# ## test_fixtures.py::test_logout   Good morning        logout executing    PASSED
#
# ## Fixture is not applied for test_signup

##########################################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")           ## setup
#     yield
#     print("Good evening")           ## teardown
#
# def test_login(greet):
#     print("login executing")
#
# def test_signup(greet):
#     print("signup executing")
#
# def test_logout(greet):
#     print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login    Good morning        login executing     PASSEDGood evening
# ## test_fixtures.py::test_signup   Good morning        signup executing    PASSEDGood evening
# ## test_fixtures.py::test_logout   Good morning        logout executing    PASSEDGood evening

'''
The operations before yield will execute before the execution of the test function
The operations after yield will execute after the execution of the test function

'''

##########################################################################################

# @pytest.fixture(autouse=True)
# def greet():
#     print("Good morning")           ## setup
#     yield
#     print("Good evening")           ## teardown
#
# def test_login():
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login    Good morning        login executing         PASSEDGood evening
# ## test_fixtures.py::test_signup   Good morning        signup executing        PASSEDGood evening
# ## test_fixtures.py::test_logout   Good morning        logout executing        PASSEDGood evening

##########################################################################################

# @pytest.fixture()
# def greet():
#     print("Good morning")           ## setup
#     yield
#     print("Good evening")           ## teardown
#
#
# class TestSample:
#
#     def test_login(self, greet):
#         print("login executing")
#
#     def test_signup(self, greet):
#         print("signup executing")
#
#     def test_logout(self, greet):
#         print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login    Good morning        login executing         PASSEDGood evening
# ## test_fixtures.py::test_signup   Good morning        signup executing        PASSEDGood evening
# ## test_fixtures.py::test_logout   Good morning        logout executing        PASSEDGood evening

# ##########################################################################################
#
# @pytest.fixture(autouse=True)
# def greet():
#     print("Good morning")           ## setup
#     yield
#     print("Good evening")           ## teardown
#
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::test_login    Good morning        login executing         PASSEDGood evening
# ## test_fixtures.py::test_signup   Good morning        signup executing        PASSEDGood evening
# ## test_fixtures.py::test_logout   Good morning        logout executing        PASSEDGood evening


##########################################################################################

# @pytest.fixture(autouse=True, scope='class')
# def greet():
#     print("Good morning")           ## setup
#     yield
#     print("Good evening")           ## teardown
#
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 3 items
# ## test_fixtures.py::TestSample::test_login    Good morning        login executing     PASSED
# ## test_fixtures.py::TestSample::test_signup                       signup executing    PASSED
# ## test_fixtures.py::TestSample::test_logout                       logout executing    PASSEDGood evening

##########################################################################################

# @pytest.fixture(scope='class')
# def greet():
#     print("Good morning")           ## setup
#     yield
#     print("Good evening")           ## teardown
#
# class TestSample:
#
#     def test_login(self, greet):
#         print("login executing")
#
#     def test_signup(self, greet):
#         print("signup executing")
#
#
# class TestExample:
#
#     def test_reg(self, greet):
#         print("reg executing")
#
#     def test_logout(self, greet):
#         print("logout executing")
#
# ## collected 4 items
# ## test_fixtures.py::TestSample::test_login    Good morning        login executing     PASSED
# ## test_fixtures.py::TestSample::test_signup                       signup executing    PASSEDGood evening
# ## test_fixtures.py::TestExample::test_reg     Good morning        reg executing       PASSED
# ## test_fixtures.py::TestExample::test_logout                      logout executing    PASSEDGood evening

##########################################################################################

# @pytest.fixture(autouse=True, scope='module')
# def greet():
#     print("Good morning")           ## setup
#     yield
#     print("Good evening")           ## teardown
#
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_signup(self):
#         print("signup executing")
#
# class TestExample:
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 4 items
# ## test_fixtures.py::TestSample::test_login    Good morning        login executing     PASSED
# ## test_fixtures.py::TestSample::test_signup                       signup executing    PASSED
# ## test_fixtures.py::TestExample::test_reg                         reg executing       PASSED
# ## test_fixtures.py::TestExample::test_logout                      logout executing    PASSEDGood evening

##########################################################################################
import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

@pytest.fixture(scope='class')
def setup():
    driver = webdriver.Chrome(opts)
    driver.get('https://demowebshop.tricentis.com/')
    time.sleep(2)
    yield driver
    driver.close()

## setup --> webdriver.Chrome(opts)
## driver -> webdriver.Chrome(opts)

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

class TestLogin:

    def test_login_link(self, setup):
        setup.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(2)

    def test_login_email(self, setup):
        setup.find_element('xpath', '//input[@id="Email"]').send_keys('shailaja@gmail.com')

    def test_login_pwd(self, setup):
        setup.find_element('xpath', '//input[@id="Password"]').send_keys('shailaja@12345')


























