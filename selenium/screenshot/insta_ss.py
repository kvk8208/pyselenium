from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(15)

driver.get("https://www.instagram.com/mahi7781/?hl=en")
sleep(2)
msd=driver.find_element(By.CSS_SELECTOR,"xrvj5dj.xl463y0.x1ec4g5p.xdj266r.xwy3nlu.xh8yej3")
sleep(4)
msd.screenshot("msd_insta_ss")

sleep(2)
driver.quit()


