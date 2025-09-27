# def login():
#     print("login executing")
#
# def logout():
#     print("logout executing")
#
# login()
# logout()
#
# ## To execute the function, we have to call the function
#
# ####################################################################################################
#
# class Sample:
#
#     def login(self):
#         print("login executing")
#
#     def logout(self):
#         print("logout executing")
#
# s_obj = Sample()
# s_obj.login()
# s_obj.logout()

# ####################################################################################################

'''
Pytest  :   Pytest is a unit-testing framework
            Testing the small portion of the entire program is Unit-testing
            To perform unit-testing in selenium, we use Pytest

            To install pytest
            Go to command prompt    --> pip install pytest

            RULES
            *   filename should always start with test_ or end with _test
                Eg  :   test_filename.py        OR          filename_test.py
            *   function names should start with test_
                Eg  :   def test_funcname():
                            pass
            *   class name should start with Test
                Eg  :   class TestClassName:
                            pass

            When we follow the pytest rules, pytest will automatically recognize the functions, classes, files
            which are following the pytest rules.
            So, we can execute the functions, classes without calling them

            To execute the pytest files
            Right click anywhere on the test_file --> open in --> terminal --> pytest test_filename.py -vs
                -v  --> Verbosity.  This gives the detailed explanation of the code
                -s  --> Scripting.  This will print all the print statements

'''
import time

# def test_login():
#     print("login executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 2 items
# ## test_basics.py::test_login      login executing         PASSED
# ## test_basics.py::test_logout     logout executing        PASSED

############################################################################################

# def test_login():
#     print("login executing")
#
# def signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 2 items
# ## test_basics.py::test_login      login executing         PASSED
# ## test_basics.py::test_logout     logout executing        PASSED

'''
signup will not execute because it is not following the pytest rule.
pytest cannot recognize the functions which are not following the rules
'''

############################################################################################

# def test_login():
#     print("login executing")
#     def test_signup():
#         print("signup executing")
#
# ## collected 1 item
# ## test_basics.py::test_login      login executing             PASSED

'''
Whenever we have nested test_functions, pytest cannot recognize the inner test_function.
It can recognize only the outer test_function
'''

############################################################################################

# def test_login():
#     raise Exception
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# ## collected 3 items
# ## test_basics.py::test_login                              FAILED
# ## test_basics.py::test_signup     signup executing        PASSED
# ## test_basics.py::test_logout     logout executing        PASSED

'''
NOTE    :   Error in one testcase will not affect the execution of the other testcases 
'''

############################################################################################

# def test_login():
#     print("login executing")
#
# def test_signup():
#     print("signup executing")
#
# def test_logout():
#     print("logout executing")
#
# test_login()
# test_signup()
# test_logout()
#
# ## collecting ... login executing
# ## signup executing
# ## logout executing
# ## collected 3 items
# ## test_basics.py::test_login      login executing         PASSED
# ## test_basics.py::test_signup     signup executing        PASSED
# ## test_basics.py::test_logout     logout executing        PASSED

'''
NOTE    :   When we call the test_functions, the execution will happen twice
'''

############################################################################################

# def test_add(a, b):
#     print(a + b)
#
# test_add(1, 2)
#
# ## collected 1 item
# ## test_basics.py::test_add            ERROR

'''
NOTE    :   test_functions donot take any parameters
'''

############################################################################################

# def test_login():
#     print("hello world")
#
# def test_login():
#     print("hello universe")
#
# ## collected 1 item
# ## test_basics.py::test_login          hello universe          PASSED

'''
NOTE    :   If we are having multiple test functions with the same test function name, pytest will always consider 
the latest occurance
'''

############################################################################################

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
# ## test_basics.py::TestSample::test_login      login executing         PASSED
# ## test_basics.py::TestSample::test_signup     signup executing        PASSED
# ## test_basics.py::TestSample::test_logout     logout executing        PASSED


############################################################################################
#
# class Sample:
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
# ## collected 0 items

'''
classname is not following the pytest rules
'''
############################################################################################

# class TestSample:
#
#     def login(self):
#         print("login executing")
#
#     def signup(self):
#         print("signup executing")
#
#     def logout(self):
#         print("logout executing")
#
# ## collected 0 items

'''
test_methods are not following the pytest rules
'''

############################################################################################
#
# class TestSample:
#
#     name = 'Atharva'
#
#     def test_greet(self):
#         print(f"Hello {self.name}, Welcome to India")
#
# ## collected 1 item
# ## test_basics.py::TestSample::test_greet      Hello Atharva, Welcome to India             PASSED

############################################################################################

# class TestSample:
#
#     def test_greet(self, name):
#         print(f"Hello {name}, Welcome to India")
#
# ## collected 1 item
# ## test_basics.py::TestSample::test_greet          ERROR

############################################################################################

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
#
# s_obj = TestSample()
# s_obj.test_login()
# s_obj.test_signup()
# s_obj.test_logout()
#
# ## collecting ... login executing
# ## signup executing
# ## logout executing
# ## collected 3 items
# ## test_basics.py::TestSample::test_login      login executing         PASSED
# ## test_basics.py::TestSample::test_signup     signup executing        PASSED
# ## test_basics.py::TestSample::test_logout     logout executing        PASSED

############################################################################################

# class TestSample:
#
#     def __init__(self):
#         pass
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
# ## collected 0 items
# ## PytestCollectionWarning: cannot collect test class 'TestSample' because it has a __init__ constructor

############################################################################################

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

class TestRegister:

    def test_reg_link(self):
        driver.find_element('xpath', '//a[text()="Register"]').click()
        time.sleep(2)

    def test_gender_btn(self):
        driver.find_element('xpath', '//input[@id="gender-female"]').click()

    def test_fname(self):
        driver.find_element('xpath', '//input[@id="FirstName"]').send_keys('Shailaja')

    def test_lname(self):
        driver.find_element('xpath', '//input[@id="LastName"]').send_keys('Aralikatti')

    def test_reg_email(self):
        driver.find_element('xpath', '//input[@id="Email"]').send_keys('shailaja@gmail.com')

    def test_reg_pwd(self):
        driver.find_element('xpath', '//input[@id="Password"]').send_keys('shailaja@12345')

    def test_confirm_pwd(self):
        driver.find_element('xpath', '//input[@id="ConfirmPassword"]').send_keys('shailaja@12345')
        time.sleep(2)


class TestLogin:

    def test_login_link(self):
        driver.find_element('xpath', '//a[text()="Log in"]').click()
        time.sleep(2)

    def test_login_email(self):
        driver.find_element('xpath', '//input[@id="Email"]').send_keys('shailaja@gmail.com')

    def test_login_pwd(self):
        driver.find_element('xpath', '//input[@id="Password"]').send_keys('shailaja@12345')






















