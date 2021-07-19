from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BaseElement(object):
    def __init__(self, driver, value, by):
        '''
        Creates a base web page element.

        Driver - Browser driver object
        Value - The id, class, or xpath
        By - By.ID, By.XPATH, etc.
        Locator - Tuple containing how the element is located and the value.
        '''
        self.driver = driver
        self.value = value
        self.by = by
        self.locator = (self.by, self.value)

        self.web_element = None
        self.find()

    @property
    def text(self):
        '''
        If the web element has text, it will be assigned to the object as an object property.
        '''
        text =  self.web_element.text
        return text

    def find(self):
        '''
        Locates the web element by the driver, value, and by values configured when the object is created.
        '''
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator = self.locator))
        self.web_element = element
        return None

    def click(self):
        '''
        Generic command to click the web element defined by the driver, value, and by values configured whent he object is created.
        '''
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator = self.locator))
        element.click()
        return None

    def send_keys(self, text):
        '''
        Sends keys to an input field.
        '''
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator = self.locator))
        element.send_keys(text)
        return None
    
    def select_dropdown(self, index):
        '''
        If the element is a dropdown menu, it will select the item at the indexed location.
        '''
        element = Select(WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator = self.locator)))
        element.select_by_index(index)
        return None
    
    def clear_input(self):
        '''
        Generic command to clear an input element.
        '''
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator = self.locator))
        element.clear()
        return None