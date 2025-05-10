from selenium import webdriver
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
expected_url="https://demowebshop.tricentiss.com/"
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
actual_url=driver.current_url
print(actual_url)
if expected_url==actual_url:
    print('i am in dws page')
else:
    print("i am not in dws page")
driver.close()