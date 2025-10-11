'''
Synchronization :   Matching the speed of the webdriver to the speed of the application.

There are 2 types of synchronization
*   unconditional synchronization   :   No conditions are passed.
        We achieve unconditional synchronization by passing time.sleep(n).
        Unnecessary wait is too much in unconditional synchronization

*   conditional synchronization     :   Conditions are passed
        There are 2 types
        *   implicit_wait   :   Conditions are internally taken.
                                SYNTAX  :   driver.implicitly_wait(n)
                                implicit_wait will make the driver wait until the element is available on the application.
                                As soon as the element is available, it will start performing the operations right away.
                                No unnecessary wait time

        *   explicit_wait   :   We pass the conditions externally.

                                from selenium.webdriver.support.ui import WebDriverWait
                                from selenium.webdriver.support import expected_conditions
                                    WebDriverWait --> class
                                    expected_conditions --> module

                                wait_obj = WebDriverWait(driver, timeouttime)


            Web pages often load asynchronously
            Elements may not be immediately available → leading to NoSuchElementException or ElementNotInteractableException.
            WebDriverWait ensures the element is ready before interacting

            Implicit Wait
                Applied globally
                Waits for element presence only
                Less flexible

            WebDriverWait (Explicit Wait)
                Applied only to specific elements
                Waits for multiple conditions
                More powerful & precise

        WebDriverWait   :   It allows the driver to wait for a certain condition to check before we continue the operation.
                            Instead of waiting for a fixed amount of time, it waits until a condition is True or maximum time is reached.

        expected_conditions :   The conditions to be applied on the web-elements are already pre-defined and they are defined in expected_conditions.py
                            To make use of the pre-defined conditions we import expected_conditions

        until()         :   It is a method of WebDriverWait
                            It checks whether the given condition is satisfied or not
                            If the condition is True, it will continue the operations.
                            If the condition is False, it will always gives TimeOutException


'''

import time

## Unconditional synchronization
# ## time.sleep()
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\files_\loading.html')
# time.sleep(20)
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Harry')
# time.sleep(1)
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('Potter')

# #############################################################################################
#
# ## implicit_wait
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.implicitly_wait(30)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\files_\loading.html')
#
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Harry')
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('Potter')


#############################################################################################

# ## explicit_wait

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_obj = WebDriverWait(driver, 30)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\files_\loading.html')
#
# wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//div[contains(text(), "FirstName")]')))
#
# driver.find_element('xpath', '//input[@name="fname"]').send_keys('Harry')
# driver.find_element('xpath', '//input[@name="lname"]').send_keys('Potter')

#############################################################################################

# ## explicit_wait

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# wait_obj = WebDriverWait(driver, 20)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="password"]').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('xpath', '//input[@id="login-button"]').click()
# time.sleep(2)
#
# # try:
# #     wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//span[text()="Products"]')))
# #     print("Succesfull login")
# # except:
# #     print("Unsucessfull login")
#
# ##
# try:
#     wait_obj.until(expected_conditions.url_contains('inventory'))
#     print("Succesfull login")
# except:
#     print("Unsuccesfull login")

# #############################################################################################
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\files_\progressbar.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Click Me"]').click()
# time.sleep(45)
# driver.find_element('xpath', '//button[text()="Click Me"]').click()

# #############################################################################################
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.implicitly_wait(50)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\files_\progressbar.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Click Me"]').click()
# driver.find_element('xpath', '//div[text()="100%"]')
# time.sleep(1)
# driver.find_element('xpath', '//button[text()="Click Me"]').click()

#############################################################################################

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
wait_obj = WebDriverWait(driver, 50)

driver.get(r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\files_\progressbar.html')
time.sleep(2)

driver.find_element('xpath', '//button[text()="Click Me"]').click()
wait_obj.until(expected_conditions.visibility_of_element_located(('xpath', '//div[text()="100%"]')))
driver.find_element('xpath', '//button[text()="Click Me"]').click()

































