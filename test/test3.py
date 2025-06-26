import sys
import random
import string
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("1~5개의 랜덤 버튼 생성")

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.button_a = QPushButton("버튼 A")
        self.button_a.clicked.connect(self.create_random_buttons)
        self.layout.addWidget(self.button_a)

        self.buttons_created = False

    def create_random_buttons(self):
        if self.buttons_created:
            return

        count = random.randint(1, 5)                # 버튼 개수: 1~5
        values = random.sample(range(1, 6), count)  # 중복 없이 값 선택 (예: [3, 1, 5])

        for value in values:
            btn = QPushButton(self.random_name())
            btn.clicked.connect(lambda _, v=value: print(v))
            self.layout.addWidget(btn)

        self.buttons_created = True  # 버튼은 한 번만 생성

    def random_name(self, length=5):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())