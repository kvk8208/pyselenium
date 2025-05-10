"""
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
expected_url="https://demo.automationtesting.in/Register.html"
driver=webdriver.Chrome(options=option)
driver.maximize_window()
sleep(2)
driver.get("https://demo.automationtesting.in/Register.html")
sleep(1)
driver.find_element(By.XPATH,"//input[@type='text']").send_keys("Krishna")
driver.find_element(By.XPATH,"(//input[@type='text'])[2]").send_keys("Kadam")
driver.find_element(By.XPATH,"//textarea[@ng-model='Adress']").send_keys("Pune")
driver.find_element(By.XPATH,"//input[@ng-model='EmailAdress']").send_keys("krishnakadam1628@gmail.com")
driver.find_element(By.XPATH,"//input[@ng-model='Phone']").send_keys("8208818281")
driver.find_element(By.XPATH,"//input[@value='Male']").click()
driver.find_element(By.ID,"checkbox1").click()
sleep(2)
action=ActionChains(driver)
lang=driver.find_element(By.ID,"msdd")
lang.click()
sleep(1)
action.key_down(Keys.PAGE_DOWN).perform()
sel_lang=driver.find_element(By.XPATH,"//a[text()='Hindi']")
action.scroll_to_element(sel_lang).perform()
driver.find_element(By.LINK_TEXT,"Hindi").click()
sleep(2)
skills=driver.find_element(By.ID,"Skills")
sel=Select(skills)
sel.select_by_visible_text("Python")
sleep(2)
driver.find_element(By.XPATH,"//span[@role='combobox']").click()
sleep(1)
sel_country=driver.find_element(By.XPATH,"//input[@role='textbox']")
action.send_keys_to_element(sel_country,"India").perform()
action.key_down(Keys.ENTER).perform()
sleep(2)
sel_year=driver.find_element(By.XPATH,"//select[@placeholder='Year']")
sel=Select(sel_year)
sel.select_by_visible_text("2002")
sleep(1)
sel_month=driver.find_element(By.XPATH,"//select[@placeholder='Month']")
sel=Select(sel_month)
sel.select_by_visible_text("January")
sleep(1)
sel_day=driver.find_element(By.XPATH,"//select[@placeholder='Day']")
sel=Select(sel_day)
sel.select_by_visible_text("2")
sleep(1)
driver.find_element(By.ID,"firstpassword").send_keys("Krishna@2002")
driver.find_element(By.ID,"secondpassword").send_keys("Krishna@2002")
sleep(2)
driver.find_element(By.ID,"submitbtn").click()
sleep(3)

driver.close()
"""
"""
#task1
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=option)
driver.maximize_window()
sleep(2)
driver.get("file:///C:/Users/krish/Downloads/MultipleWindow%20(1).html")
sleep(1)
driver.find_element(By.XPATH,"//input[@type='button']").click()
sleep(1)
child=driver.window_handles
print(child)
driver.close()
for i in range(1,len(child)):
    driver.switch_to.window(child[i])
    driver.maximize_window()
"""


"""
#task2
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=option)
driver.maximize_window()
sleep(2)
driver.get("file:///C:/Users/krish/Downloads/MultipleWindow%20(1).html")
sleep(1)
driver.find_element(By.XPATH,"//input[@type='button']").click()
sleep(1)
child=driver.window_handles
print(child)
driver.close()
expected_url = "https://www.olivegarden.com/home"
for i in range(1,len(child)):
    driver.switch_to.window(child[i])
    actual = driver.current_url
    if expected_url==actual:
        driver.maximize_window()
    else:
        driver.close()
"""

"""
#task3
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
option=webdriver.ChromeOptions()
option.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=option)
driver.maximize_window()
sleep(2)
driver.get("file:///C:/Users/krish/Downloads/MultipleWindow%20(1).html")
sleep(1)
driver.find_element(By.XPATH,"//input[@type='button']").click()
sleep(1)
child=driver.window_handles
print(child)
driver.close()
olive_page= "https://www.olivegarden.com/home"
barbeque_nation="https://www.barbequenation.com/"
giallozafferano="https://www.giallozafferano.com/"
for i in range(1,len(child)):
    driver.switch_to.window(child[i])
    driver.maximize_window()
    barbeque_nation_1=driver.current_url
    sleep(2)
    if barbeque_nation_1==barbeque_nation:
        driver.find_element(By.XPATH,"//button[@aria-label='Open sidebar menu']").click()
        sleep(4)
    olive_page_1=driver.current_url
    if olive_page_1==olive_page:
        driver.find_element(By.XPATH,"//button[@aria-label='Close']").click()
        sleep(2)
        driver.find_element(By.XPATH,"//a[contains(text(),'Log In')]").click()
        sleep(4)
    giallozafferano_1=driver.current_url
    if giallozafferano_1== giallozafferano:
        driver.find_element(By.XPATH,"//button[contains(text(),'I Accept')]").click()
        sleep(2)
        driver.find_element(By.XPATH,"//div[@class='gz-header-hamburger gz-btn-link']//span").click()
    driver.close()
"""


"""
#task4
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)

driver.maximize_window()
sleep(2)

parent=driver.current_window_handle
print(parent)

driver.get("file:///C:/Users/krish/Downloads/MultipleWindow%20(1).html")
sleep(2)

driver.find_element(By.XPATH,"//input[@type='button']").click()
sleep(2)

child=driver.window_handles
print(child)
sleep(2)

for i in child:
    driver.switch_to.window(i)
    url=driver.current_url
    print(url)
    driver.close()
"""
