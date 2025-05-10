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

#Absolute XPATH
# driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[2]/div/ul/li/a").click()
# Relative XPATH
# driver.find_element(By.ID,"small-searchterms").send_keys("Bag")
# sleep(1)
# driver.find_element(By.XPATH,"//input[@class='button-1 search-box-button']").click()
# sleep(2)
# register=driver.find_element(By.XPATH,"//a[text()='Register']")
# data=register.text
# print(data)
# register1=driver.find_element(By.XPATH,"//strong[text()='Community poll']")
# data1=register1.text
# print(data1)
driver.find_element(By.XPATH,"(//input[@type='text'])[2]").send_keys("Watch")
sleep(2)


