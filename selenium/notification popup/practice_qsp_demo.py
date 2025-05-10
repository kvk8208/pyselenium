from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demoapps.qspiders.com/")
sleep(2)
driver.find_element(By.XPATH,"//a[@class='block w-[100%] h-full']").click()
sleep(2)
driver.find_element(By.XPATH,"//section[contains(text(),'Popups')]").click()
sleep(2)
driver.find_element(By.XPATH,"//section[contains(text(),'Javascript')]").click()
sleep(2)
driver.find_element(By.ID,"buttonAlert2").click()
sleep(2)
alert=driver.switch_to.alert
sleep(2)
alert.accept()
sleep(2)
driver.find_element(By.LINK_TEXT,"Confirm").click()
sleep(2)
driver.find_element(By.ID,"buttonAlert5").click()
sleep(2)
alert1=driver.switch_to.alert
sleep(2)
# alert1.accept()
alert1.dismiss()
sleep(2)
driver.find_element(By.LINK_TEXT,"Prompt").click()
sleep(2)
driver.find_element(By.ID,"buttonAlert1").click()
sleep(2)
alert2=driver.switch_to.alert
# alert2.send_keys('yes')
alert2.send_keys('no')
# alert2.accept()
alert2.dismiss()
sleep(2)
driver.close()