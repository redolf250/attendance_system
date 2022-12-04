# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashoboardOeTqHn.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import asset_rc

class Ui_dashboard(object):
    def setupUi(self, dashboard):
        if dashboard.objectName():
            dashboard.setObjectName(u"dashboard")
        dashboard.resize(1500, 1000)
        dashboard.setMinimumSize(QSize(1500, 1000))
        dashboard.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1500, 1000))
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.drop_shadow_layout = QFrame(self.centralwidget)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setMinimumSize(QSize(1280, 1000))
        self.drop_shadow_layout.setStyleSheet(u"")
        self.drop_shadow_layout.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_layout.setFrameShadow(QFrame.Raised)
        self.drop_shadow_layout.setLineWidth(0)
        self.content_layout = QVBoxLayout(self.drop_shadow_layout)
        self.content_layout.setSpacing(0)
        self.content_layout.setObjectName(u"content_layout")
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_layout)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(0, 50))
        self.title_bar.setMaximumSize(QSize(16777215, 50))
        self.title_bar.setStyleSheet(u"\n"
"background-color: rgb(35, 35, 35);")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.other_fields = QFrame(self.title_bar)
        self.other_fields.setObjectName(u"other_fields")
        self.other_fields.setFrameShape(QFrame.NoFrame)
        self.other_fields.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.other_fields)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logo = QFrame(self.other_fields)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(100, 16777215))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.logo)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.logo)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"padding-left:5px;")
        self.label.setPixmap(QPixmap(u":/icons/asset/layers.svg"))
        self.label.setMargin(10)

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout_2.addWidget(self.logo)

        self.options = QFrame(self.other_fields)
        self.options.setObjectName(u"options")
        self.options.setFrameShape(QFrame.NoFrame)
        self.options.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.options)


        self.horizontalLayout.addWidget(self.other_fields)

        self.controls_frame = QFrame(self.title_bar)
        self.controls_frame.setObjectName(u"controls_frame")
        self.controls_frame.setMinimumSize(QSize(100, 0))
        self.controls_frame.setMaximumSize(QSize(100, 16777215))
        self.controls_frame.setFrameShape(QFrame.NoFrame)
        self.controls_frame.setFrameShadow(QFrame.Raised)
        self.btn_maximize = QPushButton(self.controls_frame)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setGeometry(QRect(40, 20, 16, 16))
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(17, 17))
        self.btn_maximize.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgba(255, 170, 0,150);\n"
"	\n"
"}")
        self.btn_minimize = QPushButton(self.controls_frame)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setGeometry(QRect(10, 20, 16, 16))
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(85, 255, 127);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgba(85, 255, 127,150);\n"
"	\n"
"}")
        self.btn_close = QPushButton(self.controls_frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setGeometry(QRect(70, 20, 16, 16))
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 0, 0);\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: rgba(255, 0, 0,150);\n"
"	\n"
"}")

        self.horizontalLayout.addWidget(self.controls_frame)


        self.content_layout.addWidget(self.title_bar)

        self.content = QFrame(self.drop_shadow_layout)
        self.content.setObjectName(u"content")
        self.content.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.content)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.content)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(70, 0))
        self.menu_frame.setMaximumSize(QSize(80, 16777215))
        self.menu_frame.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.menu_frame.setFrameShape(QFrame.NoFrame)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menu_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.menu_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, -1, -1, -1)
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 70))
        self.btn_home.setMaximumSize(QSize(16777215, 70))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/asset/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon)
        self.btn_home.setIconSize(QSize(40, 40))
        self.btn_home.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_home)

        self.btn_database = QPushButton(self.frame)
        self.btn_database.setObjectName(u"btn_database")
        self.btn_database.setMinimumSize(QSize(0, 70))
        self.btn_database.setMaximumSize(QSize(16777215, 70))
        self.btn_database.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"	padding-left:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/asset/user-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_database.setIcon(icon1)
        self.btn_database.setIconSize(QSize(45, 45))
        self.btn_database.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_database)

        self.btn_search = QPushButton(self.frame)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(0, 70))
        self.btn_search.setMaximumSize(QSize(16777215, 70))
        self.btn_search.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/asset/search.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon2)
        self.btn_search.setIconSize(QSize(40, 40))
        self.btn_search.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_search)

        self.btn_camera = QPushButton(self.frame)
        self.btn_camera.setObjectName(u"btn_camera")
        self.btn_camera.setMinimumSize(QSize(0, 70))
        self.btn_camera.setMaximumSize(QSize(16777215, 70))
        self.btn_camera.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/asset/camera.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_camera.setIcon(icon3)
        self.btn_camera.setIconSize(QSize(40, 40))
        self.btn_camera.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_camera)

        self.btn_report = QPushButton(self.frame)
        self.btn_report.setObjectName(u"btn_report")
        self.btn_report.setMinimumSize(QSize(0, 70))
        self.btn_report.setMaximumSize(QSize(16777215, 70))
        self.btn_report.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/asset/pie-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_report.setIcon(icon4)
        self.btn_report.setIconSize(QSize(40, 40))
        self.btn_report.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_report)

        self.btn_help = QPushButton(self.frame)
        self.btn_help.setObjectName(u"btn_help")
        self.btn_help.setMinimumSize(QSize(0, 70))
        self.btn_help.setMaximumSize(QSize(16777215, 70))
        self.btn_help.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-left: 3px solid;\n"
"	border-left-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border-left-color: rgb(255, 255, 255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/asset/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_help.setIcon(icon5)
        self.btn_help.setIconSize(QSize(40, 40))
        self.btn_help.setFlat(True)

        self.verticalLayout_4.addWidget(self.btn_help)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignTop)


        self.horizontalLayout_3.addWidget(self.menu_frame)

        self.content_frame = QFrame(self.content)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.NoFrame)
        self.content_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.content_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.content_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(500, 0))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setMinimumSize(QSize(200, 0))
        self.horizontalLayout_4 = QHBoxLayout(self.home)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.left_frame = QFrame(self.home)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setMinimumSize(QSize(500, 0))
        self.left_frame.setMaximumSize(QSize(400, 16777215))
        self.left_frame.setStyleSheet(u"")
        self.left_frame.setFrameShape(QFrame.NoFrame)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.left_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.info_frame = QFrame(self.left_frame)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setMinimumSize(QSize(0, 470))
        self.info_frame.setMaximumSize(QSize(16777215, 600))
        self.info_frame.setFrameShape(QFrame.NoFrame)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.image = QLabel(self.info_frame)
        self.image.setObjectName(u"image")
        self.image.setGeometry(QRect(20, 20, 261, 291))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(14)
        font1.setBold(False)
        font1.setWeight(50)
        self.image.setFont(font1)
        self.image.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.image.setAlignment(Qt.AlignCenter)
        self.firstname = QLabel(self.info_frame)
        self.firstname.setObjectName(u"firstname")
        self.firstname.setGeometry(QRect(290, 20, 191, 41))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.firstname.setFont(font2)
        self.firstname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.firstname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.middlename = QLabel(self.info_frame)
        self.middlename.setObjectName(u"middlename")
        self.middlename.setGeometry(QRect(290, 70, 191, 41))
        self.middlename.setFont(font2)
        self.middlename.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.middlename.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.lastname = QLabel(self.info_frame)
        self.lastname.setObjectName(u"lastname")
        self.lastname.setGeometry(QRect(290, 120, 191, 41))
        self.lastname.setFont(font2)
        self.lastname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.lastname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.refrence = QLabel(self.info_frame)
        self.refrence.setObjectName(u"refrence")
        self.refrence.setGeometry(QRect(290, 170, 191, 41))
        self.refrence.setFont(font2)
        self.refrence.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.refrence.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.index = QLabel(self.info_frame)
        self.index.setObjectName(u"index")
        self.index.setGeometry(QRect(290, 220, 191, 41))
        self.index.setFont(font2)
        self.index.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.index.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.coledge = QLabel(self.info_frame)
        self.coledge.setObjectName(u"coledge")
        self.coledge.setGeometry(QRect(290, 270, 191, 41))
        self.coledge.setFont(font2)
        self.coledge.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.coledge.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.validity = QLabel(self.info_frame)
        self.validity.setObjectName(u"validity")
        self.validity.setGeometry(QRect(20, 320, 261, 41))
        self.validity.setFont(font2)
        self.validity.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.validity.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.nationality = QLabel(self.info_frame)
        self.nationality.setObjectName(u"nationality")
        self.nationality.setGeometry(QRect(290, 320, 191, 41))
        self.nationality.setFont(font2)
        self.nationality.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.nationality.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.year = QLabel(self.info_frame)
        self.year.setObjectName(u"year")
        self.year.setGeometry(QRect(20, 370, 151, 41))
        self.year.setFont(font2)
        self.year.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.year.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.program = QLabel(self.info_frame)
        self.program.setObjectName(u"program")
        self.program.setGeometry(QRect(180, 370, 301, 41))
        self.program.setFont(font2)
        self.program.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.program.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.last_out = QLabel(self.info_frame)
        self.last_out.setObjectName(u"last_out")
        self.last_out.setGeometry(QRect(20, 420, 291, 41))
        self.last_out.setFont(font2)
        self.last_out.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.last_out.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.image_2 = QLabel(self.info_frame)
        self.image_2.setObjectName(u"image_2")
        self.image_2.setGeometry(QRect(10, 10, 481, 461))
        self.image_2.setFont(font1)
        self.image_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.image_2.setAlignment(Qt.AlignCenter)
        self.last_in = QLabel(self.info_frame)
        self.last_in.setObjectName(u"last_in")
        self.last_in.setGeometry(QRect(320, 420, 161, 41))
        self.last_in.setFont(font2)
        self.last_in.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"\n"
"}")
        self.last_in.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.image_2.raise_()
        self.image.raise_()
        self.firstname.raise_()
        self.middlename.raise_()
        self.lastname.raise_()
        self.refrence.raise_()
        self.index.raise_()
        self.coledge.raise_()
        self.validity.raise_()
        self.nationality.raise_()
        self.year.raise_()
        self.program.raise_()
        self.last_out.raise_()
        self.last_in.raise_()

        self.verticalLayout_6.addWidget(self.info_frame)

        self.frame_3 = QFrame(self.left_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_notification = QLabel(self.frame_3)
        self.label_notification.setObjectName(u"label_notification")
        self.label_notification.setGeometry(QRect(10, 360, 481, 101))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_notification.setFont(font3)
        self.label_notification.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.label_notification.setAlignment(Qt.AlignCenter)
        self.date_frame_2 = QFrame(self.frame_3)
        self.date_frame_2.setObjectName(u"date_frame_2")
        self.date_frame_2.setGeometry(QRect(10, 10, 481, 51))
        self.date_frame_2.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.date_frame_2.setFrameShape(QFrame.StyledPanel)
        self.date_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.date_frame_2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.face_auth = QRadioButton(self.date_frame_2)
        self.face_auth.setObjectName(u"face_auth")
        font4 = QFont()
        font4.setFamily(u"Arial")
        font4.setPointSize(10)
        self.face_auth.setFont(font4)
        self.face_auth.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/asset/user-check.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.face_auth.setIcon(icon6)
        self.face_auth.setChecked(False)

        self.horizontalLayout_13.addWidget(self.face_auth)

        self.qr_code_auth = QRadioButton(self.date_frame_2)
        self.qr_code_auth.setObjectName(u"qr_code_auth")
        self.qr_code_auth.setFont(font4)
        self.qr_code_auth.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.qr_code_auth.setIcon(icon6)
        self.qr_code_auth.setChecked(True)

        self.horizontalLayout_13.addWidget(self.qr_code_auth)

        self.biometric_auth = QRadioButton(self.date_frame_2)
        self.biometric_auth.setObjectName(u"biometric_auth")
        self.biometric_auth.setFont(font4)
        self.biometric_auth.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.biometric_auth.setIcon(icon6)
        self.biometric_auth.setChecked(False)

        self.horizontalLayout_13.addWidget(self.biometric_auth)

        self.camera_ip = QLineEdit(self.frame_3)
        self.camera_ip.setObjectName(u"camera_ip")
        self.camera_ip.setGeometry(QRect(20, 110, 461, 51))
        font5 = QFont()
        font5.setPointSize(10)
        self.camera_ip.setFont(font5)
        self.camera_ip.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.camera_ip.setClearButtonEnabled(True)
        self.btn_connect_detect = QPushButton(self.frame_3)
        self.btn_connect_detect.setObjectName(u"btn_connect_detect")
        self.btn_connect_detect.setGeometry(QRect(20, 180, 131, 41))
        self.btn_connect_detect.setFont(font5)
        self.btn_connect_detect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/asset/video.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_connect_detect.setIcon(icon7)
        self.btn_connect_detect.setIconSize(QSize(30, 30))
        self.btn_connect_detect.setFlat(True)
        self.label_27 = QLabel(self.frame_3)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setGeometry(QRect(30, 120, 41, 31))
        self.label_27.setPixmap(QPixmap(u":/icons/asset/video.svg"))
        self.btn_disconnect = QPushButton(self.frame_3)
        self.btn_disconnect.setObjectName(u"btn_disconnect")
        self.btn_disconnect.setGeometry(QRect(160, 180, 141, 41))
        self.btn_disconnect.setFont(font5)
        self.btn_disconnect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/asset/video-off.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_disconnect.setIcon(icon8)
        self.btn_disconnect.setIconSize(QSize(30, 30))
        self.btn_disconnect.setFlat(True)
        self.comboBox = QComboBox(self.frame_3)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(310, 180, 171, 38))
        self.comboBox.setMinimumSize(QSize(0, 38))
        self.comboBox.setMaximumSize(QSize(16777215, 38))
        self.comboBox.setFont(font5)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 5px;\n"
"}")
        self.comboBox.setFrame(False)
        self.firstname_23 = QLabel(self.frame_3)
        self.firstname_23.setObjectName(u"firstname_23")
        self.firstname_23.setGeometry(QRect(10, 80, 481, 161))
        font6 = QFont()
        font6.setFamily(u"Arial")
        font6.setPointSize(10)
        font6.setBold(False)
        font6.setWeight(50)
        self.firstname_23.setFont(font6)
        self.firstname_23.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.firstname_23.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.firstname_24 = QLabel(self.frame_3)
        self.firstname_24.setObjectName(u"firstname_24")
        self.firstname_24.setGeometry(QRect(10, 260, 481, 81))
        self.firstname_24.setFont(font6)
        self.firstname_24.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.firstname_24.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.btn_open_exit_camera_ui = QPushButton(self.frame_3)
        self.btn_open_exit_camera_ui.setObjectName(u"btn_open_exit_camera_ui")
        self.btn_open_exit_camera_ui.setGeometry(QRect(20, 280, 151, 41))
        self.btn_open_exit_camera_ui.setFont(font5)
        self.btn_open_exit_camera_ui.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_open_exit_camera_ui.setIcon(icon7)
        self.btn_open_exit_camera_ui.setIconSize(QSize(30, 30))
        self.btn_open_exit_camera_ui.setFlat(True)
        self.btn_clear_label = QPushButton(self.frame_3)
        self.btn_clear_label.setObjectName(u"btn_clear_label")
        self.btn_clear_label.setGeometry(QRect(180, 280, 141, 41))
        self.btn_clear_label.setFont(font5)
        self.btn_clear_label.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/asset/delete.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear_label.setIcon(icon9)
        self.btn_clear_label.setIconSize(QSize(30, 30))
        self.btn_clear_label.setFlat(True)
        self.btn_init_face_auth = QPushButton(self.frame_3)
        self.btn_init_face_auth.setObjectName(u"btn_init_face_auth")
        self.btn_init_face_auth.setGeometry(QRect(330, 280, 151, 41))
        self.btn_init_face_auth.setFont(font5)
        self.btn_init_face_auth.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/asset/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_init_face_auth.setIcon(icon10)
        self.btn_init_face_auth.setIconSize(QSize(30, 30))
        self.btn_init_face_auth.setFlat(True)
        self.firstname_23.raise_()
        self.label_notification.raise_()
        self.date_frame_2.raise_()
        self.camera_ip.raise_()
        self.btn_connect_detect.raise_()
        self.label_27.raise_()
        self.btn_disconnect.raise_()
        self.comboBox.raise_()
        self.firstname_24.raise_()
        self.btn_open_exit_camera_ui.raise_()
        self.btn_clear_label.raise_()
        self.btn_init_face_auth.raise_()

        self.verticalLayout_6.addWidget(self.frame_3)


        self.horizontalLayout_4.addWidget(self.left_frame)

        self.right_frame = QFrame(self.home)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setMinimumSize(QSize(0, 700))
        self.right_frame.setFrameShape(QFrame.NoFrame)
        self.right_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.right_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.camera_frame = QFrame(self.right_frame)
        self.camera_frame.setObjectName(u"camera_frame")
        self.camera_frame.setMinimumSize(QSize(0, 700))
        self.camera_frame.setMaximumSize(QSize(16777215, 700))
        self.camera_frame.setFrameShape(QFrame.NoFrame)
        self.camera_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.camera_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.camera_view = QLabel(self.camera_frame)
        self.camera_view.setObjectName(u"camera_view")
        self.camera_view.setMinimumSize(QSize(0, 680))
        self.camera_view.setMaximumSize(QSize(16777215, 680))
        self.camera_view.setFont(font1)
        self.camera_view.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.camera_view.setPixmap(QPixmap(u":/icons/asset/camera-off.svg"))
        self.camera_view.setAlignment(Qt.AlignCenter)
        self.camera_view.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.camera_view)


        self.verticalLayout_7.addWidget(self.camera_frame)

        self.properties_frame = QFrame(self.right_frame)
        self.properties_frame.setObjectName(u"properties_frame")
        self.properties_frame.setFrameShape(QFrame.NoFrame)
        self.properties_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.properties_frame)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.properties_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(450, 16777215))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.erosion = QSlider(self.frame_4)
        self.erosion.setObjectName(u"erosion")
        self.erosion.setMaximum(99)
        self.erosion.setSingleStep(3)
        self.erosion.setPageStep(3)
        self.erosion.setValue(3)
        self.erosion.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.erosion, 3, 1, 1, 1)

        self.thresh_value = QLabel(self.frame_4)
        self.thresh_value.setObjectName(u"thresh_value")
        self.thresh_value.setMinimumSize(QSize(50, 0))
        self.thresh_value.setMaximumSize(QSize(50, 16777215))
        self.thresh_value.setFont(font6)
        self.thresh_value.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.thresh_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.thresh_value, 4, 2, 1, 1)

        self.hsv_value = QLabel(self.frame_4)
        self.hsv_value.setObjectName(u"hsv_value")
        self.hsv_value.setMinimumSize(QSize(50, 0))
        self.hsv_value.setMaximumSize(QSize(50, 16777215))
        self.hsv_value.setFont(font6)
        self.hsv_value.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.hsv_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.hsv_value, 5, 2, 1, 1)

        self.dilation_value = QLabel(self.frame_4)
        self.dilation_value.setObjectName(u"dilation_value")
        self.dilation_value.setMinimumSize(QSize(50, 0))
        self.dilation_value.setMaximumSize(QSize(50, 16777215))
        self.dilation_value.setFont(font6)
        self.dilation_value.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.dilation_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.dilation_value, 2, 2, 1, 1)

        self.entry_unimp_label = QLabel(self.frame_4)
        self.entry_unimp_label.setObjectName(u"entry_unimp_label")
        self.entry_unimp_label.setFont(font6)
        self.entry_unimp_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.entry_unimp_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.entry_unimp_label, 5, 0, 1, 1)

        self.brigthness = QSlider(self.frame_4)
        self.brigthness.setObjectName(u"brigthness")
        self.brigthness.setMaximum(100)
        self.brigthness.setValue(30)
        self.brigthness.setSliderPosition(30)
        self.brigthness.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.brigthness, 5, 1, 1, 1)

        self.entry_dilation_label = QLabel(self.frame_4)
        self.entry_dilation_label.setObjectName(u"entry_dilation_label")
        self.entry_dilation_label.setFont(font6)
        self.entry_dilation_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.entry_dilation_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.entry_dilation_label, 2, 0, 1, 1)

        self.entry_erosion_label = QLabel(self.frame_4)
        self.entry_erosion_label.setObjectName(u"entry_erosion_label")
        self.entry_erosion_label.setFont(font6)
        self.entry_erosion_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.entry_erosion_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.entry_erosion_label, 3, 0, 1, 1)

        self.erosion_value = QLabel(self.frame_4)
        self.erosion_value.setObjectName(u"erosion_value")
        self.erosion_value.setMinimumSize(QSize(50, 0))
        self.erosion_value.setMaximumSize(QSize(50, 16777215))
        self.erosion_value.setFont(font6)
        self.erosion_value.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.erosion_value.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.erosion_value, 3, 2, 1, 1)

        self.threshold = QSlider(self.frame_4)
        self.threshold.setObjectName(u"threshold")
        self.threshold.setMaximum(100)
        self.threshold.setValue(1)
        self.threshold.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.threshold, 4, 1, 1, 1)

        self.entry_blur_label = QLabel(self.frame_4)
        self.entry_blur_label.setObjectName(u"entry_blur_label")
        self.entry_blur_label.setFont(font6)
        self.entry_blur_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.entry_blur_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.entry_blur_label, 4, 0, 1, 1)

        self.dilation = QSlider(self.frame_4)
        self.dilation.setObjectName(u"dilation")
        self.dilation.setMaximum(100)
        self.dilation.setValue(1)
        self.dilation.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.dilation, 2, 1, 1, 1)

        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 20))
        self.label_14.setMaximumSize(QSize(16777215, 20))
        self.label_14.setFont(font4)
        self.label_14.setStyleSheet(u"")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_14, 1, 0, 1, 3)


        self.horizontalLayout_10.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_18 = QLabel(self.frame_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 20))
        self.label_18.setMaximumSize(QSize(16777215, 20))
        self.label_18.setFont(font4)
        self.label_18.setStyleSheet(u"")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_18, 0, 1, 1, 1)

        self.exit_dilation_label = QLabel(self.frame_5)
        self.exit_dilation_label.setObjectName(u"exit_dilation_label")
        self.exit_dilation_label.setFont(font6)
        self.exit_dilation_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.exit_dilation_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.exit_dilation_label, 1, 0, 1, 1)

        self.average_blur = QSlider(self.frame_5)
        self.average_blur.setObjectName(u"average_blur")
        self.average_blur.setMaximum(100)
        self.average_blur.setValue(1)
        self.average_blur.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.average_blur, 1, 1, 1, 1)

        self.avg_blur_value = QLabel(self.frame_5)
        self.avg_blur_value.setObjectName(u"avg_blur_value")
        self.avg_blur_value.setMinimumSize(QSize(50, 0))
        self.avg_blur_value.setMaximumSize(QSize(50, 16777215))
        self.avg_blur_value.setFont(font6)
        self.avg_blur_value.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.avg_blur_value.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.avg_blur_value, 1, 2, 1, 1)

        self.exit_erosion_label = QLabel(self.frame_5)
        self.exit_erosion_label.setObjectName(u"exit_erosion_label")
        self.exit_erosion_label.setFont(font6)
        self.exit_erosion_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.exit_erosion_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.exit_erosion_label, 2, 0, 1, 1)

        self.sharpness = QSlider(self.frame_5)
        self.sharpness.setObjectName(u"sharpness")
        self.sharpness.setMaximum(100)
        self.sharpness.setValue(50)
        self.sharpness.setSliderPosition(50)
        self.sharpness.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.sharpness, 2, 1, 1, 1)

        self.gb_blur_value = QLabel(self.frame_5)
        self.gb_blur_value.setObjectName(u"gb_blur_value")
        self.gb_blur_value.setMinimumSize(QSize(50, 0))
        self.gb_blur_value.setMaximumSize(QSize(50, 16777215))
        self.gb_blur_value.setFont(font6)
        self.gb_blur_value.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.gb_blur_value.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.gb_blur_value, 2, 2, 1, 1)

        self.exit_blur_label = QLabel(self.frame_5)
        self.exit_blur_label.setObjectName(u"exit_blur_label")
        self.exit_blur_label.setFont(font6)
        self.exit_blur_label.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.exit_blur_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.exit_blur_label, 3, 0, 1, 1)

        self.contrast = QSlider(self.frame_5)
        self.contrast.setObjectName(u"contrast")
        self.contrast.setMaximum(100)
        self.contrast.setValue(60)
        self.contrast.setSliderPosition(60)
        self.contrast.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.contrast, 3, 1, 1, 1)

        self.bb_blur_value = QLabel(self.frame_5)
        self.bb_blur_value.setObjectName(u"bb_blur_value")
        self.bb_blur_value.setMinimumSize(QSize(50, 0))
        self.bb_blur_value.setMaximumSize(QSize(50, 16777215))
        self.bb_blur_value.setFont(font6)
        self.bb_blur_value.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.bb_blur_value.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.bb_blur_value, 3, 2, 1, 1)

        self.exit_umimpl = QLabel(self.frame_5)
        self.exit_umimpl.setObjectName(u"exit_umimpl")
        self.exit_umimpl.setFont(font6)
        self.exit_umimpl.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.exit_umimpl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.exit_umimpl, 4, 0, 1, 1)

        self.kernel = QSlider(self.frame_5)
        self.kernel.setObjectName(u"kernel")
        self.kernel.setMaximum(10)
        self.kernel.setSingleStep(1)
        self.kernel.setPageStep(1)
        self.kernel.setValue(1)
        self.kernel.setSliderPosition(1)
        self.kernel.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.kernel, 4, 1, 1, 1)

        self.kernel_value = QLabel(self.frame_5)
        self.kernel_value.setObjectName(u"kernel_value")
        self.kernel_value.setMinimumSize(QSize(50, 0))
        self.kernel_value.setMaximumSize(QSize(50, 16777215))
        self.kernel_value.setFont(font6)
        self.kernel_value.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.kernel_value.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.kernel_value, 4, 2, 1, 1)


        self.horizontalLayout_10.addWidget(self.frame_5)


        self.verticalLayout_11.addWidget(self.frame_2)


        self.verticalLayout_7.addWidget(self.properties_frame)


        self.horizontalLayout_4.addWidget(self.right_frame)

        self.stackedWidget.addWidget(self.home)
        self.search = QWidget()
        self.search.setObjectName(u"search")
        self.horizontalLayout_5 = QHBoxLayout(self.search)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.left_frame_2 = QFrame(self.search)
        self.left_frame_2.setObjectName(u"left_frame_2")
        self.left_frame_2.setMinimumSize(QSize(500, 0))
        self.left_frame_2.setMaximumSize(QSize(500, 16777215))
        self.left_frame_2.setFrameShape(QFrame.NoFrame)
        self.left_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.left_frame_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, -1, 0, 0)
        self.top = QFrame(self.left_frame_2)
        self.top.setObjectName(u"top")
        self.top.setMinimumSize(QSize(0, 510))
        self.top.setMaximumSize(QSize(500, 520))
        self.top.setFrameShape(QFrame.NoFrame)
        self.top.setFrameShadow(QFrame.Raised)
        self.db_validity = QLabel(self.top)
        self.db_validity.setObjectName(u"db_validity")
        self.db_validity.setGeometry(QRect(20, 400, 261, 41))
        self.db_validity.setFont(font2)
        self.db_validity.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_validity.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_refrence = QLabel(self.top)
        self.db_refrence.setObjectName(u"db_refrence")
        self.db_refrence.setGeometry(QRect(290, 250, 191, 41))
        self.db_refrence.setFont(font2)
        self.db_refrence.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_refrence.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_year = QLabel(self.top)
        self.db_year.setObjectName(u"db_year")
        self.db_year.setGeometry(QRect(20, 450, 151, 41))
        self.db_year.setFont(font2)
        self.db_year.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_year.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_nationality = QLabel(self.top)
        self.db_nationality.setObjectName(u"db_nationality")
        self.db_nationality.setGeometry(QRect(290, 400, 191, 41))
        self.db_nationality.setFont(font2)
        self.db_nationality.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_nationality.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_image_data = QLabel(self.top)
        self.db_image_data.setObjectName(u"db_image_data")
        self.db_image_data.setGeometry(QRect(20, 100, 261, 291))
        self.db_image_data.setFont(font1)
        self.db_image_data.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_image_data.setAlignment(Qt.AlignCenter)
        self.db_lastname = QLabel(self.top)
        self.db_lastname.setObjectName(u"db_lastname")
        self.db_lastname.setGeometry(QRect(290, 200, 191, 41))
        self.db_lastname.setFont(font2)
        self.db_lastname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_lastname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_middlename = QLabel(self.top)
        self.db_middlename.setObjectName(u"db_middlename")
        self.db_middlename.setGeometry(QRect(290, 150, 191, 41))
        self.db_middlename.setFont(font2)
        self.db_middlename.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_middlename.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_firstname = QLabel(self.top)
        self.db_firstname.setObjectName(u"db_firstname")
        self.db_firstname.setGeometry(QRect(290, 100, 191, 41))
        self.db_firstname.setFont(font2)
        self.db_firstname.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_firstname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_index = QLabel(self.top)
        self.db_index.setObjectName(u"db_index")
        self.db_index.setGeometry(QRect(290, 300, 191, 41))
        self.db_index.setFont(font2)
        self.db_index.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_index.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_programe = QLabel(self.top)
        self.db_programe.setObjectName(u"db_programe")
        self.db_programe.setGeometry(QRect(180, 450, 301, 41))
        self.db_programe.setFont(font2)
        self.db_programe.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_programe.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.db_college = QLabel(self.top)
        self.db_college.setObjectName(u"db_college")
        self.db_college.setGeometry(QRect(290, 350, 191, 41))
        self.db_college.setFont(font2)
        self.db_college.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.db_college.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.search_box = QLineEdit(self.top)
        self.search_box.setObjectName(u"search_box")
        self.search_box.setGeometry(QRect(20, 10, 321, 51))
        self.search_box.setFont(font5)
        self.search_box.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.search_box.setClearButtonEnabled(True)
        self.btn_search_page = QPushButton(self.top)
        self.btn_search_page.setObjectName(u"btn_search_page")
        self.btn_search_page.setGeometry(QRect(350, 10, 131, 51))
        self.btn_search_page.setFont(font5)
        self.btn_search_page.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_search_page.setIcon(icon2)
        self.btn_search_page.setIconSize(QSize(30, 30))
        self.btn_search_page.setFlat(True)
        self.label_29 = QLabel(self.top)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setGeometry(QRect(10, 0, 481, 71))
        self.label_29.setFont(font3)
        self.label_29.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_29.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.image_3 = QLabel(self.top)
        self.image_3.setObjectName(u"image_3")
        self.image_3.setGeometry(QRect(10, 80, 481, 431))
        self.image_3.setFont(font1)
        self.image_3.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.image_3.setAlignment(Qt.AlignCenter)
        self.image_3.raise_()
        self.label_29.raise_()
        self.db_validity.raise_()
        self.db_refrence.raise_()
        self.db_year.raise_()
        self.db_nationality.raise_()
        self.db_image_data.raise_()
        self.db_lastname.raise_()
        self.db_middlename.raise_()
        self.db_firstname.raise_()
        self.db_index.raise_()
        self.db_programe.raise_()
        self.db_college.raise_()
        self.search_box.raise_()
        self.btn_search_page.raise_()

        self.verticalLayout_9.addWidget(self.top)

        self.bottom = QFrame(self.left_frame_2)
        self.bottom.setObjectName(u"bottom")
        self.bottom.setMinimumSize(QSize(0, 300))
        self.bottom.setMaximumSize(QSize(16777215, 500))
        self.bottom.setFrameShape(QFrame.NoFrame)
        self.frame_6 = QFrame(self.bottom)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(20, 170, 461, 241))
        self.frame_6.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.calendarWidget = QCalendarWidget(self.frame_6)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)

        self.verticalLayout_12.addWidget(self.calendarWidget)

        self.start_date = QRadioButton(self.bottom)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setGeometry(QRect(20, 80, 95, 20))
        self.start_date.setFont(font4)
        self.start_date.setStyleSheet(u"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"}")
        self.start_date.setChecked(True)
        self.end_date = QRadioButton(self.bottom)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setGeometry(QRect(140, 80, 95, 20))
        self.end_date.setFont(font4)
        self.end_date.setStyleSheet(u"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"}")
        self.db_start_date = QLineEdit(self.bottom)
        self.db_start_date.setObjectName(u"db_start_date")
        self.db_start_date.setGeometry(QRect(20, 110, 211, 51))
        self.db_start_date.setFont(font5)
        self.db_start_date.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(35, 35, 35);\n"
"	border-radius:15px;\n"
"	padding-left: 45px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.db_start_date.setClearButtonEnabled(True)
        self.db_end_date = QLineEdit(self.bottom)
        self.db_end_date.setObjectName(u"db_end_date")
        self.db_end_date.setGeometry(QRect(260, 110, 221, 51))
        self.db_end_date.setFont(font5)
        self.db_end_date.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(35, 35, 35);\n"
"	border-radius:15px;\n"
"	padding-left: 45px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.db_end_date.setClearButtonEnabled(True)
        self.label_25 = QLabel(self.bottom)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(30, 120, 31, 31))
        self.label_25.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.label_30 = QLabel(self.bottom)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setGeometry(QRect(10, 70, 481, 350))
        self.label_30.setMinimumSize(QSize(0, 345))
        self.label_30.setFont(font3)
        self.label_30.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_30.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_reload = QPushButton(self.bottom)
        self.btn_reload.setObjectName(u"btn_reload")
        self.btn_reload.setGeometry(QRect(340, 10, 141, 41))
        self.btn_reload.setFont(font5)
        self.btn_reload.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/asset/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reload.setIcon(icon11)
        self.btn_reload.setIconSize(QSize(30, 30))
        self.btn_reload.setFlat(True)
        self.btn_print = QPushButton(self.bottom)
        self.btn_print.setObjectName(u"btn_print")
        self.btn_print.setGeometry(QRect(20, 10, 151, 41))
        self.btn_print.setFont(font5)
        self.btn_print.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/asset/printer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_print.setIcon(icon12)
        self.btn_print.setIconSize(QSize(30, 30))
        self.btn_print.setFlat(True)
        self.btn_dump_csv = QPushButton(self.bottom)
        self.btn_dump_csv.setObjectName(u"btn_dump_csv")
        self.btn_dump_csv.setGeometry(QRect(190, 10, 131, 41))
        self.btn_dump_csv.setFont(font5)
        self.btn_dump_csv.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/asset/file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_dump_csv.setIcon(icon13)
        self.btn_dump_csv.setIconSize(QSize(30, 30))
        self.btn_dump_csv.setFlat(True)
        self.label_26 = QLabel(self.bottom)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(270, 120, 31, 31))
        self.label_26.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.label_40 = QLabel(self.bottom)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(10, -10, 481, 71))
        self.label_40.setFont(font3)
        self.label_40.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_40.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_40.raise_()
        self.label_30.raise_()
        self.frame_6.raise_()
        self.start_date.raise_()
        self.end_date.raise_()
        self.db_start_date.raise_()
        self.label_25.raise_()
        self.db_end_date.raise_()
        self.btn_reload.raise_()
        self.btn_print.raise_()
        self.btn_dump_csv.raise_()
        self.label_26.raise_()

        self.verticalLayout_9.addWidget(self.bottom)


        self.horizontalLayout_5.addWidget(self.left_frame_2)

        self.rigth_frame = QFrame(self.search)
        self.rigth_frame.setObjectName(u"rigth_frame")
        self.rigth_frame.setStyleSheet(u"")
        self.rigth_frame.setFrameShape(QFrame.StyledPanel)
        self.rigth_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.rigth_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, -1, -1, -1)
        self.tableWidget = QTableWidget(self.rigth_frame)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font5);
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font5);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font5);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font5);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        font7 = QFont()
        font7.setPointSize(10)
        font7.setBold(False)
        font7.setWeight(50)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font7);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font7);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setLayoutDirection(Qt.LeftToRight)
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.tableWidget.setFrameShape(QFrame.Panel)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setAutoScrollMargin(5)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(60)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(135)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(30)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_9.addWidget(self.tableWidget)


        self.horizontalLayout_5.addWidget(self.rigth_frame)

        self.stackedWidget.addWidget(self.search)
        self.camera = QWidget()
        self.camera.setObjectName(u"camera")
        self.horizontalLayout_6 = QHBoxLayout(self.camera)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.left_child = QFrame(self.camera)
        self.left_child.setObjectName(u"left_child")
        self.left_child.setMaximumSize(QSize(450, 16777215))
        self.left_child.setFrameShape(QFrame.NoFrame)
        self.left_child.setFrameShadow(QFrame.Plain)
        self.firstname_25 = QLabel(self.left_child)
        self.firstname_25.setObjectName(u"firstname_25")
        self.firstname_25.setGeometry(QRect(10, 10, 441, 171))
        self.firstname_25.setFont(font6)
        self.firstname_25.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.firstname_25.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.btn_camera_one_connect = QPushButton(self.left_child)
        self.btn_camera_one_connect.setObjectName(u"btn_camera_one_connect")
        self.btn_camera_one_connect.setGeometry(QRect(20, 120, 131, 41))
        self.btn_camera_one_connect.setFont(font5)
        self.btn_camera_one_connect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_camera_one_connect.setIcon(icon7)
        self.btn_camera_one_connect.setIconSize(QSize(30, 30))
        self.btn_camera_one_connect.setFlat(True)
        self.btn_camera_one_disconnect = QPushButton(self.left_child)
        self.btn_camera_one_disconnect.setObjectName(u"btn_camera_one_disconnect")
        self.btn_camera_one_disconnect.setGeometry(QRect(160, 120, 141, 41))
        self.btn_camera_one_disconnect.setFont(font5)
        self.btn_camera_one_disconnect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_camera_one_disconnect.setIcon(icon8)
        self.btn_camera_one_disconnect.setIconSize(QSize(30, 30))
        self.btn_camera_one_disconnect.setFlat(True)
        self.camera_one_comboBox = QComboBox(self.left_child)
        self.camera_one_comboBox.addItem("")
        self.camera_one_comboBox.addItem("")
        self.camera_one_comboBox.addItem("")
        self.camera_one_comboBox.addItem("")
        self.camera_one_comboBox.addItem("")
        self.camera_one_comboBox.addItem("")
        self.camera_one_comboBox.setObjectName(u"camera_one_comboBox")
        self.camera_one_comboBox.setGeometry(QRect(330, 50, 111, 50))
        self.camera_one_comboBox.setMinimumSize(QSize(0, 50))
        self.camera_one_comboBox.setMaximumSize(QSize(16777215, 50))
        self.camera_one_comboBox.setFont(font5)
        self.camera_one_comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}")
        self.camera_one_comboBox.setFrame(False)
        self.camera_one_id_ip = QLineEdit(self.left_child)
        self.camera_one_id_ip.setObjectName(u"camera_one_id_ip")
        self.camera_one_id_ip.setGeometry(QRect(20, 50, 301, 51))
        self.camera_one_id_ip.setFont(font5)
        self.camera_one_id_ip.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.camera_one_id_ip.setClearButtonEnabled(True)
        self.label_31 = QLabel(self.left_child)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setGeometry(QRect(30, 60, 41, 31))
        self.label_31.setPixmap(QPixmap(u":/icons/asset/video.svg"))
        self.btn_camera_two_disconnect = QPushButton(self.left_child)
        self.btn_camera_two_disconnect.setObjectName(u"btn_camera_two_disconnect")
        self.btn_camera_two_disconnect.setGeometry(QRect(160, 330, 141, 41))
        self.btn_camera_two_disconnect.setFont(font5)
        self.btn_camera_two_disconnect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_camera_two_disconnect.setIcon(icon8)
        self.btn_camera_two_disconnect.setIconSize(QSize(30, 30))
        self.btn_camera_two_disconnect.setFlat(True)
        self.camera_two_id_ip = QLineEdit(self.left_child)
        self.camera_two_id_ip.setObjectName(u"camera_two_id_ip")
        self.camera_two_id_ip.setGeometry(QRect(20, 260, 301, 51))
        self.camera_two_id_ip.setFont(font5)
        self.camera_two_id_ip.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.camera_two_id_ip.setClearButtonEnabled(True)
        self.btn_camera_two_connect = QPushButton(self.left_child)
        self.btn_camera_two_connect.setObjectName(u"btn_camera_two_connect")
        self.btn_camera_two_connect.setGeometry(QRect(20, 330, 131, 41))
        self.btn_camera_two_connect.setFont(font5)
        self.btn_camera_two_connect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_camera_two_connect.setIcon(icon7)
        self.btn_camera_two_connect.setIconSize(QSize(30, 30))
        self.btn_camera_two_connect.setFlat(True)
        self.firstname_26 = QLabel(self.left_child)
        self.firstname_26.setObjectName(u"firstname_26")
        self.firstname_26.setGeometry(QRect(10, 220, 441, 171))
        self.firstname_26.setFont(font6)
        self.firstname_26.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.firstname_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_32 = QLabel(self.left_child)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setGeometry(QRect(30, 270, 41, 31))
        self.label_32.setPixmap(QPixmap(u":/icons/asset/video.svg"))
        self.btn_camera_three_disconnect = QPushButton(self.left_child)
        self.btn_camera_three_disconnect.setObjectName(u"btn_camera_three_disconnect")
        self.btn_camera_three_disconnect.setGeometry(QRect(160, 540, 141, 41))
        self.btn_camera_three_disconnect.setFont(font5)
        self.btn_camera_three_disconnect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_camera_three_disconnect.setIcon(icon8)
        self.btn_camera_three_disconnect.setIconSize(QSize(30, 30))
        self.btn_camera_three_disconnect.setFlat(True)
        self.camera_three_id_ip = QLineEdit(self.left_child)
        self.camera_three_id_ip.setObjectName(u"camera_three_id_ip")
        self.camera_three_id_ip.setGeometry(QRect(20, 470, 301, 51))
        self.camera_three_id_ip.setFont(font5)
        self.camera_three_id_ip.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.camera_three_id_ip.setClearButtonEnabled(True)
        self.btn_camera_three_connect = QPushButton(self.left_child)
        self.btn_camera_three_connect.setObjectName(u"btn_camera_three_connect")
        self.btn_camera_three_connect.setGeometry(QRect(20, 540, 131, 41))
        self.btn_camera_three_connect.setFont(font5)
        self.btn_camera_three_connect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_camera_three_connect.setIcon(icon7)
        self.btn_camera_three_connect.setIconSize(QSize(30, 30))
        self.btn_camera_three_connect.setFlat(True)
        self.firstname_27 = QLabel(self.left_child)
        self.firstname_27.setObjectName(u"firstname_27")
        self.firstname_27.setGeometry(QRect(10, 430, 441, 171))
        self.firstname_27.setFont(font6)
        self.firstname_27.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.firstname_27.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_33 = QLabel(self.left_child)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setGeometry(QRect(30, 480, 41, 31))
        self.label_33.setPixmap(QPixmap(u":/icons/asset/video.svg"))
        self.btn_camera_four_disconnect = QPushButton(self.left_child)
        self.btn_camera_four_disconnect.setObjectName(u"btn_camera_four_disconnect")
        self.btn_camera_four_disconnect.setGeometry(QRect(160, 750, 141, 41))
        self.btn_camera_four_disconnect.setFont(font5)
        self.btn_camera_four_disconnect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_camera_four_disconnect.setIcon(icon8)
        self.btn_camera_four_disconnect.setIconSize(QSize(30, 30))
        self.btn_camera_four_disconnect.setFlat(True)
        self.camera_four_id_ip = QLineEdit(self.left_child)
        self.camera_four_id_ip.setObjectName(u"camera_four_id_ip")
        self.camera_four_id_ip.setGeometry(QRect(20, 680, 301, 51))
        self.camera_four_id_ip.setFont(font5)
        self.camera_four_id_ip.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.camera_four_id_ip.setClearButtonEnabled(True)
        self.btn_camera_four_connect = QPushButton(self.left_child)
        self.btn_camera_four_connect.setObjectName(u"btn_camera_four_connect")
        self.btn_camera_four_connect.setGeometry(QRect(20, 750, 131, 41))
        self.btn_camera_four_connect.setFont(font5)
        self.btn_camera_four_connect.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_camera_four_connect.setIcon(icon7)
        self.btn_camera_four_connect.setIconSize(QSize(30, 30))
        self.btn_camera_four_connect.setFlat(True)
        self.firstname_28 = QLabel(self.left_child)
        self.firstname_28.setObjectName(u"firstname_28")
        self.firstname_28.setGeometry(QRect(10, 640, 441, 171))
        self.firstname_28.setFont(font6)
        self.firstname_28.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"	padding-top:5px;\n"
"}")
        self.firstname_28.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_34 = QLabel(self.left_child)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setGeometry(QRect(30, 690, 41, 31))
        self.label_34.setPixmap(QPixmap(u":/icons/asset/video.svg"))
        self.notification = QLabel(self.left_child)
        self.notification.setObjectName(u"notification")
        self.notification.setGeometry(QRect(10, 840, 441, 101))
        self.notification.setFont(font3)
        self.notification.setStyleSheet(u"QLabel{\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.notification.setAlignment(Qt.AlignCenter)
        self.btn_cast_cam_one = QPushButton(self.left_child)
        self.btn_cast_cam_one.setObjectName(u"btn_cast_cam_one")
        self.btn_cast_cam_one.setGeometry(QRect(310, 120, 131, 41))
        self.btn_cast_cam_one.setFont(font5)
        self.btn_cast_cam_one.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/icons/asset/cast.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cast_cam_one.setIcon(icon14)
        self.btn_cast_cam_one.setIconSize(QSize(30, 30))
        self.btn_cast_cam_one.setFlat(True)
        self.camera_two_comboBox = QComboBox(self.left_child)
        self.camera_two_comboBox.addItem("")
        self.camera_two_comboBox.addItem("")
        self.camera_two_comboBox.addItem("")
        self.camera_two_comboBox.addItem("")
        self.camera_two_comboBox.addItem("")
        self.camera_two_comboBox.addItem("")
        self.camera_two_comboBox.setObjectName(u"camera_two_comboBox")
        self.camera_two_comboBox.setGeometry(QRect(330, 260, 111, 50))
        self.camera_two_comboBox.setMinimumSize(QSize(0, 50))
        self.camera_two_comboBox.setMaximumSize(QSize(16777215, 50))
        self.camera_two_comboBox.setFont(font5)
        self.camera_two_comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}")
        self.camera_two_comboBox.setFrame(False)
        self.btn_cast_cam_one_2 = QPushButton(self.left_child)
        self.btn_cast_cam_one_2.setObjectName(u"btn_cast_cam_one_2")
        self.btn_cast_cam_one_2.setGeometry(QRect(310, 330, 131, 41))
        self.btn_cast_cam_one_2.setFont(font5)
        self.btn_cast_cam_one_2.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_cast_cam_one_2.setIcon(icon14)
        self.btn_cast_cam_one_2.setIconSize(QSize(30, 30))
        self.btn_cast_cam_one_2.setFlat(True)
        self.camera_three_comboBox = QComboBox(self.left_child)
        self.camera_three_comboBox.addItem("")
        self.camera_three_comboBox.addItem("")
        self.camera_three_comboBox.addItem("")
        self.camera_three_comboBox.addItem("")
        self.camera_three_comboBox.addItem("")
        self.camera_three_comboBox.addItem("")
        self.camera_three_comboBox.setObjectName(u"camera_three_comboBox")
        self.camera_three_comboBox.setGeometry(QRect(330, 470, 111, 50))
        self.camera_three_comboBox.setMinimumSize(QSize(0, 50))
        self.camera_three_comboBox.setMaximumSize(QSize(16777215, 50))
        self.camera_three_comboBox.setFont(font5)
        self.camera_three_comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}")
        self.camera_three_comboBox.setFrame(False)
        self.btn_cast_cam_three = QPushButton(self.left_child)
        self.btn_cast_cam_three.setObjectName(u"btn_cast_cam_three")
        self.btn_cast_cam_three.setGeometry(QRect(310, 540, 131, 41))
        self.btn_cast_cam_three.setFont(font5)
        self.btn_cast_cam_three.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_cast_cam_three.setIcon(icon14)
        self.btn_cast_cam_three.setIconSize(QSize(30, 30))
        self.btn_cast_cam_three.setFlat(True)
        self.camera_four_comboBox = QComboBox(self.left_child)
        self.camera_four_comboBox.addItem("")
        self.camera_four_comboBox.addItem("")
        self.camera_four_comboBox.addItem("")
        self.camera_four_comboBox.addItem("")
        self.camera_four_comboBox.addItem("")
        self.camera_four_comboBox.addItem("")
        self.camera_four_comboBox.setObjectName(u"camera_four_comboBox")
        self.camera_four_comboBox.setGeometry(QRect(330, 680, 111, 50))
        self.camera_four_comboBox.setMinimumSize(QSize(0, 50))
        self.camera_four_comboBox.setMaximumSize(QSize(16777215, 50))
        self.camera_four_comboBox.setFont(font5)
        self.camera_four_comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}")
        self.camera_four_comboBox.setFrame(False)
        self.btn_cast_cam_four = QPushButton(self.left_child)
        self.btn_cast_cam_four.setObjectName(u"btn_cast_cam_four")
        self.btn_cast_cam_four.setGeometry(QRect(310, 750, 131, 41))
        self.btn_cast_cam_four.setFont(font5)
        self.btn_cast_cam_four.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_cast_cam_four.setIcon(icon14)
        self.btn_cast_cam_four.setIconSize(QSize(30, 30))
        self.btn_cast_cam_four.setFlat(True)
        self.firstname_28.raise_()
        self.firstname_27.raise_()
        self.firstname_26.raise_()
        self.firstname_25.raise_()
        self.btn_camera_one_connect.raise_()
        self.btn_camera_one_disconnect.raise_()
        self.camera_one_comboBox.raise_()
        self.camera_one_id_ip.raise_()
        self.label_31.raise_()
        self.btn_camera_two_disconnect.raise_()
        self.camera_two_id_ip.raise_()
        self.btn_camera_two_connect.raise_()
        self.label_32.raise_()
        self.btn_camera_three_disconnect.raise_()
        self.camera_three_id_ip.raise_()
        self.btn_camera_three_connect.raise_()
        self.label_33.raise_()
        self.btn_camera_four_disconnect.raise_()
        self.camera_four_id_ip.raise_()
        self.btn_camera_four_connect.raise_()
        self.label_34.raise_()
        self.notification.raise_()
        self.btn_cast_cam_one.raise_()
        self.camera_two_comboBox.raise_()
        self.btn_cast_cam_one_2.raise_()
        self.camera_three_comboBox.raise_()
        self.btn_cast_cam_three.raise_()
        self.camera_four_comboBox.raise_()
        self.btn_cast_cam_four.raise_()

        self.horizontalLayout_6.addWidget(self.left_child)

        self.rignt_child = QFrame(self.camera)
        self.rignt_child.setObjectName(u"rignt_child")
        self.rignt_child.setFrameShape(QFrame.NoFrame)
        self.rignt_child.setFrameShadow(QFrame.Plain)
        self.verticalLayout_10 = QVBoxLayout(self.rignt_child)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.camera_down = QFrame(self.rignt_child)
        self.camera_down.setObjectName(u"camera_down")
        self.camera_down.setFrameShape(QFrame.StyledPanel)
        self.camera_down.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.camera_down)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.camera_1 = QLabel(self.camera_down)
        self.camera_1.setObjectName(u"camera_1")
        font8 = QFont()
        font8.setFamily(u"Arial")
        font8.setPointSize(20)
        font8.setBold(True)
        font8.setWeight(75)
        self.camera_1.setFont(font8)
        self.camera_1.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.camera_1.setPixmap(QPixmap(u":/icons/asset/camera-off.svg"))
        self.camera_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.camera_1)

        self.camera_2 = QLabel(self.camera_down)
        self.camera_2.setObjectName(u"camera_2")
        self.camera_2.setFont(font8)
        self.camera_2.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.camera_2.setPixmap(QPixmap(u":/icons/asset/camera-off.svg"))
        self.camera_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.camera_2)


        self.verticalLayout_10.addWidget(self.camera_down)

        self.camera_top = QFrame(self.rignt_child)
        self.camera_top.setObjectName(u"camera_top")
        self.camera_top.setFrameShape(QFrame.StyledPanel)
        self.camera_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.camera_top)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.camera_3 = QLabel(self.camera_top)
        self.camera_3.setObjectName(u"camera_3")
        self.camera_3.setFont(font8)
        self.camera_3.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.camera_3.setPixmap(QPixmap(u":/icons/asset/camera-off.svg"))
        self.camera_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.camera_3)

        self.camera_4 = QLabel(self.camera_top)
        self.camera_4.setObjectName(u"camera_4")
        self.camera_4.setFont(font8)
        self.camera_4.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius:10px;\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.camera_4.setPixmap(QPixmap(u":/icons/asset/camera-off.svg"))
        self.camera_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.camera_4)


        self.verticalLayout_10.addWidget(self.camera_top)


        self.horizontalLayout_6.addWidget(self.rignt_child)

        self.stackedWidget.addWidget(self.camera)
        self.database = QWidget()
        self.database.setObjectName(u"database")
        self.horizontalLayout_14 = QHBoxLayout(self.database)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.left_fram_reg = QFrame(self.database)
        self.left_fram_reg.setObjectName(u"left_fram_reg")
        self.left_fram_reg.setMinimumSize(QSize(660, 0))
        self.left_fram_reg.setMaximumSize(QSize(500, 16777215))
        self.left_fram_reg.setFrameShape(QFrame.NoFrame)
        self.left_fram_reg.setFrameShadow(QFrame.Raised)
        self.reg_image = QLabel(self.left_fram_reg)
        self.reg_image.setObjectName(u"reg_image")
        self.reg_image.setGeometry(QRect(30, 150, 291, 291))
        font9 = QFont()
        font9.setFamily(u"Arial")
        font9.setPointSize(14)
        font9.setBold(True)
        font9.setWeight(75)
        self.reg_image.setFont(font9)
        self.reg_image.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.reg_image.setAlignment(Qt.AlignCenter)
        self.reg_firstname = QLineEdit(self.left_fram_reg)
        self.reg_firstname.setObjectName(u"reg_firstname")
        self.reg_firstname.setGeometry(QRect(340, 150, 291, 51))
        self.reg_firstname.setFont(font5)
        self.reg_firstname.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_firstname.setClearButtonEnabled(True)
        self.reg_image_2 = QLabel(self.left_fram_reg)
        self.reg_image_2.setObjectName(u"reg_image_2")
        self.reg_image_2.setGeometry(QRect(10, 130, 641, 511))
        self.reg_image_2.setFont(font9)
        self.reg_image_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.reg_image_2.setAlignment(Qt.AlignCenter)
        self.reg_middlename = QLineEdit(self.left_fram_reg)
        self.reg_middlename.setObjectName(u"reg_middlename")
        self.reg_middlename.setGeometry(QRect(340, 210, 291, 51))
        self.reg_middlename.setFont(font5)
        self.reg_middlename.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_middlename.setClearButtonEnabled(True)
        self.reg_lastname = QLineEdit(self.left_fram_reg)
        self.reg_lastname.setObjectName(u"reg_lastname")
        self.reg_lastname.setGeometry(QRect(340, 270, 291, 51))
        self.reg_lastname.setFont(font5)
        self.reg_lastname.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_lastname.setClearButtonEnabled(True)
        self.reg_index = QLineEdit(self.left_fram_reg)
        self.reg_index.setObjectName(u"reg_index")
        self.reg_index.setGeometry(QRect(340, 390, 291, 51))
        self.reg_index.setFont(font5)
        self.reg_index.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_index.setClearButtonEnabled(True)
        self.reg_college = QLineEdit(self.left_fram_reg)
        self.reg_college.setObjectName(u"reg_college")
        self.reg_college.setGeometry(QRect(340, 450, 291, 51))
        self.reg_college.setFont(font5)
        self.reg_college.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_college.setClearButtonEnabled(True)
        self.reg_student_ref = QLineEdit(self.left_fram_reg)
        self.reg_student_ref.setObjectName(u"reg_student_ref")
        self.reg_student_ref.setGeometry(QRect(340, 330, 291, 51))
        self.reg_student_ref.setFont(font5)
        self.reg_student_ref.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_student_ref.setClearButtonEnabled(True)
        self.reg_nationality = QLineEdit(self.left_fram_reg)
        self.reg_nationality.setObjectName(u"reg_nationality")
        self.reg_nationality.setGeometry(QRect(30, 450, 291, 51))
        self.reg_nationality.setFont(font5)
        self.reg_nationality.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_nationality.setClearButtonEnabled(True)
        self.reg_start_date = QLineEdit(self.left_fram_reg)
        self.reg_start_date.setObjectName(u"reg_start_date")
        self.reg_start_date.setGeometry(QRect(30, 510, 291, 51))
        self.reg_start_date.setFont(font5)
        self.reg_start_date.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_start_date.setClearButtonEnabled(True)
        self.reg_end_date = QLineEdit(self.left_fram_reg)
        self.reg_end_date.setObjectName(u"reg_end_date")
        self.reg_end_date.setGeometry(QRect(340, 510, 291, 51))
        self.reg_end_date.setFont(font5)
        self.reg_end_date.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.reg_end_date.setClearButtonEnabled(True)
        self.label_35 = QLabel(self.left_fram_reg)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(40, 520, 31, 31))
        self.label_35.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.reg_programs = QComboBox(self.left_fram_reg)
        self.reg_programs.addItem("")
        self.reg_programs.addItem("")
        self.reg_programs.addItem("")
        self.reg_programs.addItem("")
        self.reg_programs.setObjectName(u"reg_programs")
        self.reg_programs.setGeometry(QRect(340, 570, 291, 50))
        self.reg_programs.setMinimumSize(QSize(0, 50))
        self.reg_programs.setMaximumSize(QSize(16777215, 50))
        self.reg_programs.setFont(font5)
        self.reg_programs.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.reg_programs.setFrame(False)
        self.btn_search_reg = QPushButton(self.left_fram_reg)
        self.btn_search_reg.setObjectName(u"btn_search_reg")
        self.btn_search_reg.setGeometry(QRect(510, 30, 121, 51))
        self.btn_search_reg.setFont(font5)
        self.btn_search_reg.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_search_reg.setIcon(icon2)
        self.btn_search_reg.setIconSize(QSize(30, 30))
        self.btn_search_reg.setFlat(True)
        self.label_37 = QLabel(self.left_fram_reg)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(10, 10, 641, 91))
        self.label_37.setFont(font3)
        self.label_37.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_37.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.search_reg = QLineEdit(self.left_fram_reg)
        self.search_reg.setObjectName(u"search_reg")
        self.search_reg.setGeometry(QRect(30, 30, 461, 51))
        self.search_reg.setFont(font5)
        self.search_reg.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.search_reg.setClearButtonEnabled(True)
        self.label_38 = QLabel(self.left_fram_reg)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setGeometry(QRect(10, 740, 641, 81))
        self.label_38.setFont(font3)
        self.label_38.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_38.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.btn_register = QPushButton(self.left_fram_reg)
        self.btn_register.setObjectName(u"btn_register")
        self.btn_register.setGeometry(QRect(30, 760, 131, 41))
        self.btn_register.setFont(font5)
        self.btn_register.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_register.setIcon(icon1)
        self.btn_register.setIconSize(QSize(30, 30))
        self.btn_register.setFlat(True)
        self.btn_update = QPushButton(self.left_fram_reg)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setGeometry(QRect(190, 760, 131, 41))
        self.btn_update.setFont(font5)
        self.btn_update.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/icons/asset/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_update.setIcon(icon15)
        self.btn_update.setIconSize(QSize(30, 30))
        self.btn_update.setFlat(True)
        self.btn_remove = QPushButton(self.left_fram_reg)
        self.btn_remove.setObjectName(u"btn_remove")
        self.btn_remove.setGeometry(QRect(340, 760, 131, 41))
        self.btn_remove.setFont(font5)
        self.btn_remove.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/icons/asset/user-minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_remove.setIcon(icon16)
        self.btn_remove.setIconSize(QSize(30, 30))
        self.btn_remove.setFlat(True)
        self.date_frame_3 = QFrame(self.left_fram_reg)
        self.date_frame_3.setObjectName(u"date_frame_3")
        self.date_frame_3.setGeometry(QRect(10, 660, 641, 61))
        self.date_frame_3.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.date_frame_3.setFrameShape(QFrame.NoFrame)
        self.date_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.date_frame_3)
        self.horizontalLayout_11.setSpacing(30)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(15, 12, 15, -1)
        self.reg_face_auth = QRadioButton(self.date_frame_3)
        self.reg_face_auth.setObjectName(u"reg_face_auth")
        self.reg_face_auth.setFont(font4)
        self.reg_face_auth.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.reg_face_auth.setIcon(icon6)
        self.reg_face_auth.setChecked(True)

        self.horizontalLayout_11.addWidget(self.reg_face_auth)

        self.reg_qr_auth = QRadioButton(self.date_frame_3)
        self.reg_qr_auth.setObjectName(u"reg_qr_auth")
        self.reg_qr_auth.setFont(font4)
        self.reg_qr_auth.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.reg_qr_auth.setIcon(icon6)
        self.reg_qr_auth.setChecked(False)

        self.horizontalLayout_11.addWidget(self.reg_qr_auth)

        self.reg_biometric_auth = QRadioButton(self.date_frame_3)
        self.reg_biometric_auth.setObjectName(u"reg_biometric_auth")
        self.reg_biometric_auth.setFont(font4)
        self.reg_biometric_auth.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.reg_biometric_auth.setIcon(icon6)
        self.reg_biometric_auth.setChecked(False)

        self.horizontalLayout_11.addWidget(self.reg_biometric_auth)

        self.reg_both = QRadioButton(self.date_frame_3)
        self.reg_both.setObjectName(u"reg_both")
        self.reg_both.setFont(font4)
        self.reg_both.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(35, 35, 35);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.reg_both.setIcon(icon6)
        self.reg_both.setChecked(False)

        self.horizontalLayout_11.addWidget(self.reg_both)

        self.btn_clear = QPushButton(self.left_fram_reg)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setGeometry(QRect(500, 760, 131, 41))
        self.btn_clear.setFont(font5)
        self.btn_clear.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_clear.setIcon(icon9)
        self.btn_clear.setIconSize(QSize(30, 30))
        self.btn_clear.setFlat(True)
        self.label_39 = QLabel(self.left_fram_reg)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setGeometry(QRect(10, 840, 641, 101))
        self.label_39.setFont(font3)
        self.label_39.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:15px;\n"
"}")
        self.label_39.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.image_file_reg = QLineEdit(self.left_fram_reg)
        self.image_file_reg.setObjectName(u"image_file_reg")
        self.image_file_reg.setGeometry(QRect(30, 870, 451, 51))
        self.image_file_reg.setFont(font5)
        self.image_file_reg.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.image_file_reg.setClearButtonEnabled(True)
        self.btn_browse_reg = QPushButton(self.left_fram_reg)
        self.btn_browse_reg.setObjectName(u"btn_browse_reg")
        self.btn_browse_reg.setGeometry(QRect(510, 870, 121, 51))
        self.btn_browse_reg.setFont(font5)
        self.btn_browse_reg.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/icons/asset/upload.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_browse_reg.setIcon(icon17)
        self.btn_browse_reg.setIconSize(QSize(30, 30))
        self.btn_browse_reg.setFlat(True)
        self.reg_college_2 = QComboBox(self.left_fram_reg)
        self.reg_college_2.addItem("")
        self.reg_college_2.addItem("")
        self.reg_college_2.addItem("")
        self.reg_college_2.setObjectName(u"reg_college_2")
        self.reg_college_2.setGeometry(QRect(30, 570, 291, 50))
        self.reg_college_2.setMinimumSize(QSize(0, 50))
        self.reg_college_2.setMaximumSize(QSize(16777215, 50))
        self.reg_college_2.setFont(font5)
        self.reg_college_2.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.reg_college_2.setFrame(False)
        self.label_36 = QLabel(self.left_fram_reg)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(350, 520, 31, 31))
        self.label_36.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.label_37.raise_()
        self.search_reg.raise_()
        self.reg_image_2.raise_()
        self.reg_image.raise_()
        self.reg_firstname.raise_()
        self.reg_middlename.raise_()
        self.reg_lastname.raise_()
        self.reg_index.raise_()
        self.reg_college.raise_()
        self.reg_student_ref.raise_()
        self.reg_nationality.raise_()
        self.reg_start_date.raise_()
        self.label_35.raise_()
        self.reg_programs.raise_()
        self.btn_search_reg.raise_()
        self.label_38.raise_()
        self.btn_register.raise_()
        self.btn_update.raise_()
        self.btn_remove.raise_()
        self.date_frame_3.raise_()
        self.btn_clear.raise_()
        self.label_39.raise_()
        self.image_file_reg.raise_()
        self.btn_browse_reg.raise_()
        self.reg_college_2.raise_()
        self.reg_end_date.raise_()
        self.label_36.raise_()

        self.horizontalLayout_14.addWidget(self.left_fram_reg)

        self.right_frame_reg = QFrame(self.database)
        self.right_frame_reg.setObjectName(u"right_frame_reg")
        self.right_frame_reg.setFrameShape(QFrame.NoFrame)
        self.right_frame_reg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.right_frame_reg)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_10 = QFrame(self.right_frame_reg)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_15.setSpacing(9)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_10)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_13)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.finger_print_1 = QLabel(self.frame_13)
        self.finger_print_1.setObjectName(u"finger_print_1")
        self.finger_print_1.setMinimumSize(QSize(370, 350))
        self.finger_print_1.setMaximumSize(QSize(370, 350))
        self.finger_print_1.setFont(font3)
        self.finger_print_1.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.finger_print_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_17.addWidget(self.finger_print_1)

        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.btn_browse_file_1 = QPushButton(self.frame_16)
        self.btn_browse_file_1.setObjectName(u"btn_browse_file_1")
        self.btn_browse_file_1.setGeometry(QRect(240, 40, 121, 51))
        self.btn_browse_file_1.setFont(font5)
        self.btn_browse_file_1.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_browse_file_1.setIcon(icon17)
        self.btn_browse_file_1.setIconSize(QSize(30, 30))
        self.btn_browse_file_1.setFlat(True)
        self.image_file_1 = QLineEdit(self.frame_16)
        self.image_file_1.setObjectName(u"image_file_1")
        self.image_file_1.setGeometry(QRect(10, 40, 221, 51))
        self.image_file_1.setFont(font5)
        self.image_file_1.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.image_file_1.setClearButtonEnabled(True)
        self.label_41 = QLabel(self.frame_16)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setGeometry(QRect(0, 0, 131, 21))
        self.label_41.setFont(font6)
        self.label_41.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:15px;\n"
"}")
        self.label_41.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_17.addWidget(self.frame_16)


        self.horizontalLayout_15.addWidget(self.frame_13)

        self.frame_15 = QFrame(self.frame_10)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_15)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.finger_print_2 = QLabel(self.frame_15)
        self.finger_print_2.setObjectName(u"finger_print_2")
        self.finger_print_2.setMinimumSize(QSize(370, 350))
        self.finger_print_2.setMaximumSize(QSize(370, 350))
        self.finger_print_2.setFont(font3)
        self.finger_print_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"}")
        self.finger_print_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_18.addWidget(self.finger_print_2)

        self.frame_17 = QFrame(self.frame_15)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.image_file_2 = QLineEdit(self.frame_17)
        self.image_file_2.setObjectName(u"image_file_2")
        self.image_file_2.setGeometry(QRect(10, 40, 221, 51))
        self.image_file_2.setFont(font5)
        self.image_file_2.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:10px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.image_file_2.setClearButtonEnabled(True)
        self.btn_browse_3 = QPushButton(self.frame_17)
        self.btn_browse_3.setObjectName(u"btn_browse_3")
        self.btn_browse_3.setGeometry(QRect(240, 40, 121, 51))
        self.btn_browse_3.setFont(font5)
        self.btn_browse_3.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_browse_3.setIcon(icon17)
        self.btn_browse_3.setIconSize(QSize(30, 30))
        self.btn_browse_3.setFlat(True)
        self.label_43 = QLabel(self.frame_17)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setGeometry(QRect(0, 0, 121, 21))
        self.label_43.setFont(font6)
        self.label_43.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:15px;\n"
"}")
        self.label_43.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_18.addWidget(self.frame_17)


        self.horizontalLayout_15.addWidget(self.frame_15)


        self.verticalLayout_15.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.right_frame_reg)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_20 = QFrame(self.frame_11)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(0, 220, 371, 241))
        self.frame_20.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_20.setFrameShape(QFrame.NoFrame)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_20)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.calendarWidget_reg = QCalendarWidget(self.frame_20)
        self.calendarWidget_reg.setObjectName(u"calendarWidget_reg")
        self.calendarWidget_reg.setGridVisible(False)
        self.calendarWidget_reg.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_reg.setNavigationBarVisible(True)

        self.verticalLayout_20.addWidget(self.calendarWidget_reg)

        self.label_42 = QLabel(self.frame_11)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(0, 10, 751, 61))
        self.label_42.setFont(font3)
        self.label_42.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_42.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.confidence_level_1 = QSlider(self.frame_11)
        self.confidence_level_1.setObjectName(u"confidence_level_1")
        self.confidence_level_1.setGeometry(QRect(130, 30, 321, 22))
        self.confidence_level_1.setMaximum(100)
        self.confidence_level_1.setValue(50)
        self.confidence_level_1.setOrientation(Qt.Horizontal)
        self.score = QLabel(self.frame_11)
        self.score.setObjectName(u"score")
        self.score.setGeometry(QRect(460, 30, 81, 21))
        self.score.setFont(font6)
        self.score.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 35);\n"
"")
        self.score.setAlignment(Qt.AlignCenter)
        self.label_45 = QLabel(self.frame_11)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setGeometry(QRect(10, 30, 101, 21))
        self.label_45.setFont(font6)
        self.label_45.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(35, 35, 35);\n"
"")
        self.label_45.setAlignment(Qt.AlignCenter)
        self.btn_run_check = QPushButton(self.frame_11)
        self.btn_run_check.setObjectName(u"btn_run_check")
        self.btn_run_check.setGeometry(QRect(590, 20, 151, 41))
        self.btn_run_check.setFont(font5)
        self.btn_run_check.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u":/icons/asset/check-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_run_check.setIcon(icon18)
        self.btn_run_check.setIconSize(QSize(30, 30))
        self.btn_run_check.setFlat(True)
        self.frame_21 = QFrame(self.frame_11)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(380, 220, 371, 241))
        self.frame_21.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_21.setFrameShape(QFrame.NoFrame)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_21)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.calendarWidget_reg_2 = QCalendarWidget(self.frame_21)
        self.calendarWidget_reg_2.setObjectName(u"calendarWidget_reg_2")
        self.calendarWidget_reg_2.setGridVisible(False)
        self.calendarWidget_reg_2.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_reg_2.setNavigationBarVisible(True)

        self.verticalLayout_21.addWidget(self.calendarWidget_reg_2)

        self.label_46 = QLabel(self.frame_11)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setGeometry(QRect(0, 170, 161, 41))
        self.label_46.setFont(font6)
        self.label_46.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_46.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_47 = QLabel(self.frame_11)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setGeometry(QRect(380, 170, 181, 41))
        self.label_47.setFont(font6)
        self.label_47.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_47.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_48 = QLabel(self.frame_11)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setGeometry(QRect(0, 10, 751, 201))
        self.label_48.setFont(font3)
        self.label_48.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_48.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_49 = QLabel(self.frame_11)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setGeometry(QRect(10, 70, 91, 41))
        self.label_49.setFont(font6)
        self.label_49.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:5px;\n"
"}")
        self.label_49.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.expected = QLabel(self.frame_11)
        self.expected.setObjectName(u"expected")
        self.expected.setGeometry(QRect(100, 70, 91, 41))
        self.expected.setFont(font6)
        self.expected.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.expected.setAlignment(Qt.AlignCenter)
        self.label_51 = QLabel(self.frame_11)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setGeometry(QRect(240, 70, 91, 41))
        self.label_51.setFont(font6)
        self.label_51.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_51.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.actual = QLabel(self.frame_11)
        self.actual.setObjectName(u"actual")
        self.actual.setGeometry(QRect(330, 70, 91, 41))
        self.actual.setFont(font6)
        self.actual.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.actual.setAlignment(Qt.AlignCenter)
        self.label_52 = QLabel(self.frame_11)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setGeometry(QRect(470, 70, 91, 41))
        self.label_52.setFont(font6)
        self.label_52.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.label_52.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.actual_2 = QLabel(self.frame_11)
        self.actual_2.setObjectName(u"actual_2")
        self.actual_2.setGeometry(QRect(580, 70, 91, 41))
        self.actual_2.setFont(font6)
        self.actual_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35, 35, 35);\n"
"	border-radius: 10px;\n"
"	padding-left:10px;\n"
"}")
        self.actual_2.setAlignment(Qt.AlignCenter)
        self.label_48.raise_()
        self.frame_20.raise_()
        self.label_42.raise_()
        self.confidence_level_1.raise_()
        self.score.raise_()
        self.label_45.raise_()
        self.btn_run_check.raise_()
        self.frame_21.raise_()
        self.label_46.raise_()
        self.label_47.raise_()
        self.label_49.raise_()
        self.expected.raise_()
        self.label_51.raise_()
        self.actual.raise_()
        self.label_52.raise_()
        self.actual_2.raise_()

        self.verticalLayout_15.addWidget(self.frame_11)


        self.horizontalLayout_14.addWidget(self.right_frame_reg)

        self.stackedWidget.addWidget(self.database)
        self.report = QWidget()
        self.report.setObjectName(u"report")
        self.verticalLayout_13 = QVBoxLayout(self.report)
        self.verticalLayout_13.setSpacing(9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, -1, 0)
        self.frame_7 = QFrame(self.report)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 650))
        self.frame_7.setMaximumSize(QSize(16777215, 650))
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_17.setSpacing(20)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, -1, -1, 9)
        self.plot_area = QLabel(self.frame_7)
        self.plot_area.setObjectName(u"plot_area")
        self.plot_area.setMinimumSize(QSize(699, 632))
        self.plot_area.setMaximumSize(QSize(699, 632))
        self.plot_area.setFont(font4)
        self.plot_area.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35,35,35);\n"
"	border-radius: 10px;\n"
"}")
        self.plot_area.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.plot_area)

        self.plot_area_2 = QLabel(self.frame_7)
        self.plot_area_2.setObjectName(u"plot_area_2")
        self.plot_area_2.setMinimumSize(QSize(698, 632))
        self.plot_area_2.setMaximumSize(QSize(698, 632))
        self.plot_area_2.setFont(font4)
        self.plot_area_2.setStyleSheet(u"QLabel{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(35,35,35);\n"
"	border-radius: 10px;\n"
"}")
        self.plot_area_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.plot_area_2)


        self.verticalLayout_13.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.report)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_8)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 0, 0, -1)
        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(35,35,35);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(10, 20, 371, 241))
        self.frame_12.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_12)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.calendarWidget_report = QCalendarWidget(self.frame_12)
        self.calendarWidget_report.setObjectName(u"calendarWidget_report")
        self.calendarWidget_report.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_report.setNavigationBarVisible(True)

        self.verticalLayout_16.addWidget(self.calendarWidget_report)

        self.report_start_date = QLineEdit(self.frame_9)
        self.report_start_date.setObjectName(u"report_start_date")
        self.report_start_date.setGeometry(QRect(770, 20, 181, 51))
        self.report_start_date.setFont(font5)
        self.report_start_date.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.report_start_date.setClearButtonEnabled(True)
        self.label_23 = QLabel(self.frame_9)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(780, 30, 31, 31))
        self.label_23.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_23.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.report_end_date = QLineEdit(self.frame_9)
        self.report_end_date.setObjectName(u"report_end_date")
        self.report_end_date.setGeometry(QRect(970, 20, 201, 51))
        self.report_end_date.setFont(font5)
        self.report_end_date.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.report_end_date.setClearButtonEnabled(True)
        self.label_24 = QLabel(self.frame_9)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(980, 30, 31, 31))
        self.label_24.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_24.setPixmap(QPixmap(u":/icons/asset/calendar.svg"))
        self.file_name = QLineEdit(self.frame_9)
        self.file_name.setObjectName(u"file_name")
        self.file_name.setGeometry(QRect(1190, 20, 211, 51))
        self.file_name.setFont(font5)
        self.file_name.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid  rgb(45, 45, 45);\n"
"	border-radius:15px;\n"
"	padding-left: 50px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}\n"
"\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(255, 255, 255);\n"
"}")
        self.file_name.setClearButtonEnabled(True)
        self.label_20 = QLabel(self.frame_9)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(1200, 30, 31, 31))
        self.label_20.setStyleSheet(u"background-color: rgb(45, 45, 45);")
        self.label_20.setPixmap(QPixmap(u":/icons/asset/file.svg"))
        self.date_frame = QFrame(self.frame_9)
        self.date_frame.setObjectName(u"date_frame")
        self.date_frame.setGeometry(QRect(770, 90, 221, 51))
        self.date_frame.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}")
        self.date_frame.setFrameShape(QFrame.StyledPanel)
        self.date_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.date_frame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.start_date_3 = QRadioButton(self.date_frame)
        self.start_date_3.setObjectName(u"start_date_3")
        self.start_date_3.setFont(font4)
        self.start_date_3.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.start_date_3.setChecked(True)

        self.horizontalLayout_12.addWidget(self.start_date_3)

        self.end_date_3 = QRadioButton(self.date_frame)
        self.end_date_3.setObjectName(u"end_date_3")
        self.end_date_3.setFont(font4)
        self.end_date_3.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_12.addWidget(self.end_date_3)

        self.btn_load = QPushButton(self.frame_9)
        self.btn_load.setObjectName(u"btn_load")
        self.btn_load.setGeometry(QRect(770, 220, 141, 45))
        self.btn_load.setMinimumSize(QSize(0, 45))
        self.btn_load.setMaximumSize(QSize(16777215, 45))
        self.btn_load.setFont(font5)
        self.btn_load.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_load.setIcon(icon10)
        self.btn_load.setIconSize(QSize(30, 30))
        self.btn_load.setFlat(True)
        self.btn_save = QPushButton(self.frame_9)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setGeometry(QRect(940, 220, 141, 45))
        self.btn_save.setMinimumSize(QSize(0, 45))
        self.btn_save.setMaximumSize(QSize(16777215, 45))
        self.btn_save.setFont(font5)
        self.btn_save.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u":/icons/asset/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon19)
        self.btn_save.setIconSize(QSize(30, 30))
        self.btn_save.setFlat(True)
        self.btn_refresh = QPushButton(self.frame_9)
        self.btn_refresh.setObjectName(u"btn_refresh")
        self.btn_refresh.setGeometry(QRect(1100, 220, 141, 45))
        self.btn_refresh.setMinimumSize(QSize(0, 45))
        self.btn_refresh.setMaximumSize(QSize(16777215, 45))
        self.btn_refresh.setFont(font5)
        self.btn_refresh.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_refresh.setIcon(icon11)
        self.btn_refresh.setIconSize(QSize(30, 30))
        self.btn_refresh.setFlat(True)
        self.btn_clear_area = QPushButton(self.frame_9)
        self.btn_clear_area.setObjectName(u"btn_clear_area")
        self.btn_clear_area.setGeometry(QRect(1270, 220, 131, 45))
        self.btn_clear_area.setMinimumSize(QSize(0, 45))
        self.btn_clear_area.setMaximumSize(QSize(16777215, 45))
        self.btn_clear_area.setFont(font5)
        self.btn_clear_area.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border:none;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	border: 2px solid rgb(255,255,255);	\n"
"}")
        self.btn_clear_area.setIcon(icon11)
        self.btn_clear_area.setIconSize(QSize(30, 30))
        self.btn_clear_area.setFlat(True)
        self.college_comboBox = QComboBox(self.frame_9)
        self.college_comboBox.addItem("")
        self.college_comboBox.addItem("")
        self.college_comboBox.addItem("")
        self.college_comboBox.setObjectName(u"college_comboBox")
        self.college_comboBox.setGeometry(QRect(1000, 90, 131, 50))
        self.college_comboBox.setMinimumSize(QSize(0, 50))
        self.college_comboBox.setMaximumSize(QSize(16777215, 50))
        self.college_comboBox.setFont(font5)
        self.college_comboBox.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.college_comboBox.setFrame(False)
        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(390, 20, 371, 241))
        self.frame_14.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"}")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_14)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.calendarWidget_report_2 = QCalendarWidget(self.frame_14)
        self.calendarWidget_report_2.setObjectName(u"calendarWidget_report_2")
        self.calendarWidget_report_2.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_report_2.setNavigationBarVisible(True)

        self.verticalLayout_19.addWidget(self.calendarWidget_report_2)

        self.college_courses = QComboBox(self.frame_9)
        self.college_courses.addItem("")
        self.college_courses.addItem("")
        self.college_courses.addItem("")
        self.college_courses.addItem("")
        self.college_courses.setObjectName(u"college_courses")
        self.college_courses.setGeometry(QRect(1150, 90, 251, 50))
        self.college_courses.setMinimumSize(QSize(0, 50))
        self.college_courses.setMaximumSize(QSize(16777215, 50))
        self.college_courses.setFont(font5)
        self.college_courses.setStyleSheet(u"QComboBox{\n"
"	color: rgb(255, 255, 255);\n"
"	border: 2px solid rgb(45, 45, 45);\n"
"	padding-left:10px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(35, 35, 35);\n"
"}")
        self.college_courses.setFrame(False)
        self.frame_18 = QFrame(self.frame_9)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(770, 160, 631, 41))
        self.frame_18.setStyleSheet(u"QFrame{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(45, 45, 45);\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.start_date_4 = QRadioButton(self.frame_18)
        self.start_date_4.setObjectName(u"start_date_4")
        self.start_date_4.setFont(font4)
        self.start_date_4.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.start_date_4.setChecked(True)

        self.horizontalLayout_16.addWidget(self.start_date_4)

        self.start_date_5 = QRadioButton(self.frame_18)
        self.start_date_5.setObjectName(u"start_date_5")
        self.start_date_5.setFont(font4)
        self.start_date_5.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_16.addWidget(self.start_date_5)

        self.start_date_6 = QRadioButton(self.frame_18)
        self.start_date_6.setObjectName(u"start_date_6")
        self.start_date_6.setFont(font4)
        self.start_date_6.setStyleSheet(u"QRadioButton{\n"
"	background-color: rgb(45, 45, 45);\n"
"	color: rgb(255, 255, 255);\n"
"}")

        self.horizontalLayout_16.addWidget(self.start_date_6)


        self.verticalLayout_14.addWidget(self.frame_9)


        self.verticalLayout_13.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.report)
        self.frame_8.raise_()
        self.frame_7.raise_()
        self.settings = QWidget()
        self.settings.setObjectName(u"settings")
        self.label_7 = QLabel(self.settings)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(490, 300, 251, 141))
        font10 = QFont()
        font10.setPointSize(20)
        self.label_7.setFont(font10)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.settings)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.horizontalLayout_3.addWidget(self.content_frame)


        self.content_layout.addWidget(self.content)


        self.verticalLayout.addWidget(self.drop_shadow_layout)

        dashboard.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(dashboard)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(dashboard)
    # setupUi

    def retranslateUi(self, dashboard):
        dashboard.setWindowTitle(QCoreApplication.translate("dashboard", u"MainWindow", None))
        self.label.setText("")
        self.btn_maximize.setText("")
        self.btn_minimize.setText("")
        self.btn_close.setText("")
        self.btn_home.setText("")
        self.btn_database.setText("")
        self.btn_search.setText("")
        self.btn_camera.setText("")
        self.btn_report.setText("")
        self.btn_help.setText("")
        self.image.setText(QCoreApplication.translate("dashboard", u"Image", None))
        self.firstname.setText(QCoreApplication.translate("dashboard", u"Firstname", None))
        self.middlename.setText(QCoreApplication.translate("dashboard", u"Middlename", None))
        self.lastname.setText(QCoreApplication.translate("dashboard", u"Lastname", None))
        self.refrence.setText(QCoreApplication.translate("dashboard", u"Reference", None))
        self.index.setText(QCoreApplication.translate("dashboard", u"Index", None))
        self.coledge.setText(QCoreApplication.translate("dashboard", u"College", None))
        self.validity.setText(QCoreApplication.translate("dashboard", u"Validity", None))
        self.nationality.setText(QCoreApplication.translate("dashboard", u"Nationality", None))
        self.year.setText(QCoreApplication.translate("dashboard", u"Year", None))
        self.program.setText(QCoreApplication.translate("dashboard", u"Program", None))
        self.last_out.setText(QCoreApplication.translate("dashboard", u"Last seen", None))
        self.image_2.setText("")
        self.last_in.setText(QCoreApplication.translate("dashboard", u"Duration", None))
        self.label_notification.setText(QCoreApplication.translate("dashboard", u"Notification", None))
        self.face_auth.setText(QCoreApplication.translate("dashboard", u"Face Authentication", None))
        self.qr_code_auth.setText(QCoreApplication.translate("dashboard", u"QR Code", None))
        self.biometric_auth.setText(QCoreApplication.translate("dashboard", u"Biometric ", None))
        self.camera_ip.setPlaceholderText(QCoreApplication.translate("dashboard", u"Camera Id/IP ?", None))
        self.btn_connect_detect.setText(QCoreApplication.translate("dashboard", u"Connect", None))
        self.label_27.setText("")
        self.btn_disconnect.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("dashboard", u"0", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("dashboard", u"1", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("dashboard", u"2", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("dashboard", u"3", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("dashboard", u"4", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("dashboard", u"5", None))

        self.firstname_23.setText(QCoreApplication.translate("dashboard", u"Entry camera", None))
        self.firstname_24.setText("")
        self.btn_open_exit_camera_ui.setText(QCoreApplication.translate("dashboard", u"Open frame", None))
        self.btn_clear_label.setText(QCoreApplication.translate("dashboard", u"Reset", None))
        self.btn_init_face_auth.setText(QCoreApplication.translate("dashboard", u"Initialize", None))
        self.camera_view.setText("")
        self.thresh_value.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.hsv_value.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.dilation_value.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.entry_unimp_label.setText(QCoreApplication.translate("dashboard", u"Brigthness", None))
        self.entry_dilation_label.setText(QCoreApplication.translate("dashboard", u"G_Bluring", None))
        self.entry_erosion_label.setText(QCoreApplication.translate("dashboard", u"M_Bluring", None))
        self.erosion_value.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.entry_blur_label.setText(QCoreApplication.translate("dashboard", u"Box_filter", None))
#if QT_CONFIG(tooltip)
        self.dilation.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_14.setText(QCoreApplication.translate("dashboard", u"Image Enhancement", None))
        self.label_18.setText(QCoreApplication.translate("dashboard", u"Image Enhancement", None))
        self.exit_dilation_label.setText(QCoreApplication.translate("dashboard", u"Mask", None))
#if QT_CONFIG(tooltip)
        self.average_blur.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.avg_blur_value.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.exit_erosion_label.setText(QCoreApplication.translate("dashboard", u"Sharpness", None))
        self.gb_blur_value.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.exit_blur_label.setText(QCoreApplication.translate("dashboard", u"Contrast", None))
        self.bb_blur_value.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.exit_umimpl.setText(QCoreApplication.translate("dashboard", u"Bilateral", None))
        self.kernel_value.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.db_validity.setText(QCoreApplication.translate("dashboard", u"Validity", None))
        self.db_refrence.setText(QCoreApplication.translate("dashboard", u"Reference", None))
        self.db_year.setText(QCoreApplication.translate("dashboard", u"Year", None))
        self.db_nationality.setText(QCoreApplication.translate("dashboard", u"Nationality", None))
        self.db_image_data.setText(QCoreApplication.translate("dashboard", u"Image", None))
        self.db_lastname.setText(QCoreApplication.translate("dashboard", u"Lastname", None))
        self.db_middlename.setText(QCoreApplication.translate("dashboard", u"Middlename", None))
        self.db_firstname.setText(QCoreApplication.translate("dashboard", u"Firstname", None))
        self.db_index.setText(QCoreApplication.translate("dashboard", u"Index", None))
        self.db_programe.setText(QCoreApplication.translate("dashboard", u"Program", None))
        self.db_college.setText(QCoreApplication.translate("dashboard", u"College", None))
        self.search_box.setPlaceholderText(QCoreApplication.translate("dashboard", u"Search here?", None))
        self.btn_search_page.setText(QCoreApplication.translate("dashboard", u"Search", None))
        self.label_29.setText("")
        self.image_3.setText("")
        self.start_date.setText(QCoreApplication.translate("dashboard", u"Start Date", None))
        self.end_date.setText(QCoreApplication.translate("dashboard", u"End Date", None))
        self.db_start_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"Start date?", None))
        self.db_end_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"End date?", None))
        self.label_25.setText("")
        self.label_30.setText("")
        self.btn_reload.setText(QCoreApplication.translate("dashboard", u"Clear", None))
        self.btn_print.setText(QCoreApplication.translate("dashboard", u"Print", None))
        self.btn_dump_csv.setText(QCoreApplication.translate("dashboard", u"PDF", None))
        self.label_26.setText("")
        self.label_40.setText("")
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("dashboard", u"Reference", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("dashboard", u"Program", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("dashboard", u"Date", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("dashboard", u"Time In", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("dashboard", u"Time Out", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("dashboard", u"Duration", None));
        self.firstname_25.setText(QCoreApplication.translate("dashboard", u"Camera one", None))
        self.btn_camera_one_connect.setText(QCoreApplication.translate("dashboard", u"Connect", None))
        self.btn_camera_one_disconnect.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
        self.camera_one_comboBox.setItemText(0, QCoreApplication.translate("dashboard", u"0", None))
        self.camera_one_comboBox.setItemText(1, QCoreApplication.translate("dashboard", u"1", None))
        self.camera_one_comboBox.setItemText(2, QCoreApplication.translate("dashboard", u"2", None))
        self.camera_one_comboBox.setItemText(3, QCoreApplication.translate("dashboard", u"3", None))
        self.camera_one_comboBox.setItemText(4, QCoreApplication.translate("dashboard", u"4", None))
        self.camera_one_comboBox.setItemText(5, QCoreApplication.translate("dashboard", u"5", None))

        self.camera_one_id_ip.setPlaceholderText(QCoreApplication.translate("dashboard", u"Camera Id/IP ?", None))
        self.label_31.setText("")
        self.btn_camera_two_disconnect.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
        self.camera_two_id_ip.setPlaceholderText(QCoreApplication.translate("dashboard", u"Camera Id/IP ?", None))
        self.btn_camera_two_connect.setText(QCoreApplication.translate("dashboard", u"Connect", None))
        self.firstname_26.setText(QCoreApplication.translate("dashboard", u"Camera two", None))
        self.label_32.setText("")
        self.btn_camera_three_disconnect.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
        self.camera_three_id_ip.setPlaceholderText(QCoreApplication.translate("dashboard", u"Camera Id/IP ?", None))
        self.btn_camera_three_connect.setText(QCoreApplication.translate("dashboard", u"Connect", None))
        self.firstname_27.setText(QCoreApplication.translate("dashboard", u"Camera three", None))
        self.label_33.setText("")
        self.btn_camera_four_disconnect.setText(QCoreApplication.translate("dashboard", u"Disconnect", None))
        self.camera_four_id_ip.setPlaceholderText(QCoreApplication.translate("dashboard", u"Camera Id/IP ?", None))
        self.btn_camera_four_connect.setText(QCoreApplication.translate("dashboard", u"Connect", None))
        self.firstname_28.setText(QCoreApplication.translate("dashboard", u"Camera four", None))
        self.label_34.setText("")
        self.notification.setText(QCoreApplication.translate("dashboard", u"Notification", None))
        self.btn_cast_cam_one.setText(QCoreApplication.translate("dashboard", u"Cast", None))
        self.camera_two_comboBox.setItemText(0, QCoreApplication.translate("dashboard", u"0", None))
        self.camera_two_comboBox.setItemText(1, QCoreApplication.translate("dashboard", u"1", None))
        self.camera_two_comboBox.setItemText(2, QCoreApplication.translate("dashboard", u"2", None))
        self.camera_two_comboBox.setItemText(3, QCoreApplication.translate("dashboard", u"3", None))
        self.camera_two_comboBox.setItemText(4, QCoreApplication.translate("dashboard", u"4", None))
        self.camera_two_comboBox.setItemText(5, QCoreApplication.translate("dashboard", u"5", None))

        self.btn_cast_cam_one_2.setText(QCoreApplication.translate("dashboard", u"Cast", None))
        self.camera_three_comboBox.setItemText(0, QCoreApplication.translate("dashboard", u"0", None))
        self.camera_three_comboBox.setItemText(1, QCoreApplication.translate("dashboard", u"1", None))
        self.camera_three_comboBox.setItemText(2, QCoreApplication.translate("dashboard", u"2", None))
        self.camera_three_comboBox.setItemText(3, QCoreApplication.translate("dashboard", u"3", None))
        self.camera_three_comboBox.setItemText(4, QCoreApplication.translate("dashboard", u"4", None))
        self.camera_three_comboBox.setItemText(5, QCoreApplication.translate("dashboard", u"5", None))

        self.btn_cast_cam_three.setText(QCoreApplication.translate("dashboard", u"Cast", None))
        self.camera_four_comboBox.setItemText(0, QCoreApplication.translate("dashboard", u"0", None))
        self.camera_four_comboBox.setItemText(1, QCoreApplication.translate("dashboard", u"1", None))
        self.camera_four_comboBox.setItemText(2, QCoreApplication.translate("dashboard", u"2", None))
        self.camera_four_comboBox.setItemText(3, QCoreApplication.translate("dashboard", u"3", None))
        self.camera_four_comboBox.setItemText(4, QCoreApplication.translate("dashboard", u"4", None))
        self.camera_four_comboBox.setItemText(5, QCoreApplication.translate("dashboard", u"5", None))

        self.btn_cast_cam_four.setText(QCoreApplication.translate("dashboard", u"Cast", None))
        self.camera_1.setText("")
        self.camera_2.setText("")
        self.camera_3.setText("")
        self.camera_4.setText("")
        self.reg_image.setText(QCoreApplication.translate("dashboard", u"Image", None))
        self.reg_firstname.setPlaceholderText(QCoreApplication.translate("dashboard", u"Firstname", None))
        self.reg_image_2.setText("")
        self.reg_middlename.setPlaceholderText(QCoreApplication.translate("dashboard", u"Middlename", None))
        self.reg_lastname.setPlaceholderText(QCoreApplication.translate("dashboard", u"Lastname", None))
        self.reg_index.setPlaceholderText(QCoreApplication.translate("dashboard", u"Index", None))
        self.reg_college.setPlaceholderText(QCoreApplication.translate("dashboard", u"College", None))
        self.reg_student_ref.setPlaceholderText(QCoreApplication.translate("dashboard", u"Student No.", None))
        self.reg_nationality.setPlaceholderText(QCoreApplication.translate("dashboard", u"Nationality", None))
        self.reg_start_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"Start date", None))
        self.reg_end_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"End date", None))
        self.label_35.setText("")
        self.reg_programs.setItemText(0, QCoreApplication.translate("dashboard", u"BSc. Computer Science", None))
        self.reg_programs.setItemText(1, QCoreApplication.translate("dashboard", u"BSc. Mathematics", None))
        self.reg_programs.setItemText(2, QCoreApplication.translate("dashboard", u"BSc. Chemistry", None))
        self.reg_programs.setItemText(3, QCoreApplication.translate("dashboard", u"BSc. Biology Science", None))

        self.btn_search_reg.setText(QCoreApplication.translate("dashboard", u"Search", None))
        self.label_37.setText("")
        self.search_reg.setPlaceholderText(QCoreApplication.translate("dashboard", u"Search here?", None))
        self.label_38.setText("")
        self.btn_register.setText(QCoreApplication.translate("dashboard", u"Register", None))
        self.btn_update.setText(QCoreApplication.translate("dashboard", u"Update", None))
        self.btn_remove.setText(QCoreApplication.translate("dashboard", u"Remove", None))
        self.reg_face_auth.setText(QCoreApplication.translate("dashboard", u"Face Authentication", None))
        self.reg_qr_auth.setText(QCoreApplication.translate("dashboard", u"QR Code", None))
        self.reg_biometric_auth.setText(QCoreApplication.translate("dashboard", u"Biometric ", None))
        self.reg_both.setText(QCoreApplication.translate("dashboard", u"Both", None))
        self.btn_clear.setText(QCoreApplication.translate("dashboard", u"Clear", None))
        self.label_39.setText(QCoreApplication.translate("dashboard", u"Image file", None))
        self.image_file_reg.setPlaceholderText(QCoreApplication.translate("dashboard", u"File path", None))
        self.btn_browse_reg.setText(QCoreApplication.translate("dashboard", u"Browse", None))
        self.reg_college_2.setItemText(0, QCoreApplication.translate("dashboard", u"CoS", None))
        self.reg_college_2.setItemText(1, QCoreApplication.translate("dashboard", u"CoE", None))
        self.reg_college_2.setItemText(2, QCoreApplication.translate("dashboard", u"HESSA", None))

        self.label_36.setText("")
        self.finger_print_1.setText("")
        self.btn_browse_file_1.setText(QCoreApplication.translate("dashboard", u"Browse", None))
        self.image_file_1.setPlaceholderText(QCoreApplication.translate("dashboard", u"File path", None))
        self.label_41.setText(QCoreApplication.translate("dashboard", u"Fingerprint", None))
        self.finger_print_2.setText("")
        self.image_file_2.setPlaceholderText(QCoreApplication.translate("dashboard", u"File path", None))
        self.btn_browse_3.setText(QCoreApplication.translate("dashboard", u"Browse", None))
        self.label_43.setText(QCoreApplication.translate("dashboard", u"Fingerprint", None))
        self.label_42.setText("")
        self.score.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.label_45.setText(QCoreApplication.translate("dashboard", u"Confidence", None))
        self.btn_run_check.setText(QCoreApplication.translate("dashboard", u"check", None))
        self.label_46.setText(QCoreApplication.translate("dashboard", u"Start date", None))
        self.label_47.setText(QCoreApplication.translate("dashboard", u"End date", None))
        self.label_48.setText("")
        self.label_49.setText(QCoreApplication.translate("dashboard", u"Expected:", None))
        self.expected.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.label_51.setText(QCoreApplication.translate("dashboard", u"Actual:", None))
        self.actual.setText(QCoreApplication.translate("dashboard", u"0", None))
        self.label_52.setText(QCoreApplication.translate("dashboard", u"Status:", None))
        self.actual_2.setText(QCoreApplication.translate("dashboard", u"Passed", None))
        self.plot_area.setText(QCoreApplication.translate("dashboard", u"Graph", None))
        self.plot_area_2.setText(QCoreApplication.translate("dashboard", u"Graph", None))
        self.report_start_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"Start date?", None))
        self.label_23.setText("")
        self.report_end_date.setPlaceholderText(QCoreApplication.translate("dashboard", u"End date?", None))
        self.label_24.setText("")
        self.file_name.setPlaceholderText(QCoreApplication.translate("dashboard", u"File name?", None))
        self.label_20.setText("")
        self.start_date_3.setText(QCoreApplication.translate("dashboard", u"Start Date", None))
        self.end_date_3.setText(QCoreApplication.translate("dashboard", u"End Date", None))
        self.btn_load.setText(QCoreApplication.translate("dashboard", u"Load", None))
        self.btn_save.setText(QCoreApplication.translate("dashboard", u"Save", None))
        self.btn_refresh.setText(QCoreApplication.translate("dashboard", u"Reload", None))
        self.btn_clear_area.setText(QCoreApplication.translate("dashboard", u"Clear", None))
        self.college_comboBox.setItemText(0, QCoreApplication.translate("dashboard", u"CoS", None))
        self.college_comboBox.setItemText(1, QCoreApplication.translate("dashboard", u"CoE", None))
        self.college_comboBox.setItemText(2, QCoreApplication.translate("dashboard", u"HESSA", None))

        self.college_courses.setItemText(0, QCoreApplication.translate("dashboard", u"BSc. Computer Science", None))
        self.college_courses.setItemText(1, QCoreApplication.translate("dashboard", u"BSc. Mathematics", None))
        self.college_courses.setItemText(2, QCoreApplication.translate("dashboard", u"BSc. Chemistry", None))
        self.college_courses.setItemText(3, QCoreApplication.translate("dashboard", u"BSc. Biology Science", None))

        self.start_date_4.setText(QCoreApplication.translate("dashboard", u"Pie chart", None))
        self.start_date_5.setText(QCoreApplication.translate("dashboard", u"Bar chart", None))
        self.start_date_6.setText(QCoreApplication.translate("dashboard", u"Line graph", None))
        self.label_7.setText(QCoreApplication.translate("dashboard", u"Settings", None))
    # retranslateUi

