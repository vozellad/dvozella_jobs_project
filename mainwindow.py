from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QListView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui_mainwindow import Ui_MainWindow


class MainWindow(QWidget):
    def __init__(self, jobs):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.jobs = jobs
        self.__list_jobs()

    def __list_jobs(self):
        self.model = QStandardItemModel(self)

        for j in self.jobs:
            job_str = f"{j[1]}\n{j[2]}"  # Get title and company as text
            item = QStandardItem(job_str)
            self.model.appendRow(item)

        self.ui.jobs_listView.setModel(self.model)
