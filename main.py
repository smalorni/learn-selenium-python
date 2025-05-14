# Used to locate elements
from selenium.webdriver.common.by import By
# Helps to press "Enter" button
from selenium.webdriver.common.keys import Keys
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
# Enter search input
text_input.send_keys("selenium")
# Press the "Enter" button on keyboard
text_input.send_keys(Keys.ENTER)

time.sleep(30)

# Ends the session and closes web browser
driver.quit()
