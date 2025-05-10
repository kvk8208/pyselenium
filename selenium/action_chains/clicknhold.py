from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
expected_url="https://demowebshop.tricentis.com/"
driver=webdriver.Chrome(options=option)
driver.maximize_window()
sleep(2)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
sleep(2)
act=ActionChains(driver)
source1=driver.find_element(By.ID,"box1")
target1=driver.find_element(By.ID,"box101")
act.click_and_hold(source1).release(target1).perform()