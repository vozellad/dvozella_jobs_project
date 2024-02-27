from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from ui_mainwindow import Ui_MainWindow


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

