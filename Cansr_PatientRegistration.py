'''
Write an automation test case for Cansr application for Entering Patients details in the Registation

'''

import time
from selenium import webdriver

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
time.sleep(3)

# Find the email field using xpath with id
email = browser.find_element_by_xpath("//input[@id='inp_loginid']")
# KEY POINT: Send text to an element using send_keys method
email.send_keys('sophiebishop@yopmail.com')
time.sleep(3)

# Find the password field using xpath with id
password = browser.find_element_by_xpath("//input[@id='inp_password']")
password.send_keys('Chen@42VA')
time.sleep(3)

# Find the login field using xpath with id
login = browser.find_element_by_xpath("//button[contains(text(),'Login')]")
login.click()
time.sleep(5)

# click registration and proceed
register = browser.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/h4[1]")
time.sleep(5)
register.click()
time.sleep(3)

#Enter personal info
per_info = browser.find_element_by_xpath("//a[@id='steps-uid-0-t-0']")
time.sleep(3)

title = browser.find_element_by_xpath("//select[@id='pr_title']")
title.send_keys('Ms.')
time.sleep(2)

#Gender
gender = browser.find_element_by_xpath("//select[@id='pr_gender']")
gender.send_keys('Female')
time.sleep(2)

#Save and exit
save_exit = browser.find_element_by_xpath("//button[contains(text(),'Save & Exit')]")
time.sleep(3)
save_exit.click()

submit = browser.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/a[1]")
time.sleep(3)
submit.send_keys('Yes')


browser.close()






