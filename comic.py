from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QMessageBox, QInputDialog
from PyQt6.QtCore import Qt

from comics_request import re4, re2, re5, re6
from login import add_login_button
from driver import SeleniumDriver, check_login
from like import like, unlike

new_class = uic.loadUiType("comic.ui")[0]
        


class WindowClass_new(QMainWindow, new_class):
    
    def __init__(self, no, num, comic, comic_num, comics_window):
        super().__init__()
        self.setupUi(self)
        self.driver = SeleniumDriver().get_driver()
                
        self.no = int(no)
        self.num = int(num)
        self.comic = comic
        self.comic_num = comic_num
        self.comics_window = comics_window
                      
        self.btn_back.clicked.connect(self.back_func)
        self.btn_down.clicked.connect(self.down_main)
        self.btn_like.clicked.connect(self.like_main)
        
        self.btn_layout.setContentsMargins(0, 2, 0, 0)
        self.image_box.setStyleSheet("QLineEdit { border: none; }")
        self.info_box.setStyleSheet("QLineEdit { border: none; font-weight: bold;}")
        self.text_box_status.setStyleSheet("""QLineEdit {padding-bottom: 1px;} QLineEdit { border: none; }""")
                
        btn = add_login_button(self)
        self.btn_layout.addWidget(btn)
        self.comic_info()
                
    
    def back_func(self):
        
        if self.comics_window:
            
            self.close()
        
        self.comics_window.show()
        self.comic_widget = None
    
    def text_write(self, message):      self.text_box_status.setText(message)
    
    
    def comic_info(self):
        
        self.text_write(f"select : {self.comic}")
        
        thum_subtitle = self.create_url()
        thum_subtitle = self.re_4(thum_subtitle, self.no)

        self.thumnail(thum_subtitle[0])
        self.info_box_text(thum_subtitle[1])
        
    def re_4(self, url, no):      return re4(url, no)
    
    def create_url(self):
        
        num = ((self.num-self.no)//20)+1
        
        url = f"https://comic.naver.com/api/article/list?titleId={self.comic_num}&page={str(num)}"
        
        return url
    
    def thumnail(self, url):
        
        try:
            
            pixmap = re2(url)
            
            if pixmap is not None and not pixmap.isNull():
                
                pixmap = pixmap.scaled(202, 120)

                self.image_label.setPixmap(pixmap)
                self.image_label.setText("")
                
        except Exception as e:
            
            print("로드 중 오류 발생")

    def info_box_text(self, subtitle):
        
        self.info_box.setText(subtitle)
        self.info_box.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        
    
    def down_main(self):
        
        url = self.down_create_url()
        links = re5(url)
        
        path = self.show_path_input_dialog()
        
        if path != 0:        self.download(links, path)
            
    def show_path_input_dialog(self):
        
        path, ok = QInputDialog.getText(self, "저장 경로 입력", "저장할 경로를 입력하세요:", text="C:\\Users\\SBA_USER\\test")

        if ok and path:
            
            QMessageBox.information(self, "경로 확인", f"입력된 저장 경로 : {path}")
        
        else:
            
            self.text_write("경로 입력 취소")
            
            return 0
            
        return path
        
    def down_create_url(self):
        
        url = f"https://comic.naver.com/webtoon/detail?titleId={self.comic_num}&no={str(self.no)}"
        
        return url
    
    def download(self, links, path):
        
        for link in links:
            
            re6(link, self.comic_num, self.no, path)
            
        self.text_write(f"select : {self.comic} : download 완료")
        QMessageBox.warning(self, "Done", "다운로드 완료")

    
    def like_main(self):
        
        status = check_login()
        
        if status:      self.like()
        else:           
            
            self.text_write("login 필요")
            
            return
            
    def like(self):
        
        url = self.like_create_url()
        
        if self.btn_like.text() == "♥ Like ♥":    
            
            like(url)
            self.btn_like.setText("Unlike")
            self.text_write("like this webtoon")
            
        else:
            
            unlike(url)
            self.text_write("unlike this webtoon")
        
    def like_create_url(self):
        
        url = f"https://comic.naver.com/webtoon/detail?titleId={self.comic_num}&no={str(self.no)}"
        
        return url
    
    def like_dislike(self):
        
        print("dislike click")
        
    