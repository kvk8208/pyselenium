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
computer=driver.find_element(By.XPATH,"//a[contains(text(),'Computers')]")
action.key_down(Keys.CONTROL).click(computer).perform() #open in new tab
action.key_up(Keys.CONTROL).perform()
sleep(2)
books=driver.find_element(By.XPATH,"//a[contains(text(),'Books')]")
action.key_down(Keys.SHIFT).click(books).perform()  #open in new window
sleep(5)
driver.close()
