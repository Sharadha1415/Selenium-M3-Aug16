import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://demowebshop.tricentis.com/')
time.sleep(2)

driver.find_element('xpath', '//a[text()="Register"]').click()
time.sleep(2)
driver.find_element('xpath', '//input[@id="gender-female"]').click()
driver.find_element('xpath', '//input[@id="FirstName"]').send_keys('Shailaja')
driver.find_element('xpath', '//input[@id="LastName"]').send_keys('Aralikatti')
driver.find_element('xpath', '//input[@id="Email"]').send_keys('shailaja@gmail.com')
driver.find_element('xpath', '//input[@id="Password"]').send_keys('shailaja@12345')
driver.find_element('xpath', '//input[@id="ConfirmPasswordddd"]').send_keys('shailaja@12345')
time.sleep(2)

driver.find_element('xpath', '//a[text()="Log in"]').click()
time.sleep(2)
driver.find_element('xpath', '//input[@id="Email"]').send_keys('shailaja@gmail.com')
driver.find_element('xpath', '//input[@id="Passworddd"]').send_keys('shailaja@12345')
