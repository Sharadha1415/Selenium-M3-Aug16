'''
xpath   :   It is a locator used to locate the web-elements uniquely on the web-application

There are 2 types of xpath
*   absolute xpath  :   This starts from the root of html
                        We use / to write absolute xpath
                        / represents immediate child


*   relative xpath  :   This does not start from the root of html
                        We use // to write relative xpath
                        // represents any child

'''


import time

# ## Eg1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\files_\css_selector_dup.html')
# time.sleep(2)
#
# driver.find_element('xpath', 'html/body/input[1]').send_keys('Deeksha')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/input[2]').send_keys('deeksha@12345')

##################################################################################

# ## Eg2
#
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
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('xpath', 'html/body/div/div/div[2]/div[1]/div/div/form/input').click()

##################################################################################

'''
Attributes  
    SYNTAX  :   //tagname[@attr_name="attr_value"]
    
    

'''
# ## Eg1
#
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
# driver.find_element('xpath', '//input[@id="user-name"]').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('xpath', '//input[@placeholder="Password"]').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('xpath', '//input[@value="Login"]').click()
# time.sleep(3)
# driver.find_element('xpath', '//button[@id="react-burger-menu-btn"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@id="logout_sidebar_link"]').click()

##################################################################################

# ## Eg2
#
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
# driver.find_element('xpath', '//a[@data-group="men"]').click()
# time.sleep(1)
# driver.find_element('xpath', '//a[@data-group="kids"]').click()
# time.sleep(1)
# driver.find_element('xpath', '//a[@data-group="beauty"]').click()

##################################################################################
## Eg3

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.hotstar.com/')
# time.sleep(3)
# driver.find_element('xpath', '//button[@data-testid="modal-close-button"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@aria-label="Search"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//input[@id="searchBar"]').send_keys('RRR')

##################################################################################
## Eg4

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://www.ajio.com/')
# time.sleep(2)
# driver.find_element('xpath', '//a[@title="WOMEN"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[@title="KIDS"]').click()

##################################################################################

'''
text()  :   //tagname[text()="text"]
'''

# ## Eg1
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.flipkart.com/')
# time.sleep(2)
# driver.find_element('xpath', '//span[text()="TVs & Appliances"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Flights"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Login"]').click()

################################################################################

# ## Eg2
#
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
# driver.find_element('xpath', '//a[text()="Women"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Beauty"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//a[text()="Genz"]').click()

###############################################################################

'''
Group indexing
'''

# ## Eg1
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.instagram.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '(//input[@class="_aa4b _add6 _ac4d _ap35"])[1]').send_keys('harry_potter')
# time.sleep(2)
# driver.find_element('xpath', '(//input[@class="_aa4b _add6 _ac4d _ap35"])[2]').send_keys('Harry@123456789')
# time.sleep(2)
# driver.find_element('xpath', '//div[text()="Log in"]').click()

###############################################################################

# ## Eg2
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
# driver.find_element('xpath', '(//input[@type="text"])[1]').send_keys('Jack')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@type="text"])[2]').send_keys('Sparrow')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@type="text"])[5]').send_keys('jack@gmail.com')

# ###############################################################################
#
# ## Eg3
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
# driver.find_element('xpath', '(//input[@name="fname"])[1]').send_keys('Hashmath')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@name="fname"])[2]').send_keys('Deeksha')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@name="fname"])[3]').send_keys('Shailaja')

################################################################################
## Eg4

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(options=opts)
#
# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
# driver.find_element('xpath', '(//input[@type="text"])[1]').send_keys('Ramya')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@type="text"])[2]').send_keys('ramya@gmail.com')
# time.sleep(1)
# driver.find_element('xpath', '(//input[@type="text"])[3]').send_keys('9865321470')

################################################################################
'''
contains()  :   To locate the partial portion of the complete text of any tagname, we go for contains
    SYNTAX  :   //tagname[contains(text(), "partial_text")]
'''

# ## Eg1
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.giva.co/')
# time.sleep(2)
# driver.find_element('xpath', '//span[contains(text(), "Gold with Lab Diamonds")]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[contains(text(), "GIVA Gift Card")]').click()
#
# ################################################################################
#
# ## Eg2
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '(//a[contains(text(), "Books")])[3]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//a[contains(text(), "Computers")])[3]').click()

################################################################################

'''
Dependent-Independent xpath
    *   Identify the dependent and independent elements
    *   Write the xpath of the independent element
    *   Traverse back until we get the common match for dependent independent element
    *   Continue writing the xpath of the dependent element
'''

'''
Eg1. wap to click on the checkbox of Ruby in demo.html
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\files_\demo.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//td[text()="Ruby"]/..//input[@type="checkbox"]').click()


################################################################################
'''
Eg2.    wap to click on the download link of windows in demo.html
'''
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\files_\demo.html')
# time.sleep(2)
#
# driver.find_element('xpath', '//td[text()="Windows"]/..//a[text()="Download"]').click()
#
# ################################################################################

'''
Eg3.    wap to click on the release notes of python 3.13.4 in https://www.python.org/
'''

# from selenium import webdriver
#
# driver = webdriver.Firefox()
#
# driver.get('https://www.python.org/')
# time.sleep(2)
#
# driver.find_element('xpath', '(//a[text()="Downloads"])[1]').click()
# time.sleep(2)
#
# driver.find_element('xpath', '//a[text()="Python 3.13.4"]/../..//a[text()="Release Notes"]').click()

################################################################################
'''
Eg4.    wap to print the sellprice and buyprice of bitcoin in https://www.iforex.in/tools/live-rates   
'''
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.iforex.in/tools/live-rates')
# time.sleep(4)
#
# bitcoin_sellprice = driver.find_element('xpath', '(//div[text()="Bitcoin"]/../..//span)[2]')
# # print(bitcoin_sellprice)        ## web-element
# print("sell price of bitcoin is ", bitcoin_sellprice.text)
#
#
# bitcoin_buyprice = driver.find_element('xpath', '(//div[text()="Bitcoin"]/../..//span)[3]')
# print("buy price of bitcoin is ", bitcoin_buyprice.text)

################################################################################
'''
Eg5.    wap to print the price of Silver in https://in.tradingview.com/
'''

# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://in.tradingview.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//span[text()="Search"]').click()
# time.sleep(2)
# driver.find_element('xpath', '//input[@name="query"]').send_keys('Silver')
# time.sleep(2)
# driver.find_element('xpath', '(//button[@aria-label="Search"])[3]').click()
# time.sleep(2)
# silver = driver.find_element('xpath', '//span[text()="SILVER"]/../../..//span[@class="priceWrapper-qWcO4bp9"]')
# print(silver.text)

###############################





























