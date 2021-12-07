'''
Automation test case for Weather Shopper App
If the temperature is below 19C shop for Moisturizer
If the temperture is above 34C shop for Sunscreen
'''
import time
from selenium import webdriver

# Create an instance of Chrome Browser
browser = webdriver.Chrome()

# The browser.get method will navigate to a page given by the URL
browser.maximize_window()
browser.get("https://weathershopper.pythonanywhere.com/")

# Check if the title of the page is proper
if(browser.title=="Current Temperature"):
    print ("Success: Weather Shopper application page launched successfully")
else:
    print ("Failure: Weather Shopper application page Title is incorrect")
time.sleep(5)

#Get the temperature value
current_temp = browser.find_element_by_xpath("//span[@id='temperature']")
#Text method is used to read the value
current_temp=current_temp.text

#Split method used to split the string into a list
split_string=current_temp.split()
#Get the integer value of split string
temp_value=int(split_string[-2])

if(temp_value<=19):
    buy_moisturizer = browser.find_element_by_xpath("//button[contains(text(),'Buy moisturizers')]")
    buy_moisturizer.click()
elif(temp_value>=34):
    buy_sunscreen = browser.find_element_by_xpath("//button[contains(text(),'Buy sunscreens')]")
    buy_sunscreen.click()
else:
    print("The temperature is between 19 and 34. So no need to buy Moisturizer or Sunscreen")
