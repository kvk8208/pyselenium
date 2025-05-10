# import pytest
#
# @pytest.fixture(autouse=True,scope="function")
# def setup():
#     print("precondition")
#     yield
#     print("postcondition")

#using autouse=True, there is no need to inherit fixture method in every other method

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@pytest.fixture
def setup(request):
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    sleep(3)
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.XPATH,"//button[@type='submit']").click()
    request.cls.driver=driver
    yield
    driver.find_element(By.XPATH,"//span[@class='oxd-userdropdown-tab']").click()
    sleep(3)
    driver.find_element(By.LINK_TEXT,"Logout").click()
    driver.quit()
    sleep(2)