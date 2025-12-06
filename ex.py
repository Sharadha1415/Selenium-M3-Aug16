import time

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
# opts.add_argument('--disable-notifications')
#
# driver = webdriver.Chrome(opts)
# wait_ = WebDriverWait(driver, 45)

# driver.get('https://www.saucedemo.com/')
# time.sleep(2)
#
# wait_.until(expected_conditions.visibility_of_element_located())
# wait_.until(expected_conditions.alert_is_present())
# wait_.until(expected_conditions.frame_to_be_available_and_switch_to_it())

# driver.find_element('id', 'user-name').send_keys('standard_user')
# time.sleep(1)
# driver.find_element('id', 'password').send_keys('secret_sauce')
# time.sleep(1)
# driver.find_element('id', 'login-button').click()
# time.sleep(3)
# driver.find_element('id', 'react-burger-menu-btn').click()
# time.sleep(2)
# driver.find_element('id', 'logout_sidebar_link').click()

# res = driver.find_elements('id', 'user-nameeee')
# print(res)



# driver.find_element('id', 'user-name').send_keys('data')
# driver.find_element('name', 'user-name').send_keys('data')
# driver.find_element('class name', 'input_error.form_input')
# driver.find_element('tag name', 'input')
# driver.find_element('link text', 'text')
# driver.find_element('partial link text', 'partial text')
# driver.find_element('css selector', 'tagname[attr_name="attr_value"]')


############################################

'''
listboxes
'''

from selenium.webdriver.support.select import Select

# driver.get('https://www.facebook.com/r.php?entry_point=login')
# time.sleep(2)
#
# month = driver.find_element('xpath', '//select[@id="month"]')
# select_obj = Select(month)

## select_by_index
## select_by_value
## select_by_visible_text

# select_obj.select_by_index(6)
# select_obj.select_by_value('10')
# select_obj.select_by_visible_text('Jun')



# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# colors = driver.find_element('xpath', '//select[@id="colors"]')
# select_obj = Select(colors)
#
# select_obj.select_by_index(2)
# select_obj.select_by_value('yellow')
# select_obj.select_by_value('red')
# time.sleep(2)
#
# # select_obj.deselect_all()
#
# select_obj.deselect_by_value('red')



###########################################################################

'''
alerts are not inspectable
'''

# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# driver.find_element('xpath', '//button[text()="Confirmation Alert"]').click()
# time.sleep(2)
#
# alert_obj = driver.switch_to.alert
# alert_obj.accept()
# alert_obj.dismiss()
#
# alert_obj.send_keys('data')
# alert_obj.accept()
# alert_obj.dismiss()

## authentication popup


# driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')

# driver.get('https://testautomationpractice.blogspot.com/')
# time.sleep(2)
#
# path = r'path_of_file'
# choose_file = driver.find_element('xpath', '//input[@id="singleFileInput"]')
# choose_file.send_keys(path)


##############################################################################

'''
windows handling
'''
#
# handles = driver.window_handles
#
# driver.switch_to.window(handles[0])

##############################

# 'locate the frame'
# driver.switch_to.frame('')
# 'perform the operations inside the frame'
# driver.switch_to.parent_frame()

##############################



'''
action_chains   :   To perform low-level operations in selenium, we go for ActionChains
'''

# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
#
# ac_obj = ActionChains(driver)
#
# # mouse hovering
# ac_obj.move_to_element(ele).perform()
#
# # right click
# ac_obj.context_click(ele).perform()
#
# # double click
# ac_obj.double_click(ele).perform()
#
# # scrolling
# ac_obj.scroll_to_element(ele).perform()
#
# # pagewise scrolling
# ac_obj.send_keys(Keys.PAGE_DOWN).perform()
# ac_obj.send_keys(Keys.PAGE_UP).perform()
#
# # end and start of the app
# ac_obj.send_keys(Keys.END).perform()
# ac_obj.send_keys(Keys.HOME).perform()
#
# # drag and drop
# ac_obj.drag_and_drop(draggable, droppable).perform()
#
# # keyboard
# ac_obj.send_keys(Keys.KEY).perform()


#######################################

'''
STEP1   :   import xlrd
STEP2   :   open the excel file
            workbook = xlrd.open_workbook("path_of_excel_file")     ## book object
STEP3   :   open the worksheet
            worksheet = workbook.sheet_by_name("SheetName")         ## Sheet object
STEP4   :   convert the sheet object to the generator object
            rows = worksheet.get_rows()                             ## generator object
STEP5   :   Traverse or typecast or next() to fetch the data from the generator object

'''

############################################################################################
'''
Pytest  :   It is a unit testing framework
            testing the small unit of the entire program
            
            Rules
            *   file names  --> test_filename.py
            *   func name   --> def test_funcname():
                                    pass 
            *   class name  --> class TestClassName:
                                    pass 
            
            In terminal  --> pytest test_filename.py -vs
'''
#
# import pytest
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# @pytest.fixture()
# def setup():
#     driver = webdriver.Chrome(opts)
#     driver.get('url')
#     yield driver
#
# ## setup --> driver
#
# def test_login(setup):
#     setup.find_element('id', 'login')
#
# def test_reg(setup):
#     setup.find_element('id', 'reg')


'''
git --version

setup username and email
    git config --global user.name username
    git config --global user.email email
    
To check the username and email
    git config user.name --> gives username
    git config user.email --> gives email


go to command prompt    --> change the path
                            cd project_path

Initialize empty repo   --> git init    (files will turn red)

To add the files to the staging area
    git add filename    (that file will be added to the staging area)

To add all the files to the staging area
    git add . 
    
To remove the files from staging area
    git rm --cached filename

To commit   -->     git commit -m "descriptive message"
                    It will generate commit id
                    
To go to the specific commit
    git checkout commit_id

To push the code
    git push repo_url master

To pull
    git clone repo_url
    git pull

'''

##########################################################################


from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)


driver.get('url')

driver.find_element('id', 'reg').click()
driver.find_element('name', 'login').click()
driver.find_element('xpath', 'cart').click()
driver.find_element('css', 'radio').click()

def click(loc_name, value):
    driver.find_element(loc_name, value).click()

click('id', 'reg')























































