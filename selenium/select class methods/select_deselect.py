from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

option=webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=option)
driver.maximize_window()
sleep(2)
driver.get("file:///C:/Users/krish/Downloads/demo.html")
sleep(2)

single_select=driver.find_element(By.ID,"standard_cars")
sel=Select(single_select)
sel.select_by_visible_text("Audi")
sleep(2)
sel.select_by_value("jgr")
sleep(2)
sel.select_by_index(3)
sleep(2)

multiple_select=driver.find_element(By.ID,"multiple_cars")
sel1=Select(multiple_select)
sel1.select_by_visible_text("Audi")
sleep(2)
sel1.select_by_value("jgr")
sleep(2)
sel1.select_by_index(3)
sleep(2)

# sel1.deselect_by_visible_text("Audi")
# sleep(2)
# sel1.deselect_by_value("jgr")
# sleep(2)
# sel1.deselect_by_index(3)
# sleep(2)
sel1.deselect_all()
sleep(2)
driver.close()