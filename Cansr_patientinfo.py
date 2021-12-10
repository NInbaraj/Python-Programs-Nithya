'''
Write an automation test case for Cansr application for Entering Patients details in the Registation

contiue from personal information to other details that need to be filled

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

#go to communication information
com_info = browser.find_element_by_xpath("//a[@id='steps-uid-0-t-1']")
time.sleep(3)

#fill in the address and phone number
line_1 = browser.find_element_by_xpath("//input[@id='pr_firstline']")
line_1.send_keys('49 New Dover Rd')
time.sleep(3)
town = browser.find_element_by_xpath("//input[@id='pr_countrydist']")
town.send_keys('WAINFLEET ALL SAINTS')
time.sleep(3)
country = browser.find_element_by_xpath("//select[@id='pr_country']")
country.click()
country.send_keys('United Kingdom')
time.sleep(3)
country_code = browser.find_element_by_xpath("//select[@id='country_code']")
country_code.click()
country_code.send_keys('+44')
time.sleep(3)
contact = browser.find_element_by_xpath("//input[@id='pr_mobile']")
contact.send_keys('7973107122')
time.sleep(3)

#Save and exit
save_exit = browser.find_element_by_xpath("//button[contains(text(),'Save & Exit')]")
time.sleep(3)
save_exit.click()

submit = browser.find_element_by_xpath("//body/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[2]/a[1]")
time.sleep(3)
submit.send_keys('Yes')
submit.click()








