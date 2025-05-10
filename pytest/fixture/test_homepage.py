import pytest
from selenium.webdriver.common.by import By
from time import sleep

@pytest.mark.usefixtures("setup")
class Testc1:
    def test_admin(self):
        self.driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active']").send_keys("admin")
        sleep(3)
        admin = self.driver.find_element(By.XPATH, "//span[text()='Admin']")
        sleep(3)
        assert admin.is_displayed(), "admin is not present"
        print("Admin is displayed")

    def test_pim(self):
        sleep(2)
        pim = self.driver.find_element(By.XPATH, "//span[text()='PIM']")
        sleep(2)
        assert pim.is_displayed(), "pim is not present"
        print("pim is displayed")

