from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from datetime import datetime


options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
# driver.implicitly_wait(15)
driver.get("https://omayo.blogspot.com/")
sleep(2)
driver.execute_script("window.scrollBy(0,1000);")
sleep(2)
driver.execute_script("window.scrollBy(0,500);")
# driver.execute_script("window.scrollTo(0,1000);")
# driver.execute_script("window.scrollTo(0,-1000);")

sleep(4)
driver.close()