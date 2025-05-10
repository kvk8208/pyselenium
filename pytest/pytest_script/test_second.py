import pytest
from selenium import webdriver
@pytest.mark.skip
def test_srh():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://www.sunrisershyderabad.in/")
    # assert 2==3
    print("SRH")
    driver.close()
