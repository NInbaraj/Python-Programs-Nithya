'''
1. Launch Cansr application
2. Create a new user by giving the Patient details - test case 2
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
time.sleep(5)

# Click on the New user Sign up
signup = browser.find_element_by_xpath("//a[contains(text(),'Sign Up')]")
signup.click()
time.sleep(5)

#Enter the firstame
firstname = browser.find_element_by_xpath("//input[@id='inp_firstName']")
#send text to an element using send_keys method
firstname.send_keys('Sophie')
time.sleep(5)

#Enter the lastname
lastname = browser.find_element_by_xpath("//input[@id='inp_LastName']")
#send text to an element using send_keys method
lastname.send_keys('Bishop')
time.sleep(5)

#Enter an email ID
email = browser.find_element_by_xpath("//input[@id='email']")
#send text to an element using send_keys method
email.send_keys('sophiebishop@yopmail.com')
time.sleep(5)

#Enter a zipcode
zipcode = browser.find_element_by_xpath("//input[@id='postcode']")
#send text to an element using send_keys method
zipcode.send_keys('PE24 0QH')
time.sleep(5)

#Enter the DOB
date = browser.find_element_by_xpath("//select[@id='dobDate']")
date.send_keys('19')
month = browser.find_element_by_xpath("//select[@id='dobMonth']")
month.send_keys('June')
year = browser.find_element_by_xpath("//select[@id='dobYear']")
year.send_keys('1978')
time.sleep(5)

#Enter the Captcha code
Captcha = browser.find_element_by_xpath("//input[@id='txtInput']")
time.sleep(10)

#Give consent
consent = browser.find_element_by_xpath("//input[@id='signup-consent']")
consent.click()
time.sleep(5)

#Submit the details
submit = browser.find_element_by_xpath("//button[@id='SignupBut_signup']")
submit.click()
time.sleep(5)






