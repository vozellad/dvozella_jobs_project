# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QListWidget,
    QListWidgetItem, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(974, 678)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(MainWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.middleVLine_line = QFrame(MainWindow)
        self.middleVLine_line.setObjectName(u"middleVLine_line")
        self.middleVLine_line.setFrameShape(QFrame.VLine)
        self.middleVLine_line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.middleVLine_line, 0, 1, 5, 1)

        self.jobdata_verticalLayout = QVBoxLayout()
        self.jobdata_verticalLayout.setObjectName(u"jobdata_verticalLayout")
        self.jobdata_label = QLabel(MainWindow)
        self.jobdata_label.setObjectName(u"jobdata_label")
        self.jobdata_label.setMinimumSize(QSize(0, 30))

        self.jobdata_verticalLayout.addWidget(self.jobdata_label)

        self.jobdata_line = QFrame(MainWindow)
        self.jobdata_line.setObjectName(u"jobdata_line")
        self.jobdata_line.setFrameShape(QFrame.HLine)
        self.jobdata_line.setFrameShadow(QFrame.Sunken)

        self.jobdata_verticalLayout.addWidget(self.jobdata_line)

        self.title_label = QLabel(MainWindow)
        self.title_label.setObjectName(u"title_label")

        self.jobdata_verticalLayout.addWidget(self.title_label)

        self.title_plainTextEdit = QPlainTextEdit(MainWindow)
        self.title_plainTextEdit.setObjectName(u"title_plainTextEdit")
        self.title_plainTextEdit.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.title_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.title_plainTextEdit.setSizePolicy(sizePolicy1)
        self.title_plainTextEdit.setMinimumSize(QSize(0, 30))
        self.title_plainTextEdit.setMaximumSize(QSize(16777215, 45))
        self.title_plainTextEdit.setReadOnly(True)

        self.jobdata_verticalLayout.addWidget(self.title_plainTextEdit)

        self.company_label = QLabel(MainWindow)
        self.company_label.setObjectName(u"company_label")
        self.company_label.setEnabled(True)

        self.jobdata_verticalLayout.addWidget(self.company_label)

        self.company_plainTextEdit = QPlainTextEdit(MainWindow)
        self.company_plainTextEdit.setObjectName(u"company_plainTextEdit")
        self.company_plainTextEdit.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.company_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.company_plainTextEdit.setSizePolicy(sizePolicy1)
        self.company_plainTextEdit.setMinimumSize(QSize(0, 30))
        self.company_plainTextEdit.setMaximumSize(QSize(16777215, 45))
        self.company_plainTextEdit.setReadOnly(True)

        self.jobdata_verticalLayout.addWidget(self.company_plainTextEdit)

        self.location_label = QLabel(MainWindow)
        self.location_label.setObjectName(u"location_label")

        self.jobdata_verticalLayout.addWidget(self.location_label)

        self.location_plainTextEdit = QPlainTextEdit(MainWindow)
        self.location_plainTextEdit.setObjectName(u"location_plainTextEdit")
        self.location_plainTextEdit.setEnabled(True)
        self.location_plainTextEdit.setMinimumSize(QSize(0, 30))
        self.location_plainTextEdit.setMaximumSize(QSize(16777215, 45))
        self.location_plainTextEdit.setReadOnly(True)

        self.jobdata_verticalLayout.addWidget(self.location_plainTextEdit)

        self.postedAt_label = QLabel(MainWindow)
        self.postedAt_label.setObjectName(u"postedAt_label")

        self.jobdata_verticalLayout.addWidget(self.postedAt_label)

        self.postedAt_plainTextEdit = QPlainTextEdit(MainWindow)
        self.postedAt_plainTextEdit.setObjectName(u"postedAt_plainTextEdit")
        self.postedAt_plainTextEdit.setEnabled(True)
        self.postedAt_plainTextEdit.setMinimumSize(QSize(0, 30))
        self.postedAt_plainTextEdit.setMaximumSize(QSize(16777215, 45))
        self.postedAt_plainTextEdit.setReadOnly(True)

        self.jobdata_verticalLayout.addWidget(self.postedAt_plainTextEdit)

        self.salary_label = QLabel(MainWindow)
        self.salary_label.setObjectName(u"salary_label")

        self.jobdata_verticalLayout.addWidget(self.salary_label)

        self.salary_plainTextEdit = QPlainTextEdit(MainWindow)
        self.salary_plainTextEdit.setObjectName(u"salary_plainTextEdit")
        self.salary_plainTextEdit.setEnabled(True)
        self.salary_plainTextEdit.setMinimumSize(QSize(0, 30))
        self.salary_plainTextEdit.setMaximumSize(QSize(16777215, 45))
        self.salary_plainTextEdit.setReadOnly(True)

        self.jobdata_verticalLayout.addWidget(self.salary_plainTextEdit)

        self.remote_label = QLabel(MainWindow)
        self.remote_label.setObjectName(u"remote_label")

        self.jobdata_verticalLayout.addWidget(self.remote_label)

        self.remote_plainTextEdit = QPlainTextEdit(MainWindow)
        self.remote_plainTextEdit.setObjectName(u"remote_plainTextEdit")
        self.remote_plainTextEdit.setEnabled(True)
        self.remote_plainTextEdit.setMinimumSize(QSize(0, 30))
        self.remote_plainTextEdit.setMaximumSize(QSize(16777215, 45))
        self.remote_plainTextEdit.setReadOnly(True)

        self.jobdata_verticalLayout.addWidget(self.remote_plainTextEdit)

        self.links_label = QLabel(MainWindow)
        self.links_label.setObjectName(u"links_label")

        self.jobdata_verticalLayout.addWidget(self.links_label)

        self.links_plainTextEdit = QPlainTextEdit(MainWindow)
        self.links_plainTextEdit.setObjectName(u"links_plainTextEdit")
        self.links_plainTextEdit.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.links_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.links_plainTextEdit.setSizePolicy(sizePolicy2)
        self.links_plainTextEdit.setMinimumSize(QSize(0, 30))
        self.links_plainTextEdit.setMaximumSize(QSize(16777215, 60))

        self.jobdata_verticalLayout.addWidget(self.links_plainTextEdit)

        self.qualifications_label = QLabel(MainWindow)
        self.qualifications_label.setObjectName(u"qualifications_label")

        self.jobdata_verticalLayout.addWidget(self.qualifications_label)

        self.qualifications_plainTextEdit = QPlainTextEdit(MainWindow)
        self.qualifications_plainTextEdit.setObjectName(u"qualifications_plainTextEdit")
        self.qualifications_plainTextEdit.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.qualifications_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.qualifications_plainTextEdit.setSizePolicy(sizePolicy2)
        self.qualifications_plainTextEdit.setMinimumSize(QSize(0, 30))
        self.qualifications_plainTextEdit.setMaximumSize(QSize(16777215, 60))
        self.qualifications_plainTextEdit.setReadOnly(True)

        self.jobdata_verticalLayout.addWidget(self.qualifications_plainTextEdit)

        self.description_label = QLabel(MainWindow)
        self.description_label.setObjectName(u"description_label")

        self.jobdata_verticalLayout.addWidget(self.description_label)

        self.description_plainTextEdit = QPlainTextEdit(MainWindow)
        self.description_plainTextEdit.setObjectName(u"description_plainTextEdit")
        self.description_plainTextEdit.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.description_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.description_plainTextEdit.setSizePolicy(sizePolicy2)
        self.description_plainTextEdit.setMinimumSize(QSize(0, 30))
        self.description_plainTextEdit.setMaximumSize(QSize(16777215, 120))
        self.description_plainTextEdit.setReadOnly(True)

        self.jobdata_verticalLayout.addWidget(self.description_plainTextEdit)


        self.gridLayout_2.addLayout(self.jobdata_verticalLayout, 0, 2, 5, 1)

        self.jobslist_verticalLayout = QVBoxLayout()
        self.jobslist_verticalLayout.setObjectName(u"jobslist_verticalLayout")
        self.jobs_label = QLabel(MainWindow)
        self.jobs_label.setObjectName(u"jobs_label")
        self.jobs_label.setMinimumSize(QSize(0, 30))

        self.jobslist_verticalLayout.addWidget(self.jobs_label)

        self.line = QFrame(MainWindow)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.jobslist_verticalLayout.addWidget(self.line)

        self.filter_label = QLabel(MainWindow)
        self.filter_label.setObjectName(u"filter_label")

        self.jobslist_verticalLayout.addWidget(self.filter_label)

        self.filter_gridLayout = QGridLayout()
        self.filter_gridLayout.setObjectName(u"filter_gridLayout")
        self.remoteFilter_label = QLabel(MainWindow)
        self.remoteFilter_label.setObjectName(u"remoteFilter_label")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.remoteFilter_label.sizePolicy().hasHeightForWidth())
        self.remoteFilter_label.setSizePolicy(sizePolicy3)

        self.filter_gridLayout.addWidget(self.remoteFilter_label, 3, 0, 1, 1)

        self.locationFilter_label = QLabel(MainWindow)
        self.locationFilter_label.setObjectName(u"locationFilter_label")
        sizePolicy3.setHeightForWidth(self.locationFilter_label.sizePolicy().hasHeightForWidth())
        self.locationFilter_label.setSizePolicy(sizePolicy3)

        self.filter_gridLayout.addWidget(self.locationFilter_label, 2, 0, 1, 1)

        self.resultsAmount_label = QLabel(MainWindow)
        self.resultsAmount_label.setObjectName(u"resultsAmount_label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.resultsAmount_label.sizePolicy().hasHeightForWidth())
        self.resultsAmount_label.setSizePolicy(sizePolicy4)

        self.filter_gridLayout.addWidget(self.resultsAmount_label, 5, 0, 1, 1)

        self.resultsAmt_label = QLabel(MainWindow)
        self.resultsAmt_label.setObjectName(u"resultsAmt_label")

        self.filter_gridLayout.addWidget(self.resultsAmt_label, 5, 1, 1, 1)

        self.salaryFilter_label = QLabel(MainWindow)
        self.salaryFilter_label.setObjectName(u"salaryFilter_label")
        sizePolicy3.setHeightForWidth(self.salaryFilter_label.sizePolicy().hasHeightForWidth())
        self.salaryFilter_label.setSizePolicy(sizePolicy3)

        self.filter_gridLayout.addWidget(self.salaryFilter_label, 4, 0, 1, 1)

        self.keyword_label = QLabel(MainWindow)
        self.keyword_label.setObjectName(u"keyword_label")
        sizePolicy3.setHeightForWidth(self.keyword_label.sizePolicy().hasHeightForWidth())
        self.keyword_label.setSizePolicy(sizePolicy3)

        self.filter_gridLayout.addWidget(self.keyword_label, 1, 0, 1, 1)

        self.applyFilters_pushButton = QPushButton(MainWindow)
        self.applyFilters_pushButton.setObjectName(u"applyFilters_pushButton")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.applyFilters_pushButton.sizePolicy().hasHeightForWidth())
        self.applyFilters_pushButton.setSizePolicy(sizePolicy5)

        self.filter_gridLayout.addWidget(self.applyFilters_pushButton, 5, 2, 1, 1)

        self.salaryFilter_spinBox = QSpinBox(MainWindow)
        self.salaryFilter_spinBox.setObjectName(u"salaryFilter_spinBox")
        self.salaryFilter_spinBox.setMaximum(999999999)

        self.filter_gridLayout.addWidget(self.salaryFilter_spinBox, 4, 1, 1, 2)

        self.remoteFilter_checkBox = QCheckBox(MainWindow)
        self.remoteFilter_checkBox.setObjectName(u"remoteFilter_checkBox")

        self.filter_gridLayout.addWidget(self.remoteFilter_checkBox, 3, 1, 1, 1)

        self.locationFilter_comboBox = QComboBox(MainWindow)
        self.locationFilter_comboBox.setObjectName(u"locationFilter_comboBox")

        self.filter_gridLayout.addWidget(self.locationFilter_comboBox, 2, 1, 1, 2)

        self.keywordFilter_plainTextEdit = QPlainTextEdit(MainWindow)
        self.keywordFilter_plainTextEdit.setObjectName(u"keywordFilter_plainTextEdit")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.keywordFilter_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.keywordFilter_plainTextEdit.setSizePolicy(sizePolicy6)
        self.keywordFilter_plainTextEdit.setMaximumSize(QSize(16777215, 30))

        self.filter_gridLayout.addWidget(self.keywordFilter_plainTextEdit, 1, 1, 1, 2)


        self.jobslist_verticalLayout.addLayout(self.filter_gridLayout)

        self.jobs_listWidget = QListWidget(MainWindow)
        self.jobs_listWidget.setObjectName(u"jobs_listWidget")
        self.jobs_listWidget.setStyleSheet(u"QListWidget::item:hover {\n"
"    background-color: lightgray;\n"
"}\n"
"")
        self.jobs_listWidget.setSpacing(5)

        self.jobslist_verticalLayout.addWidget(self.jobs_listWidget)

        self.jobsButtons_horizontalLayout = QHBoxLayout()
        self.jobsButtons_horizontalLayout.setObjectName(u"jobsButtons_horizontalLayout")
        self.deselect_pushButton = QPushButton(MainWindow)
        self.deselect_pushButton.setObjectName(u"deselect_pushButton")

        self.jobsButtons_horizontalLayout.addWidget(self.deselect_pushButton)

        self.map_pushButton = QPushButton(MainWindow)
        self.map_pushButton.setObjectName(u"map_pushButton")

        self.jobsButtons_horizontalLayout.addWidget(self.map_pushButton)


        self.jobslist_verticalLayout.addLayout(self.jobsButtons_horizontalLayout)


        self.gridLayout_2.addLayout(self.jobslist_verticalLayout, 0, 0, 5, 1)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Jobs Navigation", None))
        self.jobdata_label.setText(QCoreApplication.translate("MainWindow", u"SELECTED JOB DATA", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Title", None))
        self.title_plainTextEdit.setPlainText("")
        self.company_label.setText(QCoreApplication.translate("MainWindow", u"Company", None))
        self.location_label.setText(QCoreApplication.translate("MainWindow", u"Location", None))
        self.postedAt_label.setText(QCoreApplication.translate("MainWindow", u"Posted at", None))
        self.salary_label.setText(QCoreApplication.translate("MainWindow", u"Salary", None))
        self.remote_label.setText(QCoreApplication.translate("MainWindow", u"Remote", None))
        self.links_label.setText(QCoreApplication.translate("MainWindow", u"Links", None))
        self.qualifications_label.setText(QCoreApplication.translate("MainWindow", u"Qualifications", None))
        self.description_label.setText(QCoreApplication.translate("MainWindow", u"Description", None))
        self.description_plainTextEdit.setPlainText("")
        self.jobs_label.setText(QCoreApplication.translate("MainWindow", u"LIST OF JOBS", None))
        self.filter_label.setText(QCoreApplication.translate("MainWindow", u"Filtering options", None))
        self.remoteFilter_label.setText(QCoreApplication.translate("MainWindow", u"Remote: ", None))
        self.locationFilter_label.setText(QCoreApplication.translate("MainWindow", u"Location: ", None))
        self.resultsAmount_label.setText(QCoreApplication.translate("MainWindow", u"Results amount:  ", None))
        self.resultsAmt_label.setText("")
        self.salaryFilter_label.setText(QCoreApplication.translate("MainWindow", u"Min Salary (yearly): ", None))
        self.keyword_label.setText(QCoreApplication.translate("MainWindow", u"Keyword: ", None))
        self.applyFilters_pushButton.setText(QCoreApplication.translate("MainWindow", u"Apply Filters", None))
        self.remoteFilter_checkBox.setText("")
        self.keywordFilter_plainTextEdit.setPlaceholderText("")
        self.deselect_pushButton.setText(QCoreApplication.translate("MainWindow", u"Deselect", None))
        self.map_pushButton.setText(QCoreApplication.translate("MainWindow", u"Map", None))
    # retranslateUi

