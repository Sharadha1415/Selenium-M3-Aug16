'''
class name  :   If we have "class" attribute, then we can go for "class name" locator

                DRAWBACKS
                *   class name locator cannot locate the spaces.
                *   class is not unique.
                    Multiple elements can have same class attribute and same value
                *   Incase of multiple occurances, class name always considers the first occurance


'''

import time

## EG1
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

driver.find_element('class name', 'ico-register').click()
time.sleep(2)
driver.find_element('class name', 'ico-login').click()
time.sleep(2)
driver.find_element('class name', 'ico-cart').click()

##########################################################################################

## Eg2

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.saucedemo.com/')
time.sleep(2)
driver.find_element('class name', 'input_error form_input').send_keys('standard_user')

## NoSuchElementException
## Because the class value is having space in it. class name locator cannot recognize the spaces

#-----------------------------------------------------------------------------------------

## To overcome the above drawback

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.saucedemo.com/')
time.sleep(2)
driver.find_element('class name', 'input_error.form_input').send_keys('standard_user')

##########################################################################################

import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\files_\css_selector.html')
time.sleep(2)

driver.find_element('class name', 'first_row').send_keys('Deeksha')
time.sleep(1)
driver.find_element('class name', 'first_row').send_keys('Hashmath')

## Both the values will be filled in the same textbox










































