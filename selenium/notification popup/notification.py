from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--disable-notifications")
driver=webdriver.Chrome(options=options)
driver.maximize_window()
# driver.get("https://www.easemytrip.com/")
driver.get("https://www.agoda.com/en-in/?cid=1844104&ds=wdYZZg9egN3XCjE4")
sleep(2)
action=ActionChains(driver)


# driver.close()