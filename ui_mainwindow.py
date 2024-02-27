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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QListView, QPlainTextEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(847, 719)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_2 = QGridLayout(MainWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.jobslist_verticalLayout = QVBoxLayout()
        self.jobslist_verticalLayout.setObjectName(u"jobslist_verticalLayout")
        self.jobs_label = QLabel(MainWindow)
        self.jobs_label.setObjectName(u"jobs_label")
        self.jobs_label.setMinimumSize(QSize(0, 30))

        self.jobslist_verticalLayout.addWidget(self.jobs_label)

        self.filter_horizontalLayout = QHBoxLayout()
        self.filter_horizontalLayout.setObjectName(u"filter_horizontalLayout")
        self.filter_plainTextEdit = QPlainTextEdit(MainWindow)
        self.filter_plainTextEdit.setObjectName(u"filter_plainTextEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.filter_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.filter_plainTextEdit.setSizePolicy(sizePolicy1)
        self.filter_plainTextEdit.setMaximumSize(QSize(16777215, 30))

        self.filter_horizontalLayout.addWidget(self.filter_plainTextEdit)

        self.filter_pushButton = QPushButton(MainWindow)
        self.filter_pushButton.setObjectName(u"filter_pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.filter_pushButton.sizePolicy().hasHeightForWidth())
        self.filter_pushButton.setSizePolicy(sizePolicy2)
        self.filter_pushButton.setMaximumSize(QSize(60, 16777215))

        self.filter_horizontalLayout.addWidget(self.filter_pushButton)


        self.jobslist_verticalLayout.addLayout(self.filter_horizontalLayout)

        self.jobs_listView = QListView(MainWindow)
        self.jobs_listView.setObjectName(u"jobs_listView")
        self.jobs_listView.setSpacing(10)

        self.jobslist_verticalLayout.addWidget(self.jobs_listView)

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
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.title_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.title_plainTextEdit.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.company_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.company_plainTextEdit.setSizePolicy(sizePolicy3)
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
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.links_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.links_plainTextEdit.setSizePolicy(sizePolicy4)
        self.links_plainTextEdit.setMinimumSize(QSize(0, 30))
        self.links_plainTextEdit.setMaximumSize(QSize(16777215, 60))

        self.jobdata_verticalLayout.addWidget(self.links_plainTextEdit)

        self.qualifications_label = QLabel(MainWindow)
        self.qualifications_label.setObjectName(u"qualifications_label")

        self.jobdata_verticalLayout.addWidget(self.qualifications_label)

        self.qualifications_plainTextEdit = QPlainTextEdit(MainWindow)
        self.qualifications_plainTextEdit.setObjectName(u"qualifications_plainTextEdit")
        self.qualifications_plainTextEdit.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.qualifications_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.qualifications_plainTextEdit.setSizePolicy(sizePolicy4)
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
        sizePolicy4.setHeightForWidth(self.description_plainTextEdit.sizePolicy().hasHeightForWidth())
        self.description_plainTextEdit.setSizePolicy(sizePolicy4)
        self.description_plainTextEdit.setMinimumSize(QSize(0, 30))
        self.description_plainTextEdit.setMaximumSize(QSize(16777215, 120))
        self.description_plainTextEdit.setReadOnly(True)

        self.jobdata_verticalLayout.addWidget(self.description_plainTextEdit)


        self.gridLayout_2.addLayout(self.jobdata_verticalLayout, 0, 2, 5, 1)


        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.jobs_label.setText(QCoreApplication.translate("MainWindow", u"LIST OF JOBS", None))
        self.filter_plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filter jobs", None))
        self.filter_pushButton.setText(QCoreApplication.translate("MainWindow", u"Filter", None))
        self.deselect_pushButton.setText(QCoreApplication.translate("MainWindow", u"Deselect", None))
        self.map_pushButton.setText(QCoreApplication.translate("MainWindow", u"Map", None))
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
    # retranslateUi

