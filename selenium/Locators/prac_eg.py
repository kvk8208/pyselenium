# from time import sleep
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# expected_url="https://demowebshop.tricentis.com/"
# driver = webdriver.Chrome(options=options)
# driver.maximize_window()
# sleep(2)
# driver.get("https://demowebshop.tricentis.com/")
# sleep(2)
# # driver.find_element(By.LINK_TEXT, "Digital downloads").click()
# # sleep(2)
# driver.find_element(By.XPATH,"//a[contains(text(),'Digital downloads')]").click()
# sleep(2)
# info=driver.find_element(By.XPATH,"//a[text()='3rd Album']/../following-sibling::div[3]/div/span")
# # or     //a[text()='3rd Album']/../../div[3]/div/span
# print(info.text)
# info1=driver.find_element(By.XPATH,"//a[text()='Music 2']/../../div[3]/div/span")
# print(info1.text)
# info2=driver.find_element(By.XPATH,"(//a[text()='Music 2'])[2]/../../div[3]/div/span")
# print(info2.text)



""" Assignment
WSP
Open
Max
Enter into dws page
Verify page by using title
Click excellent radio button
Good radio button
Poor
Very bad
"""

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
expected_title="Demo Web Shop"
driver=webdriver.Chrome(options=option)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
actual_title=driver.title
if expected_title==actual_title:
    print("i am in dws page")
    driver.find_element(By.XPATH,"//label[text()='Excellent']/../../li[1]/input").click()
    sleep(1)
    driver.find_element(By.XPATH,"//label[text()='Good']/../../li[2]/input").click()
    sleep(1)
    driver.find_element(By.XPATH,"//label[text()='Poor']/../../li[3]/input").click()
    sleep(1)
    driver.find_element(By.XPATH,"//label[text()='Very bad']/../../li[4]/input").click()

    rating=['Excellent','Good','Poor','Very bad']
    for i,rating in enumerate (rating,start=1):
        xpath=f"//label[text()='{rating}']"
        driver.find_element(By.XPATH,xpath).click()

