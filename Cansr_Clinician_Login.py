'''
Automation test case for Cansr application - Clinician Login
'''

import time
from selenium import webdriver

class home():

    def login(self):
        # Create an instance of Chrome Browser
        self.driver = webdriver.Chrome()
        #The driver.get method will navigate to a page given by the URL
        self.driver.maximize_window()
        self.driver.get("https://www.cansrdev.com/clinical/login?logout")

        # Check if the title of the page is proper
        if(self.driver.title=="Cansr | Login"):
            print ("Success: Cansr application page launched successfully")
        else:
            print ("Failure: Cansr application page Title is incorrect")
        time.sleep(3)

        # Find the email field using xpath with id
        self.email = self.driver.find_element_by_xpath("//input[@id='inp_loginid']")
        # KEY POINT: Send text to an element using send_keys method
        self.email.send_keys('thomas.n.oneill@yopmail.com')
        time.sleep(3)

        # Find the password field using xpath with id
        self.password = self.driver.find_element_by_xpath("//input[@id='inp_password']")
        self.password.send_keys('Test@123')
        time.sleep(3)

        # Find the login field using xpath with id
        self.login = self.driver.find_element_by_xpath("//button[contains(text(),'Login')]")
        self.login.click()
        time.sleep(15)

home_object = home()
home_object.login()


