import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# expected_url="https://demowebshop.tricentis.com/"
# driver=webdriver.Chrome(options=options)
# driver.maximize_window()
# sleep(2)
# driver.get("https://demowebshop.tricentis.com/")
# sleep(2)
# actual_url=driver.current_url
# if expected_url==actual_url:
#     print("i'm in dws page")
#     searchField=driver.find_element(By.TAG_NAME,"input")
#     searchField.send_keys("smartphone")
#     sleep(2)
#     driver.find_element(By.CLASS_NAME, "ico-register").click()
#     sleep(2)
#     driver.find_element(By.ID,value="small-searchterms").send_keys("laptop")
#     sleep(2)
#     driver.find_element(By.NAME,value="FirstName").send_keys("Krishna")
# else:
#     print("i'm not in dws page")


option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
expected_url = "https://demowebshop.tricentis.com/"
driver = webdriver.Chrome(options=option)
driver.maximize_window()
sleep(2)
driver.get("https://demowebshop.tricentis.com/")
actual_url = driver.current_url
if expected_url == actual_url:
    print("i am in dws web page")
    driver.find_element(By.CLASS_NAME, "ico-register").click()
    gender = driver.find_element(By.ID, "gender-male").click()
    sleep(1)
    name = driver.find_element(By.ID, "FirstName")
    name.send_keys("Krishna")
    sleep(1)
    lastname = driver.find_element(By.ID, "LastName")
    lastname.send_keys("Kadam")
    sleep(1)
    email = driver.find_element(By.ID, "Email")
    email.send_keys("krishnakadam1628@gmail.com")
    sleep(1)
    password = driver.find_element(By.ID, "Password")
    password.send_keys("krishna@123")
    sleep(1)
    conpass = driver.find_element(By.ID, "ConfirmPassword")
    conpass.send_keys("krishna@123")
    sleep(1)
    # driver.find_element(By.NAME, "register-button").click()
else:
    print("i am not in dws page")
sleep(4)
driver.close()












