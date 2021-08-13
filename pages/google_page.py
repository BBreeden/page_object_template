from selenium.webdriver.common.by import By
from .base_element import BaseElement
from .base_page import BasePage

class GooglePage(BasePage):
    url = 'https://www.google.com'

    @property
    def search_button(self):
        '''
        Locates the search button and returns it.
        '''
        locator = (By.XPATH, '//body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[2]/div[2]/div[2]/center[1]/input[1]')
        return BaseElement(driver = self.driver, by = locator[0], value=locator[1])
    
    @property
    def search_field(self):
        '''
        Locates the search text field and returns it.
        '''
        locator = (By.XPATH, '//body[1]/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[1]/div[2]/input[1]')
        return BaseElement(driver = self.driver, by = locator[0], value=locator[1])