import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from time import sleep

@pytest.mark.usefixtures("setup")
class Testc2:
    def test_timesheet(self):
        self.driver.find_element(By.XPATH,"//span[text()='Time']").click
        sleep(2)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Type for hints...']").sendkeys("peter")
        sleep(2)
        act=ActionChains(self.driver)
        act.key_down(Keys.ARROW_DOWN).key_down(Keys.ENTER).perform()
        self.driver.find_element(By.XPATH,"//button[@type='submit']").click
        sleep(2)
        exc=self.driver.find_element(By.XPATH,"//p[text()='No Timesheets Found']")
        sleep(2)
        assert exc.is_displayed()


