from selenium import webdriver
import time

from pages.google_page import GooglePage

browser = webdriver.Chrome()

google = GooglePage(driver = browser)
google.go()
google.search_field.send_keys('Calvin and Hobbes')
google.search_button.click()

# For demonstration purposes only. Implementing static waits it not best practice.
time.sleep(5)

browser.quit()