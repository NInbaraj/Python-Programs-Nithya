'''
Automation Test Case for Factorial Calculator for Positive Integer
'''

import time
from selenium import webdriver

# Create an instance of Chrome WebDriver
driver = webdriver.Chrome()

# The driver.get method will navigate to a page given by the URL
<<<<<<< HEAD
driver.maximize_window()
=======
>>>>>>> main
driver.get("https://qainterview.pythonanywhere.com/")

# Check if the title of the page is proper
if(driver.title=="Factoriall"):
    print ("Success: Factorial Calculator page launched successfully")
else:
    print ("Failure: Factorial Calculator page Title is incorrect")
time.sleep(5)

# Find the enter the integer field using xpath with id
number = driver.find_element_by_xpath("//input[@id='number']")
# KEY POINT: Send text to an element using send_keys method
number.send_keys('5')
time.sleep(5)

# Find the xpath for calculate button
calculate = driver.find_element_by_xpath("//button[@id='getFactorial']")
calculate.click()
time.sleep(5)

# Find the factorial using xpath
factorial = driver.find_element_by_xpath("//p[@id='resultDiv']")
factorial.send_keys('120')
