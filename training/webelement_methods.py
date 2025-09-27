'''

web-element methods :   To interact with the web-elements, we have web-element methods

There are 2 types of web-element methods
*   find_element    :   To find and to interact with the web-element, we have find_element
            SYNTAX  :   driver.find_element("locator_name", "locator_value")


*   find_elements   :   find_elements is a Selenium method used to locate multiple web elements on a page.
                        It returns a list of WebElement objects.
            SYNTAX  :   driver.find_elements("loc_name", "loc_value")


'''

###############################################################################################

'''
Locators    :   To locate the web-elements, we use locators

There are 8 types of locators
    *   id
    *   name
    *   class name
    *   tag name
    *   link text
    *   partial link text
    *   css selector
    *   xpath    

'''



'''
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

driver.find_element(By.ID, '')
driver.find_element(By.NAME, '')
driver.find_element(By.CLASS_NAME, '')


'''
































































