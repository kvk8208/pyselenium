import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By




def test_admin():
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    actual_url=driver.current_url
    assert expected_url==actual_url,'i am not in orangehrm page'
    print("i am in orange page")
    driver.find_element(By.NAME,"username").send_keys("Admin")
    driver.find_element(By.NAME,"password").send_keys("admin123")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    driver.find_element(By.XPATH,"//ul[@class='oxd-main-menu']//li[1]").click()
    driver.find_element(By.XPATH,"//div[@class='orangehrm-header-container']//button").click()
    driver.find_element(By.XPATH,"//div[@class='oxd-select-text-input']").click()
    time.sleep(2)
    act=ActionChains(driver)
    act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()

