#Assignment
"""
wsf dws
1. open browser
2. maximize
3. enter into dws page
4. click gift section
5. add all products from gift section inside shopping cart
note: use only one for loop
"""

from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from Locators.TagName import actual_url

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
expected_url="https://demowebshop.tricentis.com/"
driver=webdriver.Chrome(options=option)
driver.maximize_window()
sleep(2)
driver.get("http://demowebshop.tricentis.com/")
sleep(2)
driver.find_element(By.XPATH,"//a[contains(text(),'Gift Cards')][1]").click()
sleep(2)
add_2_cart=driver.find_elements(By.XPATH,"//input[@class='button-2 product-box-add-to-cart-button']")
for add in range(len(add_2_cart)):
    add_2_cart = driver.find_elements(By.XPATH, "//input[@class='button-2 product-box-add-to-cart-button']")
    add_2_cart[add].click()
    sleep(2)
    expected_url="https://demowebshop.tricentis.com/5-virtual-gift-card"
    actual_url=driver.current_url
    expected_url1="https://demowebshop.tricentis.com/25-virtual-gift-card"
    actual_url1=driver.current_url
    expected_url2="https://demowebshop.tricentis.com/50-physical-gift-card"
    actual_url2=driver.current_url
    expected_url3 = "https://demowebshop.tricentis.com/100-physical-gift-card"
    actual_url3 = driver.current_url
    if expected_url==actual_url:
        driver.find_element(By.ID,"giftcard_1_RecipientName").send_keys("krishna")
        driver.find_element(By.ID,"giftcard_1_RecipientEmail").send_keys("krishnakadam1628@gmail.com")
        driver.find_element(By.ID,"giftcard_1_SenderName").send_keys("yash")
        driver.find_element(By.ID,"giftcard_1_SenderEmail").send_keys("yash123@gmail.com")
        driver.find_element(By.ID,"giftcard_1_Message").send_keys("add this product to cart")
        driver.find_element(By.XPATH,"//input[@class='button-1 add-to-cart-button']").click()
        sleep(2)
        driver.find_element(By.XPATH, "//a[contains(text(),'Gift Cards')][1]").click()
    elif expected_url1==actual_url1:
        driver.find_element(By.ID, "giftcard_2_RecipientName").send_keys("krishna")
        driver.find_element(By.ID, "giftcard_2_RecipientEmail").send_keys("krishnakadam1628@gmail.com")
        driver.find_element(By.ID, "giftcard_2_SenderName").send_keys("yash")
        driver.find_element(By.ID, "giftcard_2_SenderEmail").send_keys("yash123@gmail.com")
        driver.find_element(By.ID, "giftcard_2_Message").send_keys("add this product to cart")
        driver.find_element(By.XPATH, "//input[@class='button-1 add-to-cart-button']").click()
        sleep(2)
        driver.find_element(By.XPATH, "//a[contains(text(),'Gift Cards')][1]").click()
    elif expected_url2==actual_url2:
        driver.find_element(By.ID, "giftcard_3_RecipientName").send_keys("krishna")
        driver.find_element(By.ID, "giftcard_3_SenderName").send_keys("yash")
        driver.find_element(By.ID, "giftcard_3_Message").send_keys("add this product to cart")
        driver.find_element(By.XPATH, "//input[@class='button-1 add-to-cart-button']").click()
        sleep(2)
        driver.find_element(By.XPATH, "//a[contains(text(),'Gift Cards')][1]").click()
    elif expected_url3==actual_url3:
        driver.find_element(By.ID, "giftcard_4_RecipientName").send_keys("krishna")
        driver.find_element(By.ID, "giftcard_4_SenderName").send_keys("yash")
        driver.find_element(By.ID, "giftcard_4_Message").send_keys("add this product to cart")
        driver.find_element(By.XPATH, "//input[@class='button-1 add-to-cart-button']").click()
        sleep(5)
driver.close()




