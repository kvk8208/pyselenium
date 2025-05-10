import time
from selenium import webdriver
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
expected_title="Demo Web Shop. Electronics"
driver=webdriver.Chrome(options=options)
driver.maximize_window()
time.sleep(2)
driver.get("https://demowebshop.tricentis.com/electronics")
actual_title=driver.title
if actual_title==expected_title:
    print('i am in dws page')
else:
    print("i am not in dws page")
time.sleep(3)
driver.close()