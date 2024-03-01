from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget
import re

from ui_mainwindow import Ui_MainWindow


class MainWindow(QWidget):
    def __init__(self, jobs):
        # Setup UI
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Init jobs
        self.jobs = jobs
        self.curr_jobs = self.jobs  # Filtered jobs
        self.__list_jobs()
        self.ui.jobs_listWidget.selectionModel().currentChanged.connect(self.__job_selected)

        self.ui.deselect_pushButton.clicked.connect(self.__deselect_job)

        # Filter events
        self.ui.keywordFilter_plainTextEdit.textChanged.connect(self.__filter_jobs)
        self.ui.remoteFilter_checkBox.clicked.connect(self.__filter_jobs)
        self.ui.locationFilter_comboBox.currentIndexChanged.connect(self.__filter_jobs)
        self.ui.salaryFilter_spinBox.valueChanged.connect(self.__filter_jobs)

        self.__insert_city_locations()

    def __list_jobs(self):
        self.ui.jobs_listWidget.clear()
        for j in self.curr_jobs:
            job_str = f"{j[1]}\n{j[2]}"  # Get title and company as text
            self.ui.jobs_listWidget.addItem(job_str)

    def __job_selected(self, current, previous):
        if previous.row() == -1:  # Boxes will be empty on window startup
            self.__set_placeholders()
        self.__set_job_fields(self.curr_jobs[current.row()])

        self.ui.jobs_listWidget.setFocus(Qt.FocusReason.MouseFocusReason)
        self.ui.jobs_listWidget.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def __deselect_job(self):
        self.ui.jobs_listWidget.clearSelection()
        self.__clear_job_fields()
        self.__clear_placeholders()

        self.ui.jobs_listWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    def __set_placeholders(self):
        self.ui.title_plainTextEdit.setPlaceholderText("Not available")
        self.ui.company_plainTextEdit.setPlaceholderText("Not available")
        self.ui.location_plainTextEdit.setPlaceholderText("Not available")
        self.ui.description_plainTextEdit.setPlaceholderText("Not available")
        self.ui.postedAt_plainTextEdit.setPlaceholderText("Not available")
        self.ui.salary_plainTextEdit.setPlaceholderText("Not available")
        self.ui.remote_plainTextEdit.setPlaceholderText("No")
        self.ui.links_plainTextEdit.setPlaceholderText("Not available")
        self.ui.qualifications_plainTextEdit.setPlaceholderText("Not available")

    def __clear_placeholders(self):
        self.ui.title_plainTextEdit.setPlaceholderText("")
        self.ui.company_plainTextEdit.setPlaceholderText("")
        self.ui.location_plainTextEdit.setPlaceholderText("")
        self.ui.description_plainTextEdit.setPlaceholderText("")
        self.ui.postedAt_plainTextEdit.setPlaceholderText("")
        self.ui.salary_plainTextEdit.setPlaceholderText("")
        self.ui.remote_plainTextEdit.setPlaceholderText("")
        self.ui.links_plainTextEdit.setPlaceholderText("")
        self.ui.qualifications_plainTextEdit.setPlaceholderText("")

    def __set_job_fields(self, job):
        self.ui.title_plainTextEdit.setPlainText(job[1] if job[1] else "")
        self.ui.company_plainTextEdit.setPlainText(job[2] if job[2] else "")
        self.ui.location_plainTextEdit.setPlainText(job[3] if job[3] else "")
        self.ui.description_plainTextEdit.setPlainText(job[4] if job[4] else "")
        self.ui.postedAt_plainTextEdit.setPlainText(job[5] if job[5] else "")
        self.ui.salary_plainTextEdit.setPlainText(job[6] if job[6] != "0" else "")
        self.ui.remote_plainTextEdit.setPlainText("Yes" if job[7] else "")
        self.ui.links_plainTextEdit.setPlainText('\n'.join(job[-2]) if job[-2] else "")
        self.ui.qualifications_plainTextEdit.setPlainText('\n'.join(job[-1]) if job[-1] else "")

    def __clear_job_fields(self):
        self.ui.title_plainTextEdit.setPlainText("")
        self.ui.company_plainTextEdit.setPlainText("")
        self.ui.location_plainTextEdit.setPlainText("")
        self.ui.description_plainTextEdit.setPlainText("")
        self.ui.postedAt_plainTextEdit.setPlainText("")
        self.ui.salary_plainTextEdit.setPlainText("")
        self.ui.remote_plainTextEdit.setPlainText("")
        self.ui.links_plainTextEdit.setPlainText("")
        self.ui.qualifications_plainTextEdit.setPlainText("")

    def __filter_jobs(self):
        self.curr_jobs = self.jobs

        #self.__filter_remote()
        #self.__filter_min_salary()
        #self.__filter_keyword()
        self.__filter_city_location()

        self.__list_jobs()
        self.__deselect_job()

    def __filter_keyword(self):
        keyword = self.ui.keywordFilter_plainTextEdit.toPlainText()
        keyword_jobs = []

        for j in self.curr_jobs:
            if keyword.lower() in str(j).lower():
                keyword_jobs.append(j)

        self.curr_jobs = keyword_jobs

    def __insert_city_locations(self):
        cities = self.__get_city_locations()
        self.ui.locationFilter_comboBox.addItem("")
        self.ui.locationFilter_comboBox.addItems(cities)

    def __get_city_locations(self):
        cities = set()
        for j in self.curr_jobs:
            if j[3]:
                cities.add(self.__get_city_str(j[3]))
        return cities

    def __filter_city_location(self):
        user_city = self.ui.locationFilter_comboBox.currentText()
        if not user_city:
            return
        city_jobs = []
        for j in self.curr_jobs:
            if j[3] and user_city == self.__get_city_str(j[3]):
                city_jobs.append(j)
        self.curr_jobs = city_jobs

    def __get_city_str(self, city):
        if "(" in city:  # remove "(+# others)" occurrences
            city = re.findall(".+\(", city)[0][:-1].rstrip()
        if re.search("[0-9-]+$", city):  # remove zipcode
            city = " ".join(city.split(" ")[:-1])
        return city

    def __filter_remote(self):
        if self.ui.remoteFilter_checkBox.isChecked():
            self.curr_jobs = [j for j in self.curr_jobs if j[7]]

    def __filter_min_salary(self):
        user_min_salary = int(self.ui.salaryFilter_spinBox.value())
        min_salary_jobs = []

        # TODO: nesting
        for j in self.curr_jobs:
            if not j[6]:
                curr_min_salary = 0
            else:
                curr_min_salary = re.findall("^[0-9K.]+", j[6])[0]

                if curr_min_salary[-1] == "K":
                    curr_min_salary = float(curr_min_salary[:-1]) * 1000
                curr_min_salary = float(curr_min_salary)

                rate = j[6].split()[-1]
                if rate.startswith("hour"):  # could be "hourly"
                    curr_min_salary *= 40 * 52
                elif rate.startswith("week"):
                    curr_min_salary *= 52

            if user_min_salary <= curr_min_salary:
                min_salary_jobs.append(j)

        self.curr_jobs = min_salary_jobs
