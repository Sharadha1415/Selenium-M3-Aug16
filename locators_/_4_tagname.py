import time

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\files_\css_selector.html')
time.sleep(2)

driver.find_element('tag name', 'input').send_keys('Green')
time.sleep(1)
driver.find_element('tag name', 'input').send_keys('Red')


























