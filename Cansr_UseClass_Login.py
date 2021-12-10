'''
Test case for Cansr application using xpath
Test Case 1 to login for existing user
Writing this test case using class

'''
import time
from selenium import webdriver

import config_cansr as conf

class home():

    def login(self):

        # Create an instance of Chrome Browser
        self.browser = webdriver.Chrome()

        # The driver.get method will navigate to a page given by the URL
        self.browser.maximize_window()
        self.browser.get("https://www.cansrdev.com/clinical/login?logout")

        # Check if the title of the page is proper
        if(self.browser.title=="Cansr | Login"):
            print ("Success: Cansr application page launched successfully")
        else:
            print ("Failure: Cansr application page Title is incorrect")
        time.sleep(5)

        # Find the email field using xpath with id
        self.email = self.browser.find_element_by_xpath("//input[@id='inp_loginid']")
        # KEY POINT: Send text to an element using send_keys method
        self.email.send_keys(conf.email)
        time.sleep(5)

        # Find the password field using xpath with id
        self.password = self.browser.find_element_by_xpath("//input[@id='inp_password']")
        self.password.send_keys(conf.password)
        time.sleep(5)



        # Find the login field using xpath with id
        self.login = self.browser.find_element_by_xpath("//button[contains(text(),'Login')]")
        self.login.click()
        time.sleep(5)

home_obj = home()
home_obj.login()