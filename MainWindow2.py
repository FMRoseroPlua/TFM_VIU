# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1104, 773)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.barb = QProgressBar(self.centralwidget)
        self.barb.setObjectName(u"barb")
        self.barb.setMaximumSize(QSize(125, 16777215))
        self.barb.setValue(0)

        self.gridLayout.addWidget(self.barb, 8, 4, 1, 1)

        self.barn = QProgressBar(self.centralwidget)
        self.barn.setObjectName(u"barn")
        self.barn.setMaximumSize(QSize(125, 16777215))
        self.barn.setValue(0)

        self.gridLayout.addWidget(self.barn, 7, 4, 1, 1)

        self.btnstart = QPushButton(self.centralwidget)
        self.btnstart.setObjectName(u"btnstart")

        self.gridLayout.addWidget(self.btnstart, 11, 0, 1, 1)

        self.lbpredicciones = QLabel(self.centralwidget)
        self.lbpredicciones.setObjectName(u"lbpredicciones")
        self.lbpredicciones.setStyleSheet(u"")

        self.gridLayout.addWidget(self.lbpredicciones, 7, 3, 1, 1)

        self.table = QTableView(self.centralwidget)
        self.table.setObjectName(u"table")

        self.gridLayout.addWidget(self.table, 0, 0, 11, 3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 8, 3, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 9, 3, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 3, 1, 2)

        self.foco = QLabel(self.centralwidget)
        self.foco.setObjectName(u"foco")
        self.foco.setMinimumSize(QSize(70, 70))
        self.foco.setMaximumSize(QSize(70, 70))
        self.foco.setStyleSheet(u"border-radius: 35px;\n"
"\n"
"background-color: rgb(255, 88, 88);\n"
"background-color: rgb(0, 170, 127);")

        self.gridLayout.addWidget(self.foco, 2, 3, 1, 1)

        self.lbcondicion = QLabel(self.centralwidget)
        self.lbcondicion.setObjectName(u"lbcondicion")
        self.lbcondicion.setMinimumSize(QSize(0, 70))
        self.lbcondicion.setStyleSheet(u"background-color: rgb(170, 255, 127);\n"
"background-color: rgba(19, 11, 255,150);\n"
"background-color: rgb(255, 255, 127,170);\n"
"background-color: rgb(255, 170, 0, 170);\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"font-size:15pt;\n"
"color: rgb(6, 255, 14);\n"
"color: rgb(239, 117, 255);")

        self.gridLayout.addWidget(self.lbcondicion, 4, 3, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 11, 2, 1, 1)

        self.btnstop = QPushButton(self.centralwidget)
        self.btnstop.setObjectName(u"btnstop")

        self.gridLayout.addWidget(self.btnstop, 11, 1, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 6, 3, 1, 2)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 0, 3, 1, 2)

        self.barf = QProgressBar(self.centralwidget)
        self.barf.setObjectName(u"barf")
        self.barf.setMaximumSize(QSize(125, 16777215))
        self.barf.setValue(0)

        self.gridLayout.addWidget(self.barf, 9, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 5, 3, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnstart.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.lbpredicciones.setText(QCoreApplication.translate("MainWindow", u"Normal Condition", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Air Blockage or Air Leakage", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Diverted Flow", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CONDICIONES DE FUNCIONAMIENTO", None))
        self.foco.setText("")
        self.lbcondicion.setText("")
        self.btnstop.setText(QCoreApplication.translate("MainWindow", u"Detener", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"PORCENTAJE DE ESTADO DIARIO", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"ESTADO NORMAL/FALLA", None))
    # retranslateUi

