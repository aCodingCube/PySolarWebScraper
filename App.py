import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 

import time

print("Program started! ")

# using Chrome to access web
driver = webdriver.Firefox()

# open website  
driver.get("https://kostal-solar-portal.com/home");

#! Main

print("Browser started!")
print("")
print("Please login ->")
input("and enter 'Y' when finished: ")

#! find data elemet

while True:
    elements = driver.find_elements(By.CLASS_NAME,"border")
    data = elements[3].get_attribute("innerText")
    print(data)
    time.sleep(10)
    driver.refresh()
    time.sleep(2)