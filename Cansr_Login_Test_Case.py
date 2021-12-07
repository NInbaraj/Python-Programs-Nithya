'''
Test case for Cansr application using xpath
Test Case 1 to login for existing user
'''
import time
from selenium import webdriver

import config_cansr as conf


# Create an instance of Chrome Browser
browser = webdriver.Chrome()

# The driver.get method will navigate to a page given by the URL
browser.maximize_window()
browser.get("https://www.cansrdev.com/clinical/login?logout")

# Check if the title of the page is proper
if(browser.title=="Cansr | Login"):
    print ("Success: Cansr application page launched successfully")
else:
    print ("Failure: Cansr application page Title is incorrect")
time.sleep(5)

# Find the email field using xpath with id
email = browser.find_element_by_xpath("//input[@id='inp_loginid']")
# KEY POINT: Send text to an element using send_keys method
email.send_keys(conf.email)
time.sleep(5)

# Find the password field using xpath with id
password = browser.find_element_by_xpath("//input[@id='inp_password']")
password.send_keys(conf.password)
time.sleep(5)

# Find the login field using xpath with id
login = browser.find_element_by_xpath("//button[contains(text(),'Login')]")
login.click()
time.sleep(5)






