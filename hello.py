import sys
from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QTextEdit
from PyQt6.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        
app = QApplication(sys.argv)

window = MyApp()
window.show()


sys.exit(app.exec())
