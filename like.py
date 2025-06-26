from driver import SeleniumDriver
from selenium.webdriver.common.by import By



def like(url):
    
    l = "like"
    click(url, l)
    
def unlike(url):
    
    l = "unlike"
    click(url, l)


def click(url, l):
    
    singleton = SeleniumDriver()
    driver = singleton.get_driver()
    driver.get(url)

    button = driver.find_element(By.XPATH, f'//a[@data-type="like" and @data-like-click-area="normal.{l}"]')
    button.click()
