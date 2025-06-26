from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QLabel, QPushButton



class LoginDialog(QDialog):
    
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("ID 입력")

        self.pw_input = QLineEdit()
        self.pw_input.setPlaceholderText("PW 입력")
        self.pw_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.ok_button = QPushButton("확인")
        self.ok_button.clicked.connect(self.accept)

        layout.addWidget(QLabel("ID:"))
        layout.addWidget(self.id_input)
        layout.addWidget(QLabel("PW:"))
        layout.addWidget(self.pw_input)
        layout.addWidget(self.ok_button)

        self.setLayout(layout)

    def get_inputs(self):
        
        return self.id_input.text(), self.pw_input.text()


def get_login_info():
    
    dialog = LoginDialog()
    
    if dialog.exec():
        
        return dialog.get_inputs()
    
    return None, None
