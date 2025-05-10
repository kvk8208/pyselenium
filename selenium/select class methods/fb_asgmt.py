# """
# Write a script for Facebook application
# Open the browser after
# Maximize the browser after
# Enter into facebook login page after
# Click create new account button after
# Fill all the details and click signup after
# Close the browser
# """
#
# from selenium import webdriver
# from time import sleep
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# option=webdriver.ChromeOptions()
# option.add_experimental_option("detach", True)
# expected_url="https://www.facebook.com/"
# driver=webdriver.Chrome(options=option)
# driver.maximize_window()
# sleep(2)
# driver.get("https://www.facebook.com/")
# sleep(2)
# actual_url=driver.current_url
# if expected_url==actual_url:
#     print("i am in facebook page")
#     driver.find_element(By.XPATH,"(// div[@class ='_6ltg'])[2] / a").click()
#     sleep(2)
#     driver.find_element(By.XPATH,"(//input[@type='text'])[1]").send_keys("Krishna")
#     sleep(1)
#     driver.find_element(By.XPATH, "(//input[@type='text'])[2]").send_keys("Kadam")
#     sleep(1)
#     select_day=driver.find_element(By.ID,"day")
#     select=Select(select_day)
#     select.select_by_value("2")
#     sleep(1)
#     select_month=driver.find_element(By.ID,"month")
#     select1=Select(select_month)
#     select1.select_by_index(0)
#     sleep(1)
#     select_year=driver.find_element(By.ID,"year")
#     select2=Select(select_year)
#     select2.select_by_value("2002")
#     sleep(1)
#     driver.find_element(By.XPATH,"(//label[@class='_58mt'])[2]").click()
#     sleep(1)
#     driver.find_element(By.XPATH,"(//input[@type='text'])[5]").send_keys("+918208818281")
#     sleep(1)
#     driver.find_element(By.XPATH, "(//input[@type='password'])").send_keys("Kvk@1628")
#     sleep(1)
#     driver.find_element(By.XPATH,"(//button[@type='submit'])[1]").click()
# else:
#     print("i am not in facebook page")
# # driver.close()


from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
expected_url="https://demowebshop.tricentis.com/"
driver = webdriver.Chrome(options=options)
driver.maximize_window()
sleep(2)
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
driver.find_element(By.LINK_TEXT, "Digital downloads").click()
sleep(2)
# sort_by=driver.find_element(By.ID,"products-orderby")
# sort_by=driver.find_element(By.ID,"products-pagesize")
sort_by=driver.find_element(By.ID,"products-viewmode")
select=Select(sort_by)
data=select.options
count=0
for d in data:
    sort_by = driver.find_element(By.ID, "products-viewmode")
    select = Select(sort_by)
    select.select_by_index(count)
    count+=1
    sleep(2)
# driver.close()