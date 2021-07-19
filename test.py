from selenium import webdriver

from pages.google_page import GooglePage

browser = webdriver.Chrome()

google = GooglePage(driver = browser)
google.go()
google.search_button.click()

browser.quit()