from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
expected_url="https://demowebshop.tricentis.com/"
driver=webdriver.Chrome(options=option)
driver.maximize_window()
sleep(2)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
sleep(2)
act=ActionChains(driver)
# source1=driver.find_element(By.ID,"box1")
# target1=driver.find_element(By.ID,"box101")
# act.drag_and_drop(source1,target1).perform()
# sleep(1)
# source2=driver.find_element(By.ID,"box2")
# target2=driver.find_element(By.ID,"box102")
# act.drag_and_drop(source2,target2).perform()
# sleep(1)
# source3=driver.find_element(By.ID,"box3")
# target3=driver.find_element(By.ID,"box103")
# act.drag_and_drop(source3,target3).perform()
# sleep(1)
# source4=driver.find_element(By.ID,"box4")
# target4=driver.find_element(By.ID,"box104")
# act.drag_and_drop(source4,target4).perform()
# sleep(1)
# source5=driver.find_element(By.ID,"box5")
# target5=driver.find_element(By.ID,"box105")
# act.drag_and_drop(source5,target5).perform()
# sleep(1)
# source6=driver.find_element(By.ID,"box6")
# target6=driver.find_element(By.ID,"box106")
# act.drag_and_drop(source6,target6).perform()
# sleep(1)
# source7=driver.find_element(By.ID,"box7")
# target7=driver.find_element(By.ID,"box107")
# act.drag_and_drop(source7,target7).perform()
# sleep(1)

source7=driver.find_element(By.ID,"box7")
target7=driver.find_element(By.ID,"box107")
act.drag_and_drop_by_offset(source7,820,231).perform()

# driver.close()