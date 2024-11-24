from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QMessageBox
from GUI.style.style_Qt import CONST_MAIN_WINDOW
from Logics.generation import generate

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("генератор QR")
        self.setFixedSize(400, 300)
        self.setStyleSheet(CONST_MAIN_WINDOW)
        self.setWindowIcon(QIcon(r"image\icon.webp"))
        
        self.success = True

        control_UI = QVBoxLayout()
        central_widget = QWidget()
        
        instructions = QLabel(text="Введите url и мы создадим для вас QR_CODE")
        self.enter = QLineEdit()
        generator = QPushButton(text="Начать генерацию")
        generator.clicked.connect(self.start)
        
        control_UI.addWidget(instructions, alignment=Qt.AlignmentFlag.AlignCenter)
        control_UI.addWidget(self.enter)
        control_UI.addWidget(generator)
        
        central_widget.setLayout(control_UI) 
        
        self.setCentralWidget(central_widget)
        self.show()
        
    def start(self):
        try:
            url = self.enter.text()
            generate(url)
        except:
            self.success = False
            error = QMessageBox()
            error.setWindowIcon(QIcon(r"image\icon.webp"))
            error.setWindowTitle("Ошибка")
            error.setText("Ошибка, скорее всего проблема в url")
            error.exec()
            
        if self.success == True:
            result = QMessageBox()
            result.setWindowIcon(QIcon(r"image\icon.webp"))
            result.setWindowTitle("Успех")
            result.setText("На рабочем столе создан url")
            result.exec()