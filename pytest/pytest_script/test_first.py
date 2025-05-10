import pytest
from selenium import webdriver

@pytest.mark.smoke
def test_dws():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://demowebshop.tricentis.com/")
    print("demo web shop application")
    driver.close()

@pytest.mark.regression
def test_csk():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://www.chennaisuperkings.com/")
    print("CSK")
    driver.close()

@pytest.mark.skip
def test_mi():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://www.mumbaiindians.com/")
    print("MI")
    driver.close()

@pytest.mark.smoke
def test_rcb():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://royalchallengers.com/")
    print("RCB")
    driver.close()
