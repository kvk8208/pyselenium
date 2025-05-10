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
# for i in range(6):
#     action.key_down(Keys.TAB).perform()
#     sleep(1)
# action.send_keys("Laptop").perform()
# sleep(1)
# action.key_down(Keys.ENTER).perform()
# sleep(2)
# search_field=driver.find_element(By.ID,"small-searchterms")
# action.send_keys_to_element(search_field,"laptop").perform()
# action.key_down(Keys.ENTER).perform()
# sleep(2)
# driver.close()