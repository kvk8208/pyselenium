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
cars=sel.options
i=0
for car in cars:
    sel.select_by_index(i)
    i+=1
    sleep(1)
driver.close()
