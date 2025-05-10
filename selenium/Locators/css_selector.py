"""
syntax for css selector
TagName[AN='AV']
"""
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
    driver.find_element(By.CSS_SELECTOR,"#small-searchterms").send_keys("smartphone")
    sleep(1)
    # driver.find_element(By.CSS_SELECTOR,"input[value='Search']").click()
    driver.find_element(By.CSS_SELECTOR,".button-1.search-box-button").click()
else:
    print("i am not in dws page")