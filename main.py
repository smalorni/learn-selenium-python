# Used to locate elements
from selenium.webdriver.common.by import By
# Helps to press "Enter" button
from selenium.webdriver.common.keys import Keys
#Add wait feature
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# delays
import time
# this solves the anti-bot measures from Google
import undetected_chromedriver as uc



# Modern version handle browser and driver install with Selenium Manager 
driver = uc.Chrome()

# Navigates to page
driver.get("https://google.com")
# This will find the element
text_input = driver.find_element("name", "q")
# Clear previous input data
text_input.clear()
# Enter search input
text_input.send_keys("selenium geeksforgeeks")
# Press the "Enter" button on keyboard
text_input.send_keys(Keys.ENTER)

#Add a wait until element is located
#PARTIAL_LINK_TEXT finds the link without errors compared to LINK_TEXT. 
WebDriverWait(driver, 10).until (
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Selenium Python Tutorial"))
)

#Find the link that matches the original search then clicks on it
driver.find_element(By.PARTIAL_LINK_TEXT, "Selenium Python Tutorial").click()

#Navigates to page
#Finds and confirms nav bar is displayed
is_nav_displayed = driver.find_element(By.TAG_NAME, "nav").is_displayed()

#Finds all List elements and counts how many in total
#Remember - if finding more than a single element, it uses find_elements (plural)
#Python uses len() to count and prints the number of lists found on page in terminal
lists = driver.find_elements(By.TAG_NAME, "li")
count_total = len(lists)
print(count_total)

time.sleep(20)

# Ends the session and closes web browser
driver.quit()
