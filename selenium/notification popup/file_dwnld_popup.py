from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.ilovepdf.com/word_to_pdf")
sleep(2)
upload=driver.find_element(By.XPATH,"//input[@type='file']")
upload.send_keys("C:/Users/krish/OneDrive/Desktop/Automation testing/selenium notes.docx")
sleep(5)
driver.close()

