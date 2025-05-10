from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=option)
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
sleep(2)
expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
sleep(2)
login=driver.find_element(By.XPATH,"//button[text()=' Login ']")
assert login.is_enabled()
print("login is enabled")
login.click()
sleep(2)
actual_url=driver.current_url
assert expected_url==actual_url,"login is unsuccessful"
driver.find_element(By.XPATH,"//input[@class='oxd-input oxd-input--active']").send_keys("krishna")
sleep(2)
driver.find_element(By.XPATH,"//p[@class='oxd-userdropdown-name']").click()
driver.find_element(By.LINK_TEXT,"Logout").click()
sleep(2)
driver.quit()

