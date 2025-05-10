"""
write a script for dews digital download page
open the browser
maximize the browser
enter into dws page
verify page by using url
do login
click digital download web element
add all the products which are present in digital download page by using find element
remove the product which is having an highest price
condition--> write a script in dynamic way
"""

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=option)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)

driver.close()