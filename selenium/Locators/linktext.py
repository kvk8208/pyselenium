from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
expected_url="https://demowebshop.tricentis.com/"
driver = webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)
driver.get("https://demowebshop.tricentis.com/")
actual_url = driver.current_url
if expected_url == actual_url:
    print("i am in dws web page")
    driver.find_element(By.ID,"small-searchterms").send_keys("smartphone")
    sleep(1)
    # driver.find_element(By.CLASS_NAME,"button-1").click()
    #or else u can use another class name
    # driver.find_element(By.CLASS_NAME,"search-box-button").click()
    # driver.find_element(By.LINK_TEXT,"Register").click()
    # sleep(2)
    # driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()
else:
    print("i am not in dws page")