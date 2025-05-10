from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
expected_url="https://demoapps.qspiders.com/"
driver=webdriver.Chrome(options=option)
driver.maximize_window()
sleep(2)
driver.get("https://demoapps.qspiders.com/")
sleep(2)
actual_url=driver.current_url
if expected_url==actual_url:
    print("I'm in qsp demo site")
    driver.find_element(By.XPATH, "//p[contains(text(),'UI Testing Concepts')]").click()
    sleep(4)
    driver.find_element(By.XPATH,"//section[contains(text(),'Popups')]").click()
    sleep(2)
    driver.find_element(By.XPATH,"//section[contains(text(),'Browser Windows')]").click()
    sleep(2)
    driver.find_element(By.LINK_TEXT,"New Tab").click()
    sleep(2)
    driver.find_element(By.ID,"browserButton4").click()
    child_handle = driver.window_handles
    driver.switch_to.window(child_handle[1])
    driver.find_element(By.ID,"email").send_keys("krishna@gmail.com")
    driver.find_element(By.ID,"password").send_keys("Krishna@123")
    driver.find_element(By.ID,"confirm-password").send_keys("Krishna@123")
    driver.find_element(By.XPATH,"//button[contains(text(),'Sign Up')]").click()
else:
    print("I'm not in qsp web site")
sleep(5)
driver.close()