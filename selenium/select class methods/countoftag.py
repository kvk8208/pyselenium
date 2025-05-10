# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.by import By
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# expected_url="https://demowebshop.tricentis.com/"
# driver = webdriver.Chrome(options=options)
# driver.maximize_window()
# sleep(2)
# driver.get("https://demowebshop.tricentis.com/")
# sleep(2)
# input_tag=driver.find_elements(By.XPATH,"//input")
# div_tag=driver.find_elements(By.XPATH,"//div")
# print(f'total no.of input tag={len(input_tag)+1}')
# print(f'total no.of input tag={len(div_tag)+1}')
# driver.close()
#

"""Myntra Website"""
"""
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

option=webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
expected_url="https://www.myntra.com/"
driver=webdriver.Chrome(options=option)
driver.maximize_window()
sleep(2)
driver.get("https://www.myntra.com/")
sleep(2)
actual_url=driver.current_url
if expected_url==actual_url:
    print("i am in myntra page")
    kid=driver.find_element(By.XPATH,"//a[contains(text(),'Kids')]")
    soft_toys=driver.find_element(By.XPATH,"//a[contains(text(),'Soft Toys')]")
    act=ActionChains(driver)
    act.move_to_element(kid).click(soft_toys).perform()
else:
    print("i am not in myntra page")
sleep(5)
driver.close()
"""

"""demo guru website"""
from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=option)
driver.maximize_window()
driver.get("https://demo.guru99.com/test/simple_context_menu.html")

rightclick=driver.find_element(By.XPATH,"//span[contains(text(),'right click me')]")
copy=driver.find_element(By.XPATH,"(//span[contains(text(),'Copy')])[2]")
act=ActionChains(driver)
act.move_to_element(rightclick).context_click(rightclick).click(copy).perform()



