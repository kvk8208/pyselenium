from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
expected_url="https://demowebshop.tricentis.com/"
driver=webdriver.Chrome(options=option)
driver.maximize_window()
sleep(2)
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
vote=driver.find_element(By.ID,"vote-poll-1")
if vote.is_displayed():
    print("i'm in a dws page")
else:
    print("i'm not in a dws page")
driver.close()