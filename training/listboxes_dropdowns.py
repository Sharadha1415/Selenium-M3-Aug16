'''
A ListBox is a web element that allows users to select one or more options from a list
If the tagname of the dropdown/listbox is "select", then it is a standard listbox

Selenium provides a class called Select to interact with <select> elements.

There are 2 types
*   single select listbox   :   If we can select only one element from the dropdown, then it is a single select listbox
*   multi select listbox    :   If we can select multiple elements from the dropdown, then it is a multi select listbox

We will handle single-select and multi-select listboxes in the same way

from selenium.webdriver.support.select import Select
    select_obj = Select(listbox_having_select_tag)

    We have 3 attributes to select the elements from the dropdown
    *   select_by_index     :   Will select the element from the dropdown by passing the index number
                                SYNTAX  :   select_obj.select_by_index(index_num)

    *   select_by_value     :   Will select the element from the dropdown by passing the value of the value attribute
                                SYNTAX  :   select_obj.select_by_value("value")

    *   select_by_visible_text  :   Will select the element from the dropdown by passing the text
                                SYNTAX  :   select_obj.select_by_visible_text("text")


    We have 3 attributes to deselect the elements from the dropdown
    *   deselect_by_index     :   Will deselect the element which is present in that index number
                                SYNTAX  :   select_obj.deselect_by_index(index_num)

    *   deselect_by_value     :   Will deselect the element of the value passed
                                SYNTAX  :   select_obj.deselect_by_value("value")

    *   deselect_by_visible_text  :   Will deselect the element having the given text
                                SYNTAX  :   select_obj.deselect_by_visible_text("text")


    *   select_obj.deselect_all()   :   This will deselect all the selected elements

'''
import time

# ## Single-select listbox
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\files_\demo.html')
# time.sleep(2)
#
# singleselect_listbox = driver.find_element('xpath', '//select[@id="standard_cars"]')
# select_obj = Select(singleselect_listbox)
#
# ## select_by_index
# select_obj.select_by_index(5)
# time.sleep(2)
# select_obj.select_by_index(9)
# time.sleep(2)
# select_obj.select_by_index(3)
# time.sleep(2)
# select_obj.select_by_index(20)      ## NoSuchElementException

# ## select_by_value
# select_obj.select_by_value("bmw")
# time.sleep(2)
# select_obj.select_by_value('merc')
# time.sleep(2)
# select_obj.select_by_value('toy')

# ## select_by_visible_text
# select_obj.select_by_visible_text('Honda')
# time.sleep(2)
# select_obj.select_by_visible_text('Mini')
# time.sleep(2)
# select_obj.select_by_visible_text('Volvo')

########################################################################################################
#
# ## Multi-select listbox
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get(r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\files_\demo.html')
# time.sleep(2)
#
# multiselect_listbox = driver.find_element('xpath', '//select[@id="multiple_cars"]')
# select_obj = Select(multiselect_listbox)

# ## select_by_index
# select_obj.select_by_index(2)
# time.sleep(1)
# select_obj.select_by_index(4)
# time.sleep(1)
# select_obj.select_by_index(6)

# ## select_by_value
# select_obj.select_by_value('aud')
# time.sleep(1)
# select_obj.select_by_value('bmw')
# time.sleep(1)
# select_obj.select_by_value('hda')

# ## select_by_visible_text
# select_obj.select_by_visible_text('Honda')
# time.sleep(1)
# select_obj.select_by_visible_text('Land Rover')
# time.sleep(1)
# select_obj.select_by_visible_text('Mercedes')


########################################################################################################

# ## Normal listbox
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.irctc.co.in/nget/train-search')
# time.sleep(2)
# driver.find_element('xpath', '(//div[@role="button"])[1]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[text()="Vistadome Chair Car (VC)"]').click()
# time.sleep(2)
# driver.find_element('xpath', '(//div[@role="button"])[2]').click()
# time.sleep(2)
# driver.find_element('xpath', '//span[text()="PREMIUM TATKAL"]').click()


########################################################################################################

from selenium import webdriver
from selenium.webdriver.support.select import Select

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get(r'C:\Users\Ramya\PycharmProjects\sel-M3-weekend-Aug16-2025\files_\demo.html')
time.sleep(2)

singleselect_listbox = driver.find_element('xpath', '//select[@id="standard_cars"]')
select_obj = Select(singleselect_listbox)

all_cars = driver.find_elements('xpath', '//select[@id="standard_cars"]/option')
# print(all_cars)     ## list of web-elements         ## [wb1, wb2, wb3, wb4, wb5,..]

# ## select_by_index
# for i in range(0, len(all_cars)):
#     select_obj.select_by_index(i)
#     time.sleep(0.5)


# ## select_by_value
# for car in all_cars:
#     value = car.get_attribute('value')
#     select_obj.select_by_value(value)
#     time.sleep(0.5)


# ## select_by_visible_text
# for car in all_cars:
#     text = car.text
#     select_obj.select_by_visible_text(text)
#     time.sleep(0.5)


























