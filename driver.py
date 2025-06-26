from selenium import webdriver
from selenium.webdriver.edge.options import Options



class SeleniumDriver:
    
    _instance = None

    def __new__(cls):
        
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            options = webdriver.EdgeOptions()
            
            options = Options()
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")

            cls._instance.driver = webdriver.Edge(options=options)
            
        return cls._instance

    def get_driver(self):
        
        return self.driver


def check_login():
    
    singleton = SeleniumDriver()
    driver = singleton.get_driver()
    status = driver.get_cookies()
    
    cookie_names = {cookie['name'] for cookie in status}
    
    if 'NID_AUT' in cookie_names:
        
        return True
        
    else:
        
        return False
 