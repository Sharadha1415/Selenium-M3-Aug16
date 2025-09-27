import time


# ## Launching the Chrome browser
# from selenium import webdriver
# c_driver = webdriver.Chrome()
# time.sleep(20)
#
# ##  The above command will close the browser automatically
#
# #-----------------------------------------------------------------------------------------------------
# ## To prevent the browser from automatically closing, We have to use the below code
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# c_driver = webdriver.Chrome(opts)

###########################################################################################################

# ## Launching the Firefox browser
# from selenium import webdriver
# f_driver = webdriver.Firefox()
#
# ## Firefox will not close automatically.
# ## So no need to consider FirefoxOptions and add_experimental_option attribute

###########################################################################################################

# ## Launch the Edge browser
# from selenium import webdriver
# e_driver = webdriver.Edge()
#
# ## The above code will close the browser automatically
#
# ## To prevent the browser from automatically closing, use the below code
#
# ##-----------------------------------------------------------------------------------------------------
#
# from selenium import webdriver
#
# opts = webdriver.EdgeOptions()
# opts.add_experimental_option("detach", True)
#
# e_driver = webdriver.Edge(opts)

###########################################################################################################
'''

*   get()               :   To launch the web-application, we use get()
                SYNTAX  :   driver.get("url")

*   maximize_window()   :   This will maximize the browser window
                SYNTAX  :   driver.maximize_window()
                           
*   minimize_window()   :   This will minimize the browser window
                SYNTAX  :   driver.minimize_window()   
                
*   back()              :   This will go back()
                SYNTAX  :   driver.back()

*   forward()           :   This will go forward
                SYNTAX  :   driver.forward()
                
*   refresh()           :   This will refresh the page
                SYNTAX  :   driver.refresh()

*   current_url         :   This is a property. It will give the url of the page      
                SYNTAX  :   driver.current_url   

*   title               :   This is a property. It will give the title of the page
                SYNTAX  :   driver.title

*   name                :   This is a property. It will give the name of the browser we've used in the code
                SYNTAX  :   driver.name
            
*   To take screenshot  :   driver.save_screenshot("filename.png")
                            The screenshot will be saved in the same location as our python file
                            
                            To save the screenshot in some other location
                            driver.save_screenshot(r"location\filename.png")

*   close()             :   It will close the browser object
                SYNTAX  :   driver.close()
                
'''

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

## Launch the application
driver.get('https://www.google.com/')
time.sleep(2)

## To maximize
driver.maximize_window()
time.sleep(2)
#
# # ## To minimize
# # driver.minimize_window()
# # time.sleep(2)
#
## To go back
driver.back()
time.sleep(2)

## To go forward
driver.forward()
time.sleep(2)

## To refresh
driver.refresh()
time.sleep(2)

## Few properties
print(driver.current_url)
print(driver.title)
print(driver.name)

## To take the screenshot
# driver.save_screenshot('myntra_ss.png')

# driver.save_screenshot(r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\screenshots_\myn_ss.png')
# time.sleep(2)

## close the browser
driver.close()







