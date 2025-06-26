from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time



def login(id, pw):

    options = Options()
    #options.add_argument("--headless")
    options.add_argument("--disable-gpu")


    browser = webdriver.Edge(options=options)


    URL = 'https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/'
    browser.get(URL)
    browser.implicitly_wait(10)
    

    browser.execute_script(f"document.getElementsByName('id')[0].value='{id}'")
    time.sleep(1)

    browser.execute_script(f"document.getElementsByName('pw')[0].value='{pw}'")
    time.sleep(1)

    browser.find_element(By.XPATH, '//*[@id="log.login"]').click()

    time.sleep(1)

    browser.execute_script("window.location.href ='https://www.naver.com'")
    
    return browser
