'''
Clinician login and patient details
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

#click on patient 
my_pat = driver.find_element_by_xpath("//a[contains(text(),'My Patients')]")
my_pat.click()
time.sleep(10)

# patient details
pat_detail = driver.find_element_by_xpath("//tbody/tr[1]/td[7]/center[1]/a[1]")
pat_detail.click()

        

