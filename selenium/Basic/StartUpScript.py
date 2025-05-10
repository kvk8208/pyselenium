from selenium import webdriver
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
# open the brower
driver=webdriver.Chrome(options=options)
#maximize the browser
driver.maximize_window()
#enter into DWS Homepage
driver.get("https://demowebshop.tricentis.com/")
# Close the brower
driver.close()
