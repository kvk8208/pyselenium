from selenium import webdriver
from selenium.webdriver.common.by import By


def test_dws():
    expected_url = "https://demowebshop.tricentis.com/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://demowebshop.tricentis.com/")
    actual_url=driver.current_url
    assert expected_url==actual_url,'i am not in dws page'
    print("i am in dws page")
    radio_button=driver.find_element(By.ID,"pollanswers-1")
    assert radio_button.is_selected(),"radio_button is not selected"
    print("radio_button is selected")