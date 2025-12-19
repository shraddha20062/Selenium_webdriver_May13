from selenium import webdriver
from selenium.webdriver.common.by import By
url="https://www.facebook.com/"
#open chrome browser
driver=webdriver.Firefox()

#step 2 open facebook website
driver.get(url)
#quiet the browser
driver.quit()