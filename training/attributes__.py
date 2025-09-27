'''
get_attribute() :   get_attribute() is a Selenium WebDriver method used to fetch the value of an attribute of a web element.
                    It returns the string value of the attribute.
                    SYNTAX  :   web_element.get_attribute("attr_name")

'''

import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.myntra.com/')
time.sleep(2)

home = driver.find_element('xpath', '(//a[text()="Home"])[1]')
print(home.get_attribute('href'))
print(home.get_attribute('data-color'))


############################################################################################################

'''
text    :   .text is a Selenium WebElement property that returns the visible (inner) text of an element.
            It only returns what is rendered on the page and visible to the user.
            SYNTAX  :   web_element.text
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.myntra.com/')
# time.sleep(2)
#
# home = driver.find_element('xpath', '//a[@data-group="home"]')
# print(home.text)
#
# beauty = driver.find_element('xpath', '//a[@data-group="beauty"]')
# print(beauty.text)





















