"""
It is used to find the multiple elements
characteristics--> 1) Multiple Elements
                   2) It will return all the elements
                   3) Returns list<WebElement>
                   4) If not matching any element, it will return empty list
Ways for finding multiple element--> 1) Finding Common Element
                                     2) Traversing from Common Parent to Child Elements
"""

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

from Basic.VerifyByUrl import actual_url

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=option)
driver.maximize_window()
sleep(2)
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
# community_poll=driver.find_elements(By.XPATH,"//input[@type='radio']")
# print(type(community_poll))
# for poll in community_poll:
#     poll.click()
#     sleep(1)

# nav_bar=driver.find_elements(By.XPATH,"//div[@class='header-links']/ul/li/a")
# for nav in nav_bar:
#     nav.click()
#     sleep(2)
#     driver.back()
#     sleep(1)


# driver.get("https://www.redbus.in/")
# sleep(2)
# driver.back()
# sleep(2)
# driver.forward()
# sleep(2)
# driver.refresh()
# sleep(2)
# driver.close()

links=driver.find_elements(By.XPATH,"//div[@class='column follow-us']/ul/li/a")

for link in links:
    link.click()
    sleep(2)
    expected_url = "https://demowebshop.tricentis.com/news/rss/1"
    actual_url = driver.current_url
    if expected_url == actual_url:
        driver.back()
        sleep(2)
driver.close()