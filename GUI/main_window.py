from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from GUI.style.style_Qt import CONST_MAIN_WINDOW

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("генератор QR")
        self.setFixedSize(400, 300)
        self.setStyleSheet(CONST_MAIN_WINDOW)
        self.setWindowIcon(QIcon(r"image\icon.webp"))

        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        instructions = QLabel(text="Введите url и мы создадим для вас QR_CODE")
        self.enter = QLineEdit()
        generator = QPushButton(text="Начать генерацию")
        
        control_UI.addWidget(instructions, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(self.enter)
        control_UI.addWidget(generator)
        
        central_widget.setLayout(control_UI) 
        
        self.setCentralWidget(central_widget)
        self.show()
