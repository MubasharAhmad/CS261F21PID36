# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'searchWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(955, 600)
        SearchWindow.setStyleSheet("background-color: rgb(44, 62, 80);")
        self.centralwidget = QtWidgets.QWidget(SearchWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.GoBackBtn_SearchWindow = QtWidgets.QPushButton(self.centralwidget)
        self.GoBackBtn_SearchWindow.setGeometry(QtCore.QRect(20, 20, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.GoBackBtn_SearchWindow.setFont(font)
        self.GoBackBtn_SearchWindow.setStyleSheet("QPushButton{\n"
"    background-color: rgb(127, 140, 141);\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: none\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    color: rgb(44, 62, 80);\n"
"    background-color: rgb(236, 240, 241);\n"
"    border-style: none\n"
"}")
        self.GoBackBtn_SearchWindow.setObjectName("GoBackBtn_SearchWindow")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 671, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(189, 195, 199);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.show_time_label = QtWidgets.QLabel(self.centralwidget)
        self.show_time_label.setGeometry(QtCore.QRect(870, 100, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.show_time_label.setFont(font)
        self.show_time_label.setStyleSheet("color: rgb(236, 240, 241);")
        self.show_time_label.setObjectName("show_time_label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(680, 100, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(236, 240, 241);")
        self.label_3.setObjectName("label_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 140, 931, 421))
        self.tableWidget.setStyleSheet("\n"
"QHeaderView::section\n"
"{\n"
"spacing: 10px;\n"
"background-color: rgb(127, 140, 141);\n"
"color: white;\n"
"border: 1px solid white;\n"
"margin: 1px;\n"
"text-align: leftr;\n"
"gridline-color: rgb(255, 255, 255);\n"
"    selection-color: rgb(189, 195, 199);\n"
"font: 10pt \"Segoe UI\";\n"
"}\n"
"QTableWidget::item {\n"
    "color: white;\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 100, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(189, 195, 199);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.filters_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.filters_checkBox.setGeometry(QtCore.QRect(360, 100, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.filters_checkBox.setFont(font)
        self.filters_checkBox.setStyleSheet("color: rgb(236, 240, 241);")
        self.filters_checkBox.setObjectName("filters_checkBox")
        self.SearchAlgoCB = QtWidgets.QComboBox(self.centralwidget)
        self.SearchAlgoCB.setGeometry(QtCore.QRect(100, 100, 121, 31))
        self.SearchAlgoCB.setStyleSheet("color:rgb(236, 240, 241);\n"
"background-color: rgb(52, 73, 94);\n"
"font: 12pt \"Segoe UI\";\n"
" border: 1px solid gray;\n"
"\n"
"QComboBox::item {\n"
"    border-top: 4px;\n"
"    border-left: 4px;\n"
"    border-bottom: 4px;\n"
"    border-right: 4px;\n"
"}")
        self.SearchAlgoCB.setObjectName("SearchAlgoCB")
        self.SearchAlgoCB.addItem("")
        self.SearchAlgoCB.addItem("")
        self.SearchAlgoCB.addItem("")
        self.SearchAlgoCB.addItem("")
        self.search_input = QtWidgets.QLineEdit(self.centralwidget)
        self.search_input.setGeometry(QtCore.QRect(230, 100, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.search_input.setFont(font)
        self.search_input.setStyleSheet("color: lightgray;")
        self.search_input.setObjectName("search_input")
        self.search_input_complex = QtWidgets.QLineEdit(self.centralwidget)
        self.search_input_complex.setGeometry(QtCore.QRect(440, 100, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        self.search_input_complex.setFont(font)
        self.search_input_complex.setStyleSheet("color: lightgray;")
        self.search_input_complex.setObjectName("search_input_complex")
        self.search_input_complex_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_input_complex_btn.setGeometry(QtCore.QRect(630, 100, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.search_input_complex_btn.setFont(font)
        self.search_input_complex_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(127, 140, 141);\n"
"    color: rgb(255, 255, 255);\n"
"    border-style: none\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    color: rgb(44, 62, 80);\n"
"    background-color: rgb(236, 240, 241);\n"
"    border-style: none\n"
"}")
        self.search_input_complex_btn.setObjectName("search_input_complex_btn")
        SearchWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SearchWindow)
        self.statusbar.setObjectName("statusbar")
        SearchWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SearchWindow)
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)

    def retranslateUi(self, SearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchWindow.setWindowTitle(_translate("SearchWindow", "MainWindow"))
        self.GoBackBtn_SearchWindow.setText(_translate("SearchWindow", "Go Back"))
        self.label.setText(_translate("SearchWindow", "Search Data"))
        self.show_time_label.setText(_translate("SearchWindow", "0 ms"))
        self.label_3.setText(_translate("SearchWindow", "Time taken to search:"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SearchWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SearchWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SearchWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SearchWindow", "Pages"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("SearchWindow", "Author"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("SearchWindow", "Language"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("SearchWindow", "Type"))
        self.label_2.setText(_translate("SearchWindow", "Algorithm:"))
        self.filters_checkBox.setText(_translate("SearchWindow", "filters"))
        self.SearchAlgoCB.setItemText(0, _translate("SearchWindow", "linear"))
        self.SearchAlgoCB.setItemText(1, _translate("SearchWindow", "binary"))
        self.SearchAlgoCB.setItemText(2, _translate("SearchWindow", "jump"))
        self.SearchAlgoCB.setItemText(3, _translate("SearchWindow", "exponential"))
        self.search_input_complex_btn.setText(_translate("SearchWindow", "Go"))
