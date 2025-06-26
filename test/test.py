import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic
from PyQt6 import QtCore
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QImage
from comics_request import re2


from_class = uic.loadUiType("test.ui")[0]


class WindowClass(QMainWindow, from_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.btn_comics.clicked.connect(self.btn_image)
    
    '''def btn_image(self):
        
        image_path = "test.png"
        
        try:
            
            pixmap = QPixmap(image_path)

            if pixmap.isNull():
                
                print("경로확인")
            
            self.image_label.setPixmap(pixmap)
            self.image_label.setText("")
        
        except Exception as e:
            
            print("로드 중 오류 발생")
     '''       
    
    def btn_image(self):
        
        try:
            pixmap = re2()
            if pixmap is not None and not pixmap.isNull():
                self.image_label.setPixmap(pixmap)
                self.image_label.setText("")
        
        except Exception as e:
            
            print("로드 중 오류 발생")
        
    '''def btn_comics_Func(self):
        
        self.Text_box.append("hello world")
        self.Text_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)'''



if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec()