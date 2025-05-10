from selenium import webdriver

#initial steps to avoid closing the browser
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# #open the browser
# webdriver.Chrome(options=options)


# #initial steps to avoid closing the browser
# options=webdriver.EdgeOptions()
# options.add_experimental_option("detach",True)
#
# #open the browser
# webdriver.Edge(options=options)
# #initial steps to avoid closing the browser
options=webdriver.FirefoxOptions()
options.set_preference("detach",True)

#open the browser
webdriver.Firefox(options=options)





