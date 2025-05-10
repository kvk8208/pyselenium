from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
expected_url="https://demowebshop.tricentis.com/"
driver=webdriver.Chrome(options=option)
driver.maximize_window()
sleep(2)
driver.get("https://demowebshop.tricentis.com/")
actual_url=driver.current_url
if expected_url==actual_url:
    print("i am in dws web page")
    driver.find_element(By.CLASS_NAME,"ico-register").click()
    gender=driver.find_element(By.ID,"gender-male").click()
    sleep(1)
    name=driver.find_element(By.ID,"FirstName")

    
    name.send_keys("Rishikesh")
    sleep(1)
    lastname=driver.find_element(By.ID,"LastName")
    lastname.send_keys("Kadam")
    sleep(1)
    email=driver.find_element(By.ID,"Email")
    email.send_keys("rushidemo1@gmail.com")
    sleep(1)
    password=driver.find_element(By.ID,"Password")
    password.send_keys("Golmal@12")
    sleep(1)
    conpass=driver.find_element(By.ID,"ConfirmPassword")
    conpass.send_keys("Golmal@12")
    sleep(1)
    driver.find_element(By.NAME,"register-button").click()
else:
    print("i am not in dws page")
sleep(4)
driver.close()




