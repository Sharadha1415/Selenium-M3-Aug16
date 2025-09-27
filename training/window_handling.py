'''
In web automation, sometimes actions open a new browser window or tab (e.g., clicking a link, pop-up, advertisement, or login window).
Selenium initially controls only the main window where the driver started.
To interact with other windows/tabs, we need to switch between them.

Window Handles
    Every window or tab opened by the browser has a unique ID, called a window handle.
    Selenium provides methods to get and switch between these handles.
    handles = driver.window_handles     ## Returns a list of handles for all open windows/tabs.

    To switch the driver to the window
    driver.switch_to.window(handles[index_num])

'''
import time

# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# ac_obj = ActionChains(driver)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# handles1 = driver.window_handles
# print(handles1)
#
# ## scroll down till the end of the application
# ac_obj.send_keys(Keys.END).perform()
# time.sleep(2)
#
# ## click on google+
# driver.find_element('xpath', '//a[text()="Google+"]').click()       ## opens in new tab
# time.sleep(2)
#
# handles2 = driver.window_handles
# print(handles2)         ## [parent_handle, child_handle]
#
# ## switch the driver to the child handle
# driver.switch_to.window(handles2[1])
# time.sleep(2)
#
# ## entering the data to the search blog
# driver.find_element('xpath', '//input[@placeholder="Search blog"]').send_keys('Google pixel 10')
# time.sleep(2)

###########################################################################################################


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)
opts.add_argument("--disable-notifications")

driver = webdriver.Chrome(opts)

ac_obj = ActionChains(driver)

driver.get('https://www.myntra.com/')
time.sleep(2)

## hover the cursor to the Home
home = driver.find_element('xpath', '//a[text()="Home"]')
ac_obj.move_to_element(home).perform()
time.sleep(2)

## click on wall decor
driver.find_element('xpath', '//a[text()="Wall Décor"]').click()
time.sleep(2)

## clicking on one product
driver.find_element('xpath', '//h4[@class="product-product"]').click()      ## opens in a new tab
time.sleep(2)

## Initialize the window_handles
handles1 = driver.window_handles
print(handles1)         ## [parent_handle, child_handle]

## switch the driver to the child handle
driver.switch_to.window(handles1[1])
time.sleep(2)

## adding the product to the bag
driver.find_element('xpath', '//div[text()="ADD TO BAG"]').click()
time.sleep(2)

## switch back to the parent_window
driver.switch_to.window(handles1[0])
time.sleep(2)

## clicking on one more product
driver.find_element('xpath', '(//h4[@class="product-product"])[2]').click()     ## opens in new tab
time.sleep(2)

## initializing the window_handles
handles2 = driver.window_handles
print(handles2)         ## [parent, child1, child2]

## switching the driver to the child2
driver.switch_to.window(handles2[2])
time.sleep(2)

## adding the product to the bag
driver.find_element('xpath', '//div[text()="ADD TO BAG"]').click()
time.sleep(2)



















































