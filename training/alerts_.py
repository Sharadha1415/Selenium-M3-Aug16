'''
Alerts  :   Alerts are not inspectable.
            Suppose if we are able to inspect, then it is not an alert.

            To handle the alerts, we will switch the driver to the alert
            SYNTAX  :   alert_obj = driver.switch_to.alert
                        alert_obj has two attributes to handle the alert
                        *   accept()    :   To accept the alert, we use alert_obj.accept()
                        *   dismiss()   :   To dismiss the alert, we use alert_obj.dismiss()

            There are different types alerts
            *   simple alert    :   If the alert is having only one option, then it is a simple alert.
                                    To handle the simple alert, first switch the driver to the alert
                                    Now we can either use accept or dismiss.
                                    alert_obj.accept()  or      alert_obj.dismiss()

            *   confirmation alert  :   If the alert is having two options, then it is a confirmation alert.
                                    To handle the confirmation alert, first switch the driver to the alert
                                    To click on OK/YES/AGREE,.. we give alert_obj.accept()
                                    To click on CANCEL/NO/DISAGREE,.. we give alert_obj.dismiss()

            *   Prompt alert    :   Here the alert will take the data from the user.
                                    To handle the prompt alert, first switch the driver to the alert
                                    alert_obj.send_keys("data")
                                    alert_obj.accept()



'''
import time

# ## Confirmation alert
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Confirmation Alert"]').click()       ## gives an alert
# time.sleep(2)
#
# ## switch the driver to the alert
# alert_obj = driver.switch_to.alert
#
# ## click on OK/YES/AGREE,..
# alert_obj.accept()
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Confirmation Alert"]').click()       ## gives an alert
# time.sleep(2)
#
# ## click on Cancel/No/Disagree
# alert_obj.dismiss()

###########################################################################################################

# ## Simple alert
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Simple Alert"]').click()
# time.sleep(2)
#
# alert_obj = driver.switch_to.alert
#
# alert_obj.accept()
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Simple Alert"]').click()
# time.sleep(2)
# alert_obj.dismiss()

###########################################################################################################

# ## prompt alert
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Prompt Alert"]').click()
# time.sleep(2)
#
# alert_obj = driver.switch_to.alert
# alert_obj.send_keys('Deeksha')
# alert_obj.accept()

###########################################################################################################

## Authentication pop-up

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://the-internet.herokuapp.com/basic_auth')
# time.sleep(2)
#
# ## The above application will ask for the username and password to get into the application.

# ##------------------------------------------------------------------------------------------------------
# ## To handle such popups, we will give the username and password while launching the application
# ## We will include the username and password in the url only.
#
# ## SYNTAX   :   https://username:password@url
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
# time.sleep(2)

###########################################################################################################

## file-upload pop-up

# ## single file-upload
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# choose_file = driver.find_element('xpath', '//input[@id="singleFileInput"]')
# file_path = r"C:\Users\Ramya\OneDrive\Desktop\TestYantra - RamyaProfile.docx"
#
# choose_file.send_keys(file_path)
#
# # ##-----------------------------------------------------------------------------------
#
# ## multiple file-upload
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# multiple_files = driver.find_element('xpath', '//input[@id="multipleFilesInput"]')
#
# file1 = r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\files_\file1.txt'
# file2 = r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\files_\file2.doc'
# file3 = r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\files_\ramya_resume.doc'
#
# multiple_files.send_keys(f'{file1}\n{file2}\n{file3}')
#
# ###########################################################################################################
#
# ## Push notifications
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument("--disable-notifications")
#
# driver = webdriver.Chrome(opts)
# al = driver.switch_to.alert
#
# driver.get('https://www.irctc.co.in/nget/train-search')

#########################################################################################
































