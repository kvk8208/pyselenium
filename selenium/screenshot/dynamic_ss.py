from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from datetime import datetime


options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
date=datetime.now()
s=str(date).replace(":","-")
driver.save_screenshot("dwshomepage_1"+s+".png")