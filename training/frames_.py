'''
iframe  :   It is an inline frame.
            The application present inside some other application

            The tagname of an iframe is always "iframe"

            Steps to handle iframe
                *   Locate the frame
                *   Switch the driver to the frame
                    SYNTAX  :   driver.switch_to.frame(frame)
                *   Perform the operations inside the frame
                *   Once after performing the operations, switch back to the parent frame
                    SYNTAX  :   driver.switch_to.parent_frame()

'''
import time

# ## EG1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\files_\iframe.html')
# time.sleep(2)
#
# ## locating the frame
# frame1 = driver.find_element('xpath', '//iframe[@name="frame1"]')
#
# ## switch the driver to the frame
# driver.switch_to.frame(frame1)
#
# ## performing the operations inside the frame
# driver.find_element('xpath', '//input[@id="small-searchterms"]').send_keys('Books')
# time.sleep(2)
#
# ## switch back to the parent frame
# driver.switch_to.parent_frame()
#
# ## locate frame2
# frame2 = driver.find_element('xpath', '//iframe[@name="frame2"]')
#
# ## switch the driver to frame2
# driver.switch_to.frame(frame2)
# time.sleep(2)
#
# ## performing the operations inside the frame
# driver.find_element('xpath', '//input[@id="search_form"]').send_keys('Vehicle insurance')
#
# ## switch back to the parent frame
# driver.switch_to.parent_frame()

##############################################################################################################

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)
ac_obj = ActionChains(driver)

driver.get('https://www.linkedin.com')
time.sleep(2)

## locating the google frame
google_frame = driver.find_element('xpath', '//iframe[@title="Sign in with Google Button"]')

## switch the driver to the frame
driver.switch_to.frame(google_frame)
time.sleep(2)

## perform the operations on the google frame
driver.find_element('xpath', '//span[text()="Continue with Google"]').click()
time.sleep(2)

## switch back to the parent window
driver.switch_to.parent_frame()
time.sleep(2)

## scroll until youtube window is visible
ele = driver.find_element('xpath', '//h2[contains(text(), "Join your colleagues")]')
ac_obj.scroll_to_element(ele).perform()
time.sleep(2)

## locate youtube frame
youtube_frame = driver.find_element('xpath', '//iframe[@title="Gayatri Iyer: In it to chase my dream | #InItTogether"]')

## switch the driver to the youtube frame
driver.switch_to.frame(youtube_frame)

## perform the operations
driver.find_element('xpath', '//button[@title="Play"]').click()

























































