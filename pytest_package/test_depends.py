'''
Dependency  :   We can create the dependencies between the testcases.
                One testcase can be dependent on other testcases.

                SYNTAX  :   @pytest.mark.dependency()               ## Independent testcase
                            def test_func1():
                                pass

                            @pytest.mark.dependency(depends=['test_func1'])         ## Dependent testcase
                            def test_func2():
                                pass

                            test_func2 is dependent on test_func1

                            If the independent testcase executes without any error, then dependent also executes without any error
                            If independent testcase itself is not working fine, then the dependent testcase will be skipped


'''

import time
import pytest

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_obj = WebDriverWait(driver, 5)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# @pytest.mark.dependency()               ## Independent testcase
# def test_login():
#     driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
#     driver.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauceeeeee')
#     driver.find_element('xpath', '//input[@id="login-button"]').click()
#     time.sleep(2)
#     wait_obj.until(EC.visibility_of_element_located(('xpath', '//span[text()="Products"]')))
#
#
# @pytest.mark.dependency(depends=['test_login'])
# def test_logout():
#     driver.find_element('xpath', '//button[@id="react-burger-menu-btn"]').click()
#     time.sleep(2)
#     driver.find_element('xpath', '//a[@id="logout_sidebar_link"]').click()

###############################################################################################################

# @pytest.mark.dependency()
# def test_login():
#     print("login executing")
#
# @pytest.mark.dependency(depends=["test_login"])
# def test_logout():
#     print("logout executing")
#
# ## collected 2 items
# ## test_depends.py::test_login     login executing         PASSED
# ## test_depends.py::test_logout    logout executing        PASSED

###############################################################################################################

# @pytest.mark.dependency()
# def test_login():
#     raise Exception
#
# @pytest.mark.dependency(depends=["test_login"])
# def test_logout():
#     print("logout executing")
#
# ## collected 2 items
# ## test_depends.py::test_login         FAILED
# ## test_depends.py::test_logout        SKIPPED (test_logout depends on test_login)

###############################################################################################################

# @pytest.mark.dependency()
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.dependency(depends=["test_reg"])
# def test_login():
#     print("login executing")
#
# @pytest.mark.dependency(depends=["test_reg"])
# def test_logout():
#     print("logout executing")

'''
NOTE    :   We can have one independent and multiple dependent testcases
            If the independent testcase executes without any error, then dependent also executes without any error
            If the independent testcase fails, then the dependent testcase will be skipped
'''

###############################################################################################################

# @pytest.mark.dependency()
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.dependency()
# def test_login():
#     print("login executing")
#
# @pytest.mark.dependency(depends=["test_reg", "test_login"])
# def test_logout():
#     print("logout executing")
#
# ## collected 3 items
# ## test_depends.py::test_reg       reg executing           PASSED
# ## test_depends.py::test_login     login executing         PASSED
# ## test_depends.py::test_logout    logout executing        PASSED

###############################################################################################################

# @pytest.mark.dependency()
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.dependency()
# def test_login():
#     prt("login executing")
#
# @pytest.mark.dependency(depends=["test_reg", "test_login"])
# def test_logout():
#     print("logout executing")
#
# ## collected 3 items
# ## test_depends.py::test_reg       reg executing       PASSED
# ## test_depends.py::test_login                         FAILED
# ## test_depends.py::test_logout                        SKIPPED (test_logout depends on test_login)

'''
NOTE    :   We can have one dependent testcase dependent on multiple independent testcases
            If all the independent testcases works fine, then dependent testcase also works fine
            If any one of the independent testcases fails, the dependent testcase will be skipped 
'''

###############################################################################################################

# class TestSample:
#
#     @pytest.mark.dependency()
#     def test_login(self):
#         print("login executing")
#
#     @pytest.mark.dependency(depends=["test_login"])
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 2 items
# ## test_depends.py::TestSample::test_login     login executing         PASSED
# ## test_depends.py::TestSample::test_logout                            SKIPPED (test_logout depends on test_login)

'''
In the above scenario, pytest will look for test_login testcase in the global area(outside the class)
There is no test_login outside the class, so it is skipped

'''

###############################################################################################################

# class TestSample:
#
#     @pytest.mark.dependency()
#     def test_login(self):
#         print("login executing")
#
#     @pytest.mark.dependency(depends=["TestSample::test_login"])
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 2 items
# ## test_depends.py::TestSample::test_login     login executing     PASSED
# ## test_depends.py::TestSample::test_logout    logout executing    PASSED

###############################################################################################################

class TestSample:

    @pytest.mark.dependency()
    def test_login(self):
        print("login executing")


class TestExample:

    @pytest.mark.dependency(depends=["TestSample::test_login"])
    def test_logout(self):
        print("logout executing")










































