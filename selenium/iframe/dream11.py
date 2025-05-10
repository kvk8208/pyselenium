from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--disable-notifications")
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.dream11.com/")
sleep(2)
parent_handle=driver.current_window_handle
#by using index
# driver.switch_to.frame(0)
# driver.find_element(By.ID,"regEmail").send_keys("8208818281")
sleep(2)
#by using string
# driver.switch_to.frame("send-sms-iframe")
# driver.find_element(By.ID,"regEmail").send_keys("8208818281")
#by using WebElement
frame=driver.find_element(By.XPATH,"//iframe[@title='Iframe Example']")
driver.switch_to.frame(frame)
driver.find_element(By.ID,"regEmail").send_keys("8208818281")
# driver.find_element(By.ID,"regUser").click()
sleep(2)
# driver.switch_to.window(parent_handle)
driver.switch_to.parent_frame()
driver.find_element(By.ID,"hamburger").click()
sleep(2)


driver.close()



