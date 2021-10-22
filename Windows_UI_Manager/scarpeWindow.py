# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scarpeWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ScrapWindow(object):
    def setupUi(self, ScrapWindow):
        ScrapWindow.setObjectName("ScrapWindow")
        ScrapWindow.resize(955, 567)
        font = QtGui.QFont()
        font.setPointSize(12)
        ScrapWindow.setFont(font)
        ScrapWindow.setStyleSheet("background-color: rgb(44, 62, 80);")
        self.centralwidget = QtWidgets.QWidget(ScrapWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sortDataBtn_ScrapeWindow = QtWidgets.QPushButton(self.centralwidget)
        self.sortDataBtn_ScrapeWindow.setGeometry(QtCore.QRect(30, 30, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.sortDataBtn_ScrapeWindow.setFont(font)
        self.sortDataBtn_ScrapeWindow.setStyleSheet("QPushButton{\n"
"background-color: rgb(127, 140, 141);\n"
"    color: rgb(255, 255, 255);\n"
"border-style: none;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(189, 195, 199);\n"
"    color: rgb(44, 62, 80);\n"
"border-style: none;\n"
"}")
        self.sortDataBtn_ScrapeWindow.setObjectName("sortDataBtn_ScrapeWindow")
        self.searchDataBtn_ScrapeWindow = QtWidgets.QPushButton(self.centralwidget)
        self.searchDataBtn_ScrapeWindow.setGeometry(QtCore.QRect(170, 30, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.searchDataBtn_ScrapeWindow.setFont(font)
        self.searchDataBtn_ScrapeWindow.setStyleSheet("QPushButton{\n"
"background-color: rgb(127, 140, 141);\n"
"    color: rgb(255, 255, 255);\n"
"border-style: none;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(189, 195, 199);\n"
"    color: rgb(44, 62, 80);\n"
"border-style: none;\n"
"}")
        self.searchDataBtn_ScrapeWindow.setObjectName("searchDataBtn_ScrapeWindow")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(149, 165, 166);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 50, 441, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(189, 195, 199);")
        self.label_2.setObjectName("label_2")
        self.ScrapeWindowTable = QtWidgets.QTableWidget(self.centralwidget)
        self.ScrapeWindowTable.setGeometry(QtCore.QRect(30, 100, 901, 391))
        self.ScrapeWindowTable.setStyleSheet("QHeaderView::section\n"
"{\n"
"    spacing: 10px;\n"
"    background-color: rgb(127, 140, 141);\n"
"    color: white;\n"
"    border: 1px solid lightgray;\n"
"    margin: 1px;\n"
"    text-align: center;\n"
"    font: 10pt \"Segoe UI\";\n"
"}")
        self.ScrapeWindowTable.setObjectName("ScrapeWindowTable")
        self.ScrapeWindowTable.setColumnCount(7)
        self.ScrapeWindowTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.ScrapeWindowTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.ScrapeWindowTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.ScrapeWindowTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.ScrapeWindowTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.ScrapeWindowTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.ScrapeWindowTable.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.ScrapeWindowTable.setHorizontalHeaderItem(6, item)
        self.startBtn_ScrapeWindow = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn_ScrapeWindow.setGeometry(QtCore.QRect(30, 500, 51, 31))
        self.startBtn_ScrapeWindow.setStyleSheet("QPushButton{\n"
"background-color: rgb(127, 140, 141);\n"
"    color: rgb(255, 255, 255);\n"
"border-style: none;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(189, 195, 199);\n"
"    color: rgb(44, 62, 80);\n"
"border-style: none;\n"
"}")
        self.startBtn_ScrapeWindow.setObjectName("startBtn_ScrapeWindow")
        self.stopBtn_ScrapeWindow = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn_ScrapeWindow.setGeometry(QtCore.QRect(90, 500, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(8)
        self.stopBtn_ScrapeWindow.setFont(font)
        self.stopBtn_ScrapeWindow.setStyleSheet("QPushButton{\n"
"background-color: rgb(127, 140, 141);\n"
"    color: rgb(255, 255, 255);\n"
"border-style: none;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(189, 195, 199);\n"
"    color: rgb(44, 62, 80);\n"
"border-style: none;\n"
"}")
        self.stopBtn_ScrapeWindow.setObjectName("stopBtn_ScrapeWindow")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(150, 500, 631, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar{\n"
"background-color: rgb(127, 140, 141);\n"
"color: rgb(255, 255, 255);\n"
"border-style: none;\n"
"border-radius: 15px;\n"
"text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"border-radius: 15px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.482545, x2:1, y2:0.471591, stop:0 rgba(0, 0, 0, 255), stop:0.0170455 rgba(127, 14, 174, 255), stop:1 rgba(211, 104, 255, 255));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.loadBtn_ScrapeWindow = QtWidgets.QPushButton(self.centralwidget)
        self.loadBtn_ScrapeWindow.setGeometry(QtCore.QRect(820, 500, 111, 31))
        self.loadBtn_ScrapeWindow.setStyleSheet("QPushButton{\n"
"background-color: rgb(127, 140, 141);\n"
"    color: rgb(255, 255, 255);\n"
"border-style: none;\n"
"}\n"
"QPushButton::hover{\n"
"background-color: rgb(189, 195, 199);\n"
"    color: rgb(44, 62, 80);\n"
"border-style: none;\n"
"}")
        self.loadBtn_ScrapeWindow.setObjectName("loadBtn_ScrapeWindow")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(790, 510, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        ScrapWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ScrapWindow)
        self.statusbar.setObjectName("statusbar")
        ScrapWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ScrapWindow)
        QtCore.QMetaObject.connectSlotsByName(ScrapWindow)

    def retranslateUi(self, ScrapWindow):
        _translate = QtCore.QCoreApplication.translate
        ScrapWindow.setWindowTitle(_translate("ScrapWindow", "ScrapWindow"))
        self.sortDataBtn_ScrapeWindow.setText(_translate("ScrapWindow", "Sort Data"))
        self.searchDataBtn_ScrapeWindow.setText(_translate("ScrapWindow", "Search Data"))
        self.label.setText(_translate("ScrapWindow", "<strong>Scrapping Source:</strong>"))
        self.label_2.setText(_translate("ScrapWindow", "https://#"))
        item = self.ScrapeWindowTable.horizontalHeaderItem(0)
        item.setText(_translate("ScrapWindow", "Name"))
        item = self.ScrapeWindowTable.horizontalHeaderItem(1)
        item.setText(_translate("ScrapWindow", "ID"))
        item = self.ScrapeWindowTable.horizontalHeaderItem(2)
        item.setText(_translate("ScrapWindow", "Price"))
        item = self.ScrapeWindowTable.horizontalHeaderItem(3)
        item.setText(_translate("ScrapWindow", "Pages"))
        item = self.ScrapeWindowTable.horizontalHeaderItem(4)
        item.setText(_translate("ScrapWindow", "Author"))
        item = self.ScrapeWindowTable.horizontalHeaderItem(5)
        item.setText(_translate("ScrapWindow", "Language"))
        item = self.ScrapeWindowTable.horizontalHeaderItem(6)
        item.setText(_translate("ScrapWindow", "Type"))
        self.startBtn_ScrapeWindow.setText(_translate("ScrapWindow", "Start"))
        self.stopBtn_ScrapeWindow.setText(_translate("ScrapWindow", "Stop"))
        self.loadBtn_ScrapeWindow.setText(_translate("ScrapWindow", "Load From File"))
        self.label_3.setText(_translate("ScrapWindow", "Or"))
