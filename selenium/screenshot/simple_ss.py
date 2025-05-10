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
driver.save_screenshot("dwshomepage.png")
# driver.find_element(By.CLASS_NAME,"ico-register").click()
# driver.save_screenshot("register.png")
# driver.get_screenshot_as_file("register_get.png")
# sleep(2)
search=driver.find_element(By.ID,"small-searchterms")
search.screenshot("searchbar.png")
driver.quit()
