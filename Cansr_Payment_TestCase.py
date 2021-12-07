'''
Automation Test Case for giving the payment details of the patient.
'''
import time
from selenium import webdriver

# Create an instance of Chrome Browser
browser = webdriver.Chrome()

# The driver.get method will navigate to a page given by the URL
browser.maximize_window()
browser.get("http://www.cansrdev.com/clinical/login")

# Check if the title of the page is proper
if(browser.title=="Cansr | Login"):
    print ("Success: Cansr application page launched successfully")
else:
    print ("Failure: Cansr application page Title is incorrect")
time.sleep(5)

# Enter the email field using xpath with id
email = browser.find_element_by_xpath("//input[@id='inp_loginid']")
#Send text to email using send_keys method
email.send_keys('sophiebishop@yopmail.com')
time.sleep(5)

# Enter the password field using xpath with id
password = browser.find_element_by_xpath("//input[@id='inp_password']")
#send text to password using send_keys method
password.send_keys('Chen@42VA')
time.sleep(5)

# CLick the login field using xpath with id
login = browser.find_element_by_xpath("//button[contains(text(),'Login')]")
login.click()
time.sleep(5)

#Selecting  the package
#To Continue
click_continue = browser.find_element_by_xpath("//u[contains(text(),'Click here to continue')]")
click_continue.click()
time.sleep(5)
#Select MDT opinion
purchase = browser.find_element_by_xpath("//a[@id='PKGCOS001']")
purchase.click()
time.sleep(5)

#Accepting the terms and conditions
checkbox = browser.find_element_by_xpath("//input[@id='consentCheckBox']")
checkbox.click()
time.sleep(5)
consent = browser.find_element_by_xpath("//button[@id='agreeConsentId']")
consent.click()
time.sleep(5)

#Payment details
# Select who is payinhg
whosepaying = browser.find_element_by_xpath("//small[contains(text(),'Patient')]")
# ENter the Card Detail
card_number = browser.find_element_by_xpath("//input[@id='cardNumber']")
#send card number using send_keys method
card_number.send_keys('4242424242424242')
#Expiration details
exp_month = browser.find_element_by_xpath("//select[@id='expiryMonth']")
exp_month.send_keys('June')
exp_year = browser.find_element_by_xpath("//select[@id='expiryYear']")
exp_year.send_keys('2024')
security_code = browser.find_element_by_xpath("//input[@id='securityCode']")
security_code.send_keys('987')
time.sleep(5)

#Enter Billing address
address_1 = browser.find_element_by_xpath("//input[@id='cardHolderBilAddr1']")
address_1.send_keys('49 New Dover Rd')
address_2 = browser.find_element_by_xpath("//input[@id='cardHolderBilAddr2']")
address_2.send_keys('WAINFLEET ALL SAINTS')
country = browser.find_element_by_xpath("//select[@id='countryId']")
country.send_keys('United Kingdom')
post_code = browser.find_element_by_xpath("//input[@id='billingPostCode']")
post_code.send_keys('PE24 0QH')
time.sleep(5)

#Confirm Payment Details
conf_pay = browser.find_element_by_xpath("//a[@id='confirmPaymentId']")
conf_pay.click()
time.sleep(5)

#Check details and agree to pay
agree_pay = browser.find_element_by_xpath("//button[@id='payNowButtonId']")
agree_pay.click()



