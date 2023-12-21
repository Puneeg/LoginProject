import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(3)

# Go to webpage
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)

#Test case 1: Positive LogIn test

#Type username student into Username field
username_locator = driver.find_element(By.ID,"username")
username_locator.send_keys("student")


#Type password Password123 into Password field
password_locator = driver.find_element(By.NAME,"password")
password_locator.send_keys("Password123")


#Puch Submit button
button_locator = driver.find_element(By.ID,"submit")
button_locator.click()
time.sleep(5)

#Verify new page URL contains practicetestautomation.com/logged-in-successfully/
actual_url = driver.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"
#Verify new page contains expected text ('Congratulations' or 'successfully logged in')
logged_in = driver.find_element(By.TAG_NAME,"h1")
actual_text = logged_in.text
assert actual_text == "Logged In Successfully"


#Verify button Log out is displayed on the new page"""
logged_out = driver.find_element(By.XPATH,"//a[@class='wp-block-button__link has-text-color has-background has-very-dark-gray-background-color']")
assert logged_out.is_displayed()