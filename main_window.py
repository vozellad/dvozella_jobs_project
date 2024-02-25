from PySide6.QtWidgets import QApplication, QWidget, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setup()

    def setup(self):
        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle('Window Example')

        self.show()
