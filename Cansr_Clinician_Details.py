'''
Cansr clinician login and details

'''
import time
from selenium import webdriver


# Create an instance of Chrome Browser
driver = webdriver.Chrome()
#The driver.get method will navigate to a page given by the URL
driver.maximize_window()
driver.get("https://www.cansrdev.com/clinical/login?logout")

# Check if the title of the page is proper
if(driver.title=="Cansr | Login"):
    print ("Success: Cansr application page launched successfully")
else:
    print ("Failure: Cansr application page Title is incorrect")
time.sleep(3)

# Find the email field using xpath with id
email = driver.find_element_by_xpath("//input[@id='inp_loginid']")
# KEY POINT: Send text to an element using send_keys method
email.send_keys('thomas.n.oneill@yopmail.com')
time.sleep(3)

# Find the password field using xpath with id
password = driver.find_element_by_xpath("//input[@id='inp_password']")
password.send_keys('Test@123')
time.sleep(3)

# Find the login field using xpath with id
login = driver.find_element_by_xpath("//button[contains(text(),'Login')]")
login.click()
time.sleep(15)

#Clinician account
my_account = driver.find_element_by_xpath("//span[contains(text(),'My Account')]")
my_account.click()
time.sleep(2)
profile = driver.find_element_by_xpath("//span[@id='registrationPreviewLink']")
profile.click()
time.sleep(10)
qualifications = driver.find_element_by_xpath("//a[@id='tab2-tab']")
qualifications.click()
time.sleep(10)
affiliations = driver.find_element_by_xpath("//a[@id='tab3-tab']")
affiliations.click()
time.sleep(15)

#Back to main page
main_page = driver.find_element_by_xpath("//span[contains(text(),'Main Page')]")
main_page.click()
time.sleep(5)


