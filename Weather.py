# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Weather.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setStyleSheet(u"")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, -10, 461, 501))
        self.label.setMaximumSize(QSize(461, 501))
        self.label.setPixmap(QPixmap(u"C:/Users/Maxim/Desktop/Weather/5c56e8b71938e168b37d0b3f.jpg"))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 0, 151, 131))
        self.label_2.setPixmap(QPixmap(u"C:/Users/Maxim/Desktop/Weather/icons8-\u043f\u043e\u0433\u043e\u0434\u0430-144.png"))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 40, 271, 51))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"background-color:#660000;\n"
"border:5px solid rgb(164, 19, 19);\n"
"border-radius:20;\n"
"color:white;\n"
"")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(40, 100, 231, 51))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift Condensed")
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setWeight(50)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color:#660000;\n"
"	border:5px solid rgb(164, 19, 19);\n"
"	border-radius:20;\n"
"	color:white;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color:#D1001C\n"
"}")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 170, 421, 301))
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color:white;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u0443\u0447\u0438\u0442\u044c", None))
        self.label_3.setText("")
    # retranslateUi

