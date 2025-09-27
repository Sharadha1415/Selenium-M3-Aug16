import time

## Eg1
from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)
driver.find_element('partial link text', 'Regi').click()
time.sleep(2)
driver.find_element('partial link text', 'Log ').click()

#####################################################################################

## Eg2

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://www.kushals.com/')
time.sleep(2)
driver.find_element('partial link text', 'Accessories').click()


#####################################################################################

# ## Eg3
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
# driver.get('https://www.amazon.in/')
# time.sleep(2)
# driver.find_element('partial link text', 'Deals').click()
























