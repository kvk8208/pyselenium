import time
from selenium import webdriver
from selenium.webdriver.common.by import By

opt=webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
expected_url="https://demowebshop.tricentis.com/"
driver=webdriver.Chrome(options=opt)
driver.maximize_window()
time.sleep(1)
driver.get("https://demowebshop.tricentis.com/")
actual_url=driver.current_url
if expected_url==actual_url:
    print("i am in dws page")
    # searchField=driver.find_element(By.TAG_NAME,"input")
    # searchField.send_keys("Rishi")
    # time.sleep(1)
    # driver.find_element(By.CLASS_NAME,"ico-register").click()   #verify by class attribute
    # searchbyID=driver.find_element(By.ID,"small-searchterms")
    # searchbyID.send_keys("laptop")
    # searchbyName=driver.find_element(By.NAME,"FirstName")
    # searchbyName.send_keys("Risikesh")
    driver.find_element(By.CLASS_NAME, "ico-register").click()
    name = driver.find_element(By.ID, "FirstName")
    name.send_keys("Rishikesh")
    lastname = driver.find_element(By.ID, "LastName")
    lastname.send_keys("Kadam")
    email = driver.find_element(By.ID, "Email")
    email.send_keys("yisotic787@apklamp.com")
    password = driver.find_element(By.ID, "Password")
    password.send_keys("Golmal@12")
    conpass = driver.find_element(By.ID, "ConfirmPassword")
    conpass.send_keys("Golmal@12")
    driver.find_element(By.NAME, "register-button").click()

else:
    print("i am not is dws page")
time.sleep(4)
# driver.close()
