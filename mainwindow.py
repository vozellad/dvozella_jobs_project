import re
from PySide6.QtGui import Qt
from PySide6.QtWidgets import QWidget
from mapwindow import MapWindow
from ui_mainwindow import Ui_MainWindow


class MainWindow(QWidget):
    def __init__(self, jobs):
        # Setup UI
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.map_displayed = False

        # Init jobs
        self.JOBS = jobs
        self.filtered_jobs = self.JOBS  # Filtered jobs
        self.list_jobs()
        self.ui.jobs_listWidget.selectionModel().currentChanged.connect(self.job_selected)

        self.ui.deselect_pushButton.clicked.connect(self.deselect_job)

        self.jobs_map = MapWindow([])
        self.jobs_map.windowClosed.connect(self.map_window_closed)
        self.ui.map_pushButton.clicked.connect(self.display_map)

        self.ui.applyFilters_pushButton.clicked.connect(self.filter_jobs)

        self.insert_city_locations()

        self.ui.filter_gridLayout.setAlignment(self.ui.applyFilters_pushButton, Qt.AlignmentFlag.AlignRight)

    def list_jobs(self):
        self.ui.jobs_listWidget.clear()
        for j in self.filtered_jobs:
            job_str = f"{j[1]}\n{j[2]}"  # Get title and company as text
            self.ui.jobs_listWidget.addItem(job_str)
        self.ui.resultsAmt_label.setText(str(len(self.filtered_jobs)))

    def job_selected(self, current, previous):
        if previous.row() == -1:  # Boxes will be empty on window startup
            self.set_placeholders()
        if current.row() == -1:
            return
        self.set_job_fields(self.filtered_jobs[current.row()])

        self.ui.jobs_listWidget.setFocus(Qt.FocusReason.MouseFocusReason)
        self.ui.jobs_listWidget.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def deselect_job(self):
        self.ui.jobs_listWidget.clearSelection()
        self.clear_job_fields()
        self.clear_placeholders()

        self.ui.jobs_listWidget.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    def set_placeholders(self):
        self.ui.title_plainTextEdit.setPlaceholderText("Not available")
        self.ui.company_plainTextEdit.setPlaceholderText("Not available")
        self.ui.location_plainTextEdit.setPlaceholderText("Not available")
        self.ui.description_plainTextEdit.setPlaceholderText("Not available")
        self.ui.postedAt_plainTextEdit.setPlaceholderText("Not available")
        self.ui.salary_plainTextEdit.setPlaceholderText("Not available")
        self.ui.remote_plainTextEdit.setPlaceholderText("No")
        self.ui.links_plainTextEdit.setPlaceholderText("Not available")
        self.ui.qualifications_plainTextEdit.setPlaceholderText("Not available")

    def clear_placeholders(self):
        self.ui.title_plainTextEdit.setPlaceholderText("")
        self.ui.company_plainTextEdit.setPlaceholderText("")
        self.ui.location_plainTextEdit.setPlaceholderText("")
        self.ui.description_plainTextEdit.setPlaceholderText("")
        self.ui.postedAt_plainTextEdit.setPlaceholderText("")
        self.ui.salary_plainTextEdit.setPlaceholderText("")
        self.ui.remote_plainTextEdit.setPlaceholderText("")
        self.ui.links_plainTextEdit.setPlaceholderText("")
        self.ui.qualifications_plainTextEdit.setPlaceholderText("")

    def set_job_fields(self, job):
        self.ui.title_plainTextEdit.setPlainText(job[1] if job[1] else "")
        self.ui.company_plainTextEdit.setPlainText(job[2] if job[2] else "")
        self.ui.location_plainTextEdit.setPlainText(job[3] if job[3] else "")
        self.ui.description_plainTextEdit.setPlainText(job[4] if job[4] else "")
        self.ui.postedAt_plainTextEdit.setPlainText(job[5] if job[5] else "")
        self.ui.salary_plainTextEdit.setPlainText(job[6] if job[6] != "0" else "")
        self.ui.remote_plainTextEdit.setPlainText("Yes" if job[7] else "")
        self.ui.links_plainTextEdit.setPlainText('\n'.join(job[-2]) if job[-2] else "")
        self.ui.qualifications_plainTextEdit.setPlainText('\n'.join(job[-1]) if job[-1] else "")

    def clear_job_fields(self):
        self.ui.title_plainTextEdit.setPlainText("")
        self.ui.company_plainTextEdit.setPlainText("")
        self.ui.location_plainTextEdit.setPlainText("")
        self.ui.description_plainTextEdit.setPlainText("")
        self.ui.postedAt_plainTextEdit.setPlainText("")
        self.ui.salary_plainTextEdit.setPlainText("")
        self.ui.remote_plainTextEdit.setPlainText("")
        self.ui.links_plainTextEdit.setPlainText("")
        self.ui.qualifications_plainTextEdit.setPlainText("")

    def filter_jobs(self):
        self.filtered_jobs = self.JOBS

        self.filter_remote()
        self.filter_min_salary()
        self.filter_keyword()
        self.filter_city_location()

        self.list_jobs()
        if self.map_displayed:
            self.update_map()
        self.deselect_job()

    def filter_keyword(self):
        keyword = self.ui.keywordFilter_plainTextEdit.toPlainText()
        keyword_jobs = []

        for j in self.filtered_jobs:
            if self.keyword_in_job(keyword, j):
                keyword_jobs.append(j)

        self.filtered_jobs = keyword_jobs

    def keyword_in_job(self, keyword, job):
        return (self.keyword_in_job_sublist(keyword, job[:7]) or
                self.keyword_in_job_sublist(keyword, job[-2]) or
                self.keyword_in_job_sublist(keyword, job[-1]))

    def keyword_in_job_sublist(self, keyword, job_sublist):
        if not job_sublist:
            return False
        for item in job_sublist:
            if keyword.lower() in item.lower():
                return True
        return False

    def insert_city_locations(self):
        cities = self.get_city_locations()
        self.ui.locationFilter_comboBox.addItem("")
        self.ui.locationFilter_comboBox.addItems(cities)

    def get_city_locations(self):
        cities = set()
        for j in self.filtered_jobs:
            if j[3]:
                cities.add(self.get_city_str(j[3]))
        return sorted(cities)

    def filter_city_location(self):
        user_city = self.ui.locationFilter_comboBox.currentText()
        if not user_city:
            return
        city_jobs = []
        for j in self.filtered_jobs:
            if j[3] and user_city == self.get_city_str(j[3]):
                city_jobs.append(j)
        self.filtered_jobs = city_jobs

    def get_city_str(self, city):
        city = self.remove_parenthesis_in_location(city)
        if re.search("[0-9-]+$", city):  # remove zipcode
            city = " ".join(city.split(" ")[:-1])
        return city

    def remove_parenthesis_in_location(self, city):
        if "(" in city:  # remove "(+# others)" occurrences
            city = re.findall(".+\(", city)[0][:-1].rstrip()
        return city

    def filter_remote(self):
        if self.ui.remoteFilter_checkBox.isChecked():
            self.filtered_jobs = [j for j in self.filtered_jobs if j[7]]

    def filter_min_salary(self):
        user_min_salary = int(self.ui.salaryFilter_spinBox.value())
        min_salary_jobs = []

        for j in self.filtered_jobs:
            if not j[6]:
                j_min_salary = 0
            else:
                j_min_salary = re.findall("^[0-9K.]+", j[6])[0]

                if j_min_salary[-1] == "K":
                    j_min_salary = float(j_min_salary[:-1]) * 1000
                else:
                    j_min_salary = float(j_min_salary)

                rate = j[6].split()[-1]
                if rate.startswith("hour"):  # could be "hourly"
                    j_min_salary *= 40 * 52
                elif rate.startswith("week"):
                    j_min_salary *= 52

            if user_min_salary <= j_min_salary:
                min_salary_jobs.append(j)

        self.filtered_jobs = min_salary_jobs

    def display_map(self):
        self.map_displayed = True
        self.add_jobs_to_map()
        self.jobs_map.show()

    def update_map(self):
        self.add_jobs_to_map()

    def add_jobs_to_map(self):
        jobs_to_display = self.format_jobs_for_map(self.filtered_jobs)
        self.jobs_map.add_locations(jobs_to_display)

    def format_jobs_for_map(self, jobs):
        jobs_to_display = []
        for j in jobs:
            location = self.remove_parenthesis_in_location(j[3])
            curr_data = tuple(j[:3]) + (location,)
            jobs_to_display.append(curr_data)
        return jobs_to_display

    def map_window_closed(self):
        self.map_displayed = False
