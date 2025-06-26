import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog # QDialog를 임포트합니다.
from PyQt6 import uic

# AWindow 클래스를 QMainWindow 대신 QDialog를 상속받도록 수정합니다.
class AWindow(QDialog): # <-- 여기를 QDialog로 변경!
    def __init__(self):
        super().__init__()
        uic.loadUi('comics.ui', self) # 이제 comics.ui (QDialog 기반)와 AWindow (QDialog 기반)가 일치합니다.

        self.b_window = None

        # 버튼 연결은 comics.ui에 있는 버튼 objectName에 따라 그대로 유지됩니다.
        # 예: self.openBWindowButton.clicked.connect(self.open_b_window)
        # comics.ui에 해당 버튼이 없다면 이 줄에서 오류가 발생할 수 있습니다.
        # 만약 comics.ui에 'openBWindowButton'이 없다면, 이 줄은 주석 처리하거나 제거해야 합니다.
        # self.openBWindowButton.clicked.connect(self.open_b_window) # 필요에 따라 주석 해제 또는 변경


    def open_b_window(self):
        if self.b_window is None:
            self.b_window = BWindow()
        self.b_window.show()

# BWindow 클래스는 b.ui가 QMainWindow 기반이라면 QMainWindow를 유지하거나
# b.ui가 QDialog 기반이라면 QDialog로 변경해야 합니다.
# 일단 b.ui가 QMainWindow라고 가정하고 작성합니다.
class BWindow(QMainWindow): # 또는 QDialog
    def __init__(self):
        super().__init__()
        uic.loadUi('test.ui', self) # b.ui 파일의 최상위 위젯에 따라 QMainWindow 또는 QDialog를 사용하세요.

    def closeEvent(self, event):
        event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    a_window = AWindow() # AWindow가 QDialog이므로 QDialog로 인스턴스화됩니다.
    a_window.show()
    sys.exit(app.exec())