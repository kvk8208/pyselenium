"""
#simple alert
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
driver.find_element(By.CSS_SELECTOR,".button-1.search-box-button").click()
sleep(2)
# driver.find_element(By.CLASS_NAME,"ico-register").click()  #UnexpectedAlertPresentException
alert=driver.switch_to.alert
sleep(2)
print(alert.text)
alert.accept()
sleep(3)
driver.close()
"""


#confirmation alert
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Alerts.html")
sleep(2)
driver.find_element(By.XPATH,"(//a[@data-toggle='tab'])[2]").click()
sleep(1)
driver.find_element(By.XPATH,"//button[@onclick='confirmbox()']").click()
alert=driver.switch_to.alert
sleep(2)
# alert.accept()
alert.dismiss()