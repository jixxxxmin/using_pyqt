from selenium.webdriver.common.by import By
import time
from PyQt6.QtWidgets import QPushButton

from driver import SeleniumDriver, check_login
from id_pw import LoginDialog



driver = None

def add_login_button(self):
    
    btn = QPushButton("login")
    btn.setObjectName("btn_login")
    btn.setFixedSize(50, 26)

    btn.clicked.connect(lambda:login_main(self, btn))
    
    return btn
    
def login_main(self, btn):
     
    global driver
        
    if btn.text() == "login":
        
        id, pw = id_pw()
        
        if not id or not pw:
            
            self.text_write("id, pw를 모두 입력하세요")
            
            return
        
        try:
            login(id, pw)
            
            status = check_login()
            if status:        
                
                btn.setText("logout")
                self.text_write("login success")
                
            elif status:     
                
                self.text_write("알맞은 id, pw를 입력하세요")
                
            else:       self.text_write("error")
        
        except:         self.text_write("error")
                
    else:
        
        try:
            quit(driver)
            btn.setText("login")
            
            self.text_write("logout success")
            
        except:             self.text_write("driver not exist")

def id_pw():
    
    dialog = LoginDialog()
        
    if dialog.exec():
            
        id, pw = dialog.get_inputs()
        
        return id, pw
    
    else:       return None, None
   
def login(id, pw):
    
    singleton = SeleniumDriver()
    driver = singleton.get_driver()

    URL = 'https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/'
    driver.get(URL)
    driver.implicitly_wait(10)
    

    driver.execute_script(f"document.getElementsByName('id')[0].value='{id}'")
    time.sleep(1)

    driver.execute_script(f"document.getElementsByName('pw')[0].value='{pw}'")
    time.sleep(1)

    driver.find_element(By.XPATH, '//*[@id="log.login"]').click()

    time.sleep(1)

    #driver.execute_script("window.location.href ='https://www.naver.com'")
    

