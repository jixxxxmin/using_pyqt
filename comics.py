import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QApplication, QMainWindow
from PyQt6 import uic
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QPixmap

from comics_request import re1, re2, re3
from comic import WindowClass_new
from login import add_login_button
from driver import SeleniumDriver



from_class = uic.loadUiType("comics.ui")[0]



class WindowClass(QMainWindow, from_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.driver = SeleniumDriver().get_driver()
                
        self.btn_mon.clicked.connect(self.main)
        self.btn_tue.clicked.connect(self.main)
        self.btn_wed.clicked.connect(self.main)
        self.btn_thu.clicked.connect(self.main)
        self.btn_fri.clicked.connect(self.main)
        self.btn_sat.clicked.connect(self.main)
        self.btn_sun.clicked.connect(self.main)
        
        self.btn_layout.setContentsMargins(0, 2, 0, 0)
        self.layout_comics.setContentsMargins(3, 5, 0, 5)
        self.text_box.setStyleSheet("QLineEdit { border: none; }")
        self.text_box_status.setStyleSheet("""QLineEdit {padding-bottom: 1px;} QLineEdit { border: none; }""")
        
        self.comics = {}
        self.comic = 0
        self.id = 0
        self.select_check1 = ""
        self.select_check2 = ""
        
        self.newWindow = None
        
        btn = add_login_button(self)
        self.btn_layout.addWidget(btn)
        self.naver_webtoon()
        
        
    def naver_webtoon(self):
        
        path = "logo.png"
        try:
            pixmap = QPixmap(path)
                    
            self.image_label.setPixmap(pixmap)
            self.image_label.setText("")
            
        except Exception as e:      print(f"image loading 실패")


    def main(self):
        
        day = self.sender_btn()
        day = self.select_day(day)
        day = self.create_url(day)
        self.comics = self.re_1(day)
        
        self.select_webtoon1(self.comics)
        self.select_webtoon2()
         
    def text_write(self, message):      self.text_box_status.setText(message)
    
    def sender_btn(self):   return self.sender()
    
    def select_day(self, day):
                
        if day == self.btn_mon:       day = "mon"
        elif day == self.btn_tue:     day = "tue"
        elif day == self.btn_wed:     day = "wed"
        elif day == self.btn_thu:     day = "thu"
        elif day == self.btn_fri:     day = "fri"
        elif day == self.btn_sat:     day = "sat"
        elif day == self.btn_sun:     day = "sun"
        
        return day
    
    def create_url(self, day):
        
        url = "https://comic.naver.com/api/webtoon/titlelist/weekday?week=" + day
        self.text_write(f"{day} select")
        
        return url
    
    def re_1(self, url):
        
        try:
            titles_id = re1(url)
            
            return titles_id
        
        except Exception as e:
            self.text_box_statis.append(f"Can't get comics list : {e}")
            
            return
    
    def layout_0(self, layout):
        
        for i in reversed(range(layout.count())): 
            layout.itemAt(i).widget().deleteLater()
    
    def select_webtoon1(self, comics):
        
        row = 0
        
        self.layout_0(self.layout_comics)
        
        for comic in comics:
            
            new = QPushButton(comic, self)
            new.setFixedSize(90, 30)
            
            new.clicked.connect(lambda _, c=comic:self.check(c))
            
            self.layout_comics.addWidget(new, row//3, row%3)
            row+=1
    
    def select_webtoon2(self):
        
        self.scrollArea_box.setLayout(self.layout_comics)
    
    def check(self, comic):
        
        self.select_check1 = comic
        
        if self.select_check1 == self.select_check2:   self.m_main()
        else:   self.thumnail(comic)
    
    def thumnail(self, comic):
        
        self.text_write(f"select : {comic}")
        self.select_check2 = comic
        
        url = self.comics[comic][1]
        
        try:
            
            pixmap = re2(url)
            
            if pixmap is not None and not pixmap.isNull():
                
                pixmap = pixmap.scaled(160, 208)

                self.image_label.setPixmap(pixmap)
                self.image_label.setText("")
                
        except Exception as e:
            
            print("로드 중 오류 발생")
        

    def m_main(self):
        
        try:
            id = self.m_create_url()
            num = self.re_3(id)
            
        except TypeError:     
            self.text_write("성인인증 필요")
            return
        
        except:
            self.text_write("알 수 없는 에러")
            return
        
        self.m_select_webtoon1(num)
        self.select_webtoon2()
                    
    def m_create_url(self):
        
        self.id = self.comics[self.select_check1][0]
        url = f"https://comic.naver.com/api/article/list?titleId={self.id}&page=1"
        
        return url
    
    def re_3(self, no):     return re3(no)
      
    def m_select_webtoon1(self, no):
        
        self.layout_0(self.layout_comics)
        
        row = 0
        for i in range(1, no+1):
            
            new = QPushButton(f"{str(i)}화", self)
            new.setFixedSize(50, 30)
            
            new.clicked.connect(lambda _, n=str(i):self.m_new_widget(n, no))
            
            self.layout_comics.addWidget(new, row//5, row%5)
            row+=1
        
    def m_new_widget(self, no, num):
        
        self.hide()
        self.newWindow = WindowClass_new(no, num, self.select_check1, self.id, self)
        self.newWindow.show()




if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    
    myWindow.show()
    app.exec()
    