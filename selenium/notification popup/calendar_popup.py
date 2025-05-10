"""
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--disable-notifications")
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.easemytrip.com/")
sleep(2)
driver.find_element(By.ID,"dvfarecal").click()
sleep(2)

driver.find_element(By.ID,"fiv_3_26/03/2025").click()
sleep(2)
driver.find_element(By.ID,"divRtnCal").click()
sleep(2)

# next=driver.find_element(By.ID,"img2Nex")
# for i in range(3):
#     next = driver.find_element(By.ID, "img2Nex")
#     next.click()
#     sleep(1)
# driver.find_element(By.ID,"frth_2_24/06/2025").click()

while True:
    try:
        driver.find_element(By.ID, "frth_2_24/06/2025").click()
        break
    except:
        driver.find_element(By.ID,"img2Nex").click()
sleep(5)
driver.close()
"""


