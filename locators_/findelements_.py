'''
find_elements is a Selenium method used to locate multiple web elements on a page.
It returns a list of WebElement objects.

SYNTAX  :   driver.find_elements("loc_name", "loc_value")

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
# driver.get('https://demowebshop.tricentis.com/')
# time.sleep(2)
#
# footer_elements = driver.find_elements('xpath', '//div[@class="footer-menu-wrapper"]//a')
# # print(footer_elements)      ## list of  web-elements        ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7,... wb22]
#
# for element in footer_elements:
#     print(element.text)

############################################################################################################

# ## Eg2
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
# categories = driver.find_elements('xpath', '//div[@class="block block-category-navigation"]//a')
# # print(categories)           ## list of web-elements         ## [wb1, wb2, wb3, wb4, wb5, wb6, wb7]
#
# for ele in categories:
#     print(ele.text)
#
# # ## fetching last three elements of the list
# # for ele in categories[-3::]:
# #     print(ele.text)

############################################################################################################

# ## Eg3
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
# popular_searches = driver.find_elements('xpath', '//div[@class="desktop-pSearchlinks"]/a')
# # print(popular_searches)     ## list of web-elements         ## [wb1, wb2, wb3, wb4, wb5,...]
#
# for ele in popular_searches:
#     print(ele.text)


############################################################################################################

# ## Eg4
#
# from selenium import webdriver
#
# opts = webdriver.ChromeOptions()
# opts.add_experimental_option("detach", True)
#
# driver = webdriver.Chrome(opts)
#
# driver.get('https://www.python.org/')
# time.sleep(2)
#
# '''
# all links --> href --> anchor <a>
# '''
#
# all_links = driver.find_elements('tag name', 'a')
# print(all_links)        ## list of web-elements     ## [a1, a2, a3, a4, a5, a6, a7, a8, a9...]
#
# for link in all_links:
#     print(link.get_attribute('href'))


############################################################################################################

# ## Eg5
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
# all_textboxes = driver.find_elements('xpath', '//input[@name="fname"]')
# print(all_textboxes)        ## list of web-elements
#
# ## [tb1, tb2, tb3, tb4, tb5, tb6, tb7, tb8, tb9]
# data_list = ['Money heist', 'GOT', 'squid game', 'Suits', 'Friends', 'Sherlock Holmes', 'Wednesday', 'Stranger things', 'Breaking bad']
#
# for textbox, data in zip(all_textboxes, data_list):
#     textbox.send_keys(data)

############################################################################################################
'''
1.  Go to https://www.myntra.com/, search for any product, click on the auto-suggestions.
    wap to print the name and price of the products.
2.  wap to print all the colors available for adidas shoes in myntra
3.  Go to https://in.bookmyshow.com/, give the location and wap to print all the recommended movies
'''

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_experimental_option("detach", True)

driver = webdriver.Chrome(opts)

driver.get('https://in.bookmyshow.com/')
time.sleep(2)

driver.find_element('xpath', '//p[text()="Bengaluru"]').click()
time.sleep(2)

driver.find_element('xpath', '//div[text()="See All ›"]').click()
time.sleep(2)

all_movies = driver.find_elements('xpath', '//div[@class="sc-7o7nez-0 elfplV"]')

for movie in all_movies:
    print(movie.text)











