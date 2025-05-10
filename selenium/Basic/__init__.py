from time import sleep
from selenium import webdriver

#initial steps to avoid closing the browser
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

#open the browser
driver=webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)
driver.close()
#WebElement--> anything which is present in the webpage, we called it as WebElement
# like radio button, checkbox, text fields, links etc
#all these elements are created using html, css or by js and the elements will be present in the html docs,
# to open this html doc we have two ways, 1) right click and inspect 2) ctrl+shift+i

#syntax for web element-->
# driver.find_element(locators,"value")
