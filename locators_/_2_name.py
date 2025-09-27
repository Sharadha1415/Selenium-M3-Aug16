'''
name    :   It is a attribute which is also a locator
            If we have name attribute, we can go for name locator

            name is not unique.
            Multiple elements can have same name attribute and same value
            Incase of multiple occurances, name locator will always consider the first occurance

'''

import time

# ## Eg1
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.instagram.com/')
# time.sleep(2)
# driver.find_element('name', 'username').send_keys('sherlock_holmes')
# time.sleep(1)
# driver.find_element('name', 'password').send_keys('sherlock@123456')

######################################################################################
# ## EG2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# driver.find_element('name', 'firstname').send_keys('Sherlock')
# time.sleep(1)
# driver.find_element('name', 'lastname').send_keys('Holmes')
# time.sleep(1)
# driver.find_element('name', 'reg_email__').send_keys('sherlock@gmail.com')
# time.sleep(1)
# driver.find_element('name', 'reg_passwd__').send_keys('sherlock@12345')

######################################################################################

## EG3

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\files_\css_selector.html')
time.sleep(2)
driver.find_element('name', 'fname').send_keys('Green')
time.sleep(1)
driver.find_element('name', 'fname').send_keys('red')

## Both the values will be filled in the first checkbox only.
## When multiple elements have same attribute name and value, it will always consider the first occurance






































