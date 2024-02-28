from PySide6.QtCore import QModelIndex, Slot
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QListView
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ui_mainwindow import Ui_MainWindow


class MainWindow(QWidget):
    def __init__(self, jobs):
        # Setup UI
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Init jobs
        self.jobs = jobs
        self.model = QStandardItemModel(self)
        self.ui.jobs_listView.setModel(self.model)
        self.__init_jobs_list()
        self.ui.jobs_listView.selectionModel().currentChanged.connect(self.__job_selected)

    def __init_jobs_list(self):
        for j in self.jobs:
            job_str = f"{j[1]}\n{j[2]}"  # Get title and company as text
            item = QStandardItem(job_str)
            self.model.appendRow(item)

    def __job_selected(self, current, previous):
        if previous.row() == -1:  # Boxes will be empty on window startup
            self.ui.title_plainTextEdit.setPlaceholderText("Not available")
            self.ui.company_plainTextEdit.setPlaceholderText("Not available")
            self.ui.location_plainTextEdit.setPlaceholderText("Not available")
            self.ui.description_plainTextEdit.setPlaceholderText("Not available")
            self.ui.postedAt_plainTextEdit.setPlaceholderText("Not available")
            self.ui.salary_plainTextEdit.setPlaceholderText("Not available")
            self.ui.remote_plainTextEdit.setPlaceholderText("No")

        job = self.jobs[current.row()]

        self.ui.title_plainTextEdit.setPlainText(job[1] if job[1] else "")
        self.ui.company_plainTextEdit.setPlainText(job[2] if job[2] else "")
        self.ui.location_plainTextEdit.setPlainText(job[3] if job[3] else "")
        self.ui.description_plainTextEdit.setPlainText(job[4] if job[4] else "")
        self.ui.postedAt_plainTextEdit.setPlainText(job[5] if job[5] else "")
        self.ui.salary_plainTextEdit.setPlainText(job[6] if job[6] != "0" else "")
        self.ui.remote_plainTextEdit.setPlainText("Yes" if job[7] else "")
