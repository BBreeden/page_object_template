class BasePage(object):
    
    url = None
    
    def __init__(self, driver):
        '''
        Creates an instance of a page that can be modified with a url when created.
        '''
        self.driver = driver
    
    def go(self):
        '''
        Navigates to the url.
        '''
        self.driver.get(self.url)