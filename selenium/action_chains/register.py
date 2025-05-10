from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
expected_url="https://demowebshop.tricentis.com/"
driver=webdriver.Chrome(options=option)
driver.maximize_window()
sleep(2)
driver.get("http://demowebshop.tricentis.com/")
sleep(2)
action=ActionChains(driver)

action.key_down(Keys.TAB).perform()
action.key_down(Keys.TAB).perform()
action.key_down(Keys.ENTER).perform()
sleep(2)
for i in range(26):
    action.key_down(Keys.TAB).perform()
action.send_keys("Krishna").perform()
action.key_down(Keys.TAB).perform()
sleep(1)
action.send_keys("Kadam").perform()
action.key_down(Keys.TAB).perform()
sleep(1)
action.send_keys("kvk@gamil.com").perform()
action.key_down(Keys.TAB).perform()
sleep(1)
action.send_keys("Krishna@123").perform()
action.key_down(Keys.TAB).perform()
sleep(1)
action.send_keys("Krishna@123").perform()
action.key_down(Keys.TAB).perform()
sleep(2)
action.key_down(Keys.ENTER).perform()
sleep(5)
driver.close()

