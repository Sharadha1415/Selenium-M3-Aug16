'''
Markers :   To group the testcases, we go for markers
There are 2 types of markers
    *   custom marker
    *   inbuilt marker  :   There are 4 types of inbuilt markers
                            *   skip
                            *   skipif
                            *   parametrize
                            *   xfail
'''

import pytest

# def test_login():
#     print("login executing")
#
# @pytest.mark.sanity
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.sanity
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="sanity"
# ## collected 4 items / 2 deselected / 2 selected
# ## test_markers.py::test_reg       reg executing           PASSED
# ## test_markers.py::test_signup    signup executing        PASSED

##############################################################################################################

# @pytest.mark.smoke
# def test_login():
#     print("login executing")
#
# @pytest.mark.sanity
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.regression
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.smoke
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="sanity"               --> test_reg will execute
# ## pytest test_markers.py -vs -m="smoke"                --> test_login and test_logout will execute
# ## pytest test_markers.py -vs -m="regression"           --> test_signup will execute
# ## pytest test_markers.py -vs -m="sanity and smoke"     --> collected 4 items / 4 deselected / 0 selected
# ## pytest test_markers.py -vs -m="sanity or smoke"      --> test_login, test_reg, test_logout will execute

##############################################################################################################

# @pytest.mark.sanity
# @pytest.mark.smoke
# def test_login():
#     print("login executing")
#
# @pytest.mark.regression
# @pytest.mark.sanity
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.regression
# def test_signup():
#     print("signup executing")
#
# @pytest.mark.sanity
# @pytest.mark.smoke
# def test_logout():
#     print("logout executing")
#
# ## In terminal
# ## pytest test_markers.py -vs -m="sanity"                   --> test_login, test_reg, test_logout will execute
# ## pytest test_markers.py -vs -m="smoke"                    --> test_login and test_logout will execute
# ## pytest test_markers.py -vs -m="regression"               --> test_reg and test_signup will execute
# ## pytest test_markers.py -vs -m="sanity and smoke"         --> test_login and test_logout will execute
# ## pytest test_markers.py -vs -m="sanity and regression"    --> test_reg will execute
# ## pytest test_markers.py -vs -m="smoke and regression"     --> 0
# ## pytest test_markers.py -vs -m="sanity or smoke"          --> test_login, test_reg, test_logout will execute
# ## pytest test_markers.py -vs -m="sanity or regression"     --> All 4 will execute
# ## pytest test_markers.py -vs -m="regression or smoke"      --> All 4 will execute
# ## pytest test_markers.py -vs -m="not smoke"                --> test_reg and test_signup will execute
# ## pytest test_markers.py -vs -m="not sanity"               --> test_signup will execute
# ## pytest test_markers.py -vs -m="not regression"           --> test_login and test_logout will execute

##############################################################################################################

# @pytest.mark.sanity
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## pytest test_markers.py -vs -m="sanity"   --> All 4 will execute

##############################################################################################################

# @pytest.mark.regression
# class TestSample:
#
#     @pytest.mark.sanity
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     @pytest.mark.smoke
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")

##############################################################################################################

'''
skip    :   To skip the execution of the testcase, we use skip marker
            It is an unconditional skip. 
            To skip the testcases, we dont have to pass any condition or reason.
            It will just skip the testcases which are decorated with @pytest.mark.skip
            Reason is a optional parameter
            
            SYNTAX  :   @pytest.mark.skip([reason=''])
                        def test_func():
                            pass
'''


# def test_login():
#     print("login executing")
#
# @pytest.mark.skip
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.skip
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::test_login     login executing         PASSED
# ## test_markers.py::test_reg                               SKIPPED (unconditional skip)
# ## test_markers.py::test_signup                            SKIPPED (unconditional skip)
# ## test_markers.py::test_logout    logout executing        PASSED

##############################################################################################################

# @pytest.mark.skip(reason="register completed")
# def test_reg():
#     print("reg executing")
#
# @pytest.mark.skip(reason="signup not necessary")
# def test_signup():
#     print("signup executing")
#
# ## collected 2 items
# ## test_markers.py::test_reg               SKIPPED (register completed)
# ## test_markers.py::test_signup            SKIPPED (signup not necessary)

##############################################################################################################

# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     @pytest.mark.skip
#     def test_reg(self):
#         print("reg executing")
#
#     @pytest.mark.skip
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::TestSample::test_login         login executing         PASSED
# ## test_markers.py::TestSample::test_reg                                   SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_signup                                SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_logout        logout executing        PASSED

##############################################################################################################

# @pytest.mark.skip
# class TestSample:
#
#     def test_login(self):
#         print("login executing")
#
#     def test_reg(self):
#         print("reg executing")
#
#     def test_signup(self):
#         print("signup executing")
#
#     def test_logout(self):
#         print("logout executing")
#
# ## collected 4 items
# ## test_markers.py::TestSample::test_login     SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_reg       SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_signup    SKIPPED (unconditional skip)
# ## test_markers.py::TestSample::test_logout    SKIPPED (unconditional skip)

##############################################################################################################
'''
skipif  :   skipif is also used to skip the execution of the testcases, but the skip is based on a condition.
            It takes two parameters, condition and reason.
            condition is the first parameter, reason is the second parameter.
            Both are mandatory parameters
            
            SYNTAX  :   @pytest.mark.skipif(condition, reason)
                        def test_case():
                            pass
                        
                        If the condition is True, it will skip the execution of the testcase
                        If the condition is False, it will execute the testcase 
            
'''

# @pytest.mark.skipif(10%2==0, reason='condition is True')
# def test_case1():
#     print("tc1 executing")
#
# ## collected 1 item
# ## test_markers.py::test_case1         SKIPPED (condition is True)

#####################################################################################################

# @pytest.mark.skipif(10%2!=0, reason='condition is True')
# def test_case1():
#     print("tc1 executing")
#
# ## collected 1 item
# ## test_markers.py::test_case1     tc1 executing       PASSED


#####################################################################################################

# @pytest.mark.skipif(10%2!=0)
# def test_case1():
#     print("tc1 executing")
#
# ## collected 1 item
# ## test_markers.py::test_case1         ERROR

#####################################################################################################

'''
xfail   :   This is an expected failure

            SYNTAX  :   @pytest.mark.xfail
                        def test_func():
                            pass  
                        
                        We are expecting the test_func to fail.
                        If the testcase is failed, then the output will be XFAIL
                        If the testcase is passed, then the output will be XPASS
'''

import time

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
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
# @pytest.mark.xfail
# def test_login():
#     driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
#     time.sleep(1)
#     driver.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauceeeee')
#     time.sleep(1)
#     driver.find_element('xpath', '//input[@id="login-button"]').click()
#     time.sleep(2)
#     wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//span[text()="Products"]')))


#####################################################################################################

# def test_case1():
#     print("tc1 executing")
#
# @pytest.mark.xfail
# def test_case2():
#     prit("tc2 executing")
#
# @pytest.mark.xfail
# def test_case3():
#     pri("tc3 executing")
#
# def test_case4():
#     raise Exception
#
# ## collected 4 items
# ## test_markers.py::test_case1     tc1 executing           PASSED
# ## test_markers.py::test_case2                             XFAIL
# ## test_markers.py::test_case3                             XFAIL
# ## test_markers.py::test_case4                             FAILED

#####################################################################################################

# @pytest.mark.xfail
# def test_case2():
#     print("tc2 executing")
#
# @pytest.mark.xfail
# def test_case3():
#     print("tc3 executing")
#
# ## collected 2 items
# ## test_markers.py::test_case2         tc2 executing       XPASS
# ## test_markers.py::test_case3         tc3 executing       XPASS

#####################################################################################################

'''
parametrize     :   To pass parameters for the testcases, we use parametrize markers  
'''

# @pytest.mark.parametrize('a, b', [(10, 20)])
# def test_add(a, b):
#     print(a + b)
#
# ## collected 1 item
# ## test_markers.py::test_add[10-20]        30          PASSED

##################################################################################################

# @pytest.mark.parametrize('a, b', [(1, 2), (100, 100), (100, -100), (10, 90), (-1, -2), (3, 5)])
# def test_add(a, b):
#     print(a + b)
#
# ## collected 6 items
# ## test_markers.py::test_add[1-2]          3           PASSED
# ## test_markers.py::test_add[100-100]      200         PASSED
# ## test_markers.py::test_add[100--100]     0           PASSED
# ## test_markers.py::test_add[10-90]        100         PASSED
# ## test_markers.py::test_add[-1--2]        -3          PASSED
# ## test_markers.py::test_add[3-5]          8           PASSED

























































