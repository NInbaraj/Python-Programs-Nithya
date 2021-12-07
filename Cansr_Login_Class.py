'''
Test case for Cansr application using xpath
Test Case 1 to login for existing user
login using class
'''
import time
from selenium import webdriver

import config_cansr as conf
    
class login():
    


    def cansr_login(self):
        self.browser = webdriver.Chrome()
        self.browser.maximize_window()
        self.browser.get("https://www.cansrdev.com/clinical/login?logout")

        # Check if the title of the page is proper
        if(self.browser.title=="Cansr | Login"):
            print ("Success: Cansr application page launched successfully")
        else:
            print ("Failure: Cansr application page Title is incorrect")
            time.sleep(5)
        email = conf.email
        password = conf.password
        print(email,password)

        
        self.email = self.browser.find_element_by_xpath("//input[@id='inp_loginid']")
        
        self.email.send_keys(conf.email)
        time.sleep(5)

            
        self.password = self.browser.find_element_by_xpath("//input[@id='inp_password']")
        self.password.send_keys(conf.password)
        time.sleep(5)

        self.login = self.browser.find_element_by_xpath("//button[contains(text(),'Login')]")
        self.login.click()
        time.sleep(5)

login_obj = login()
login_obj.cansr_login()






        