from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Locators.TagName import actual_url

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=option)
driver.maximize_window()
sleep(2)
driver.get("http://demowebshop.tricentis.com/")
sleep(2)
parent_handle=driver.current_window_handle
action=ActionChains(driver)
action.key_down(Keys.PAGE_DOWN).perform()
sleep(2)
driver.find_element(By.XPATH,"//a[text()='Facebook']").click()
sleep(2)
# driver.find_element(By.XPATH,"//a[text()='Twitter']").click()
# sleep(2)
child_handle=driver.window_handles
# print(child_handle)
driver.switch_to.window(child_handle[1])
driver.find_element(By.XPATH,"//span[text()='Create new account']").click()
fb_register=driver.window_handles
print(fb_register)
driver.switch_to.window(fb_register[2])
expected_url="https://www.facebook.com/reg/?entry_point=logged_out_dialog&next=%2FnopCommerce"
curr_url=driver.current_url
if expected_url==curr_url:
    print("i'm in fb_register page")
    driver.find_element(By.XPATH, "(//input[@type='text'])[1]").send_keys("Krishna")
    sleep(1)
else:
    print("i'm not in fb_register page")
# driver.close()
