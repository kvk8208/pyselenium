from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--disable-notifications")
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Frames.html")
sleep(2)
driver.find_element(By.LINK_TEXT,"Iframe with in an Iframe").click()
sleep(2)
iframe=driver.find_element(By.XPATH,"//div[@id='Multiple']/iframe")
driver.switch_to.frame(iframe)
sleep(2)
nested_iframe=driver.find_element(By.XPATH,"//div[@class='iframe-container']/iframe")
driver.switch_to.frame(nested_iframe)
sleep(2)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Krishna")
sleep(4)
driver.switch_to.default_content()
driver.find_element(By.LINK_TEXT,"Home").click()

# driver.close()




