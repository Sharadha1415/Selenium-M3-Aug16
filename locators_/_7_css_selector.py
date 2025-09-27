'''
css selector    :   To locate the web-elements using any attribute, we go for css selector
                    SYNTAX  :   tagname[attr_name="attr_value"]

                    DRAWBACKS
                    *   Indexing is not possible
                        In case of multiple occurences, css selector will always consider the first occurance
                    *   Cannot locate text using css selector
                    *   Back-traversing is not possible

'''
import time


## Eg1

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# driver.find_element('css selector', 'input[placeholder="Username"]').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('css selector', 'input[placeholder="Password"]').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('css selector', 'input[id="login-button"]').click()
# time.sleep(3)
# driver.find_element('css selector', 'button[id="react-burger-menu-btn"]').click()
# time.sleep(2)
# driver.find_element('css selector', 'a[id="logout_sidebar_link"]').click()

###################################################################################################

# ## Eg2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\files_\css_selector.html')
# time.sleep(2)
#
# driver.find_element('css selector', 'input[class="first_row"]').send_keys('Hashmath')
# time.sleep(1)
# driver.find_element('css selector', 'input[class="first_row"]').send_keys('Shailaja')
#
# ## Both the values will be filled in the same textbox.
# ## Because if we are multiple occurances, css selector will always consider the first occurance

###################################################################################################

# ## Eg3
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
# driver.find_element('css selector', 'input[name="firstname"]').send_keys('Harry')
# time.sleep(1)
# driver.find_element('css selector', 'input[name="lastname"]').send_keys('Potter')
# time.sleep(1)
# driver.find_element('css selector', 'input[name="reg_email__"]').send_keys('harry@gmail.com')
# time.sleep(1)
# driver.find_element('css selector', 'input[name="reg_passwd__"]').send_keys('harry@12345')



































