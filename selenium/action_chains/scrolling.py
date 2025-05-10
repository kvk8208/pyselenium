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
act=ActionChains(driver)
# act.key_down(Keys.PAGE_DOWN).perform()
fb=driver.find_element(By.XPATH,"//a[text()='Facebook']")
act.scroll_to_element(fb).perform()

