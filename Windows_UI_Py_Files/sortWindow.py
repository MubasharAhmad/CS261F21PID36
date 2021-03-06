# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sortWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SortWindow(object):
    def setupUi(self, SortWindow):
        SortWindow.setObjectName("SortWindow")
        SortWindow.resize(955, 600)
        SortWindow.setStyleSheet("background-color: rgb(44, 62, 80);\n"
"QMainWindow{\n"
"font: 12pt \"Segoe UI\";\n"
"}")
        self.centralwidget = QtWidgets.QWidget(SortWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.GoBackBtn_SortWindow = QtWidgets.QPushButton(self.centralwidget)
        self.GoBackBtn_SortWindow.setGeometry(QtCore.QRect(20, 20, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.GoBackBtn_SortWindow.setFont(font)
        self.GoBackBtn_SortWindow.setStyleSheet("QPushButton{\n"
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
        self.GoBackBtn_SortWindow.setObjectName("GoBackBtn_SortWindow")
        self.SearchBtn_SortWindow = QtWidgets.QPushButton(self.centralwidget)
        self.SearchBtn_SortWindow.setGeometry(QtCore.QRect(800, 20, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.SearchBtn_SortWindow.setFont(font)
        self.SearchBtn_SortWindow.setStyleSheet("QPushButton{\n"
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
        self.SearchBtn_SortWindow.setObjectName("SearchBtn_SortWindow")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 10, 631, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(189, 195, 199);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 140, 921, 421))
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
        self.label_2.setGeometry(QtCore.QRect(20, 100, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(189, 195, 199);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.SortingAlgoCB = QtWidgets.QComboBox(self.centralwidget)
        self.SortingAlgoCB.setGeometry(QtCore.QRect(220, 100, 121, 31))
        self.SortingAlgoCB.setStyleSheet("color:rgb(236, 240, 241);\n"
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
        self.SortingAlgoCB.setObjectName("SortingAlgoCB")
        self.SortingAlgoCB.addItem("")
        self.SortingAlgoCB.addItem("")
        self.SortingAlgoCB.addItem("")
        self.SortingAlgoCB.addItem("")
        self.SortingAlgoCB.addItem("")
        self.SortingAlgoCB.addItem("")
        self.SortingAlgoCB.addItem("")
        self.SortingAlgoCB.addItem("")
        self.SortingAlgoCB.addItem("")
        self.SortingAlgoCB.addItem("")
        self.SortingAlgoCB.addItem("")
        self.SortingAlgoCB.addItem("")
        self.SortingAlgoCB.addItem("")
        self.SortingAlgoCB.addItem("")
        self.Multi_level_sort_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.Multi_level_sort_checkBox.setGeometry(QtCore.QRect(470, 100, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.Multi_level_sort_checkBox.setFont(font)
        self.Multi_level_sort_checkBox.setStyleSheet("color: rgb(236, 240, 241);")
        self.Multi_level_sort_checkBox.setObjectName("Multi_level_sort_checkBox")
        self.Decre_incre_checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.Decre_incre_checkBox.setGeometry(QtCore.QRect(350, 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.Decre_incre_checkBox.setFont(font)
        self.Decre_incre_checkBox.setStyleSheet("color: rgb(236, 240, 241);")
        self.Decre_incre_checkBox.setObjectName("Decre_incre_checkBox")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(670, 100, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(236, 240, 241);")
        self.label_3.setObjectName("label_3")
        self.show_time_label = QtWidgets.QLabel(self.centralwidget)
        self.show_time_label.setGeometry(QtCore.QRect(850, 100, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.show_time_label.setFont(font)
        self.show_time_label.setStyleSheet("color: rgb(236, 240, 241);")
        self.show_time_label.setObjectName("show_time_label")
        SortWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SortWindow)
        self.statusbar.setObjectName("statusbar")
        SortWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SortWindow)
        QtCore.QMetaObject.connectSlotsByName(SortWindow)

    def retranslateUi(self, SortWindow):
        _translate = QtCore.QCoreApplication.translate
        SortWindow.setWindowTitle(_translate("SortWindow", "Sort Window"))
        self.GoBackBtn_SortWindow.setText(_translate("SortWindow", "Go Back"))
        self.SearchBtn_SortWindow.setText(_translate("SortWindow", "Search Data"))
        self.label.setText(_translate("SortWindow", "Sort Data"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("SortWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("SortWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("SortWindow", "Price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("SortWindow", "Pages"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("SortWindow", "Author"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("SortWindow", "Language"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("SortWindow", "Type"))
        self.label_2.setText(_translate("SortWindow", "Select Sorting Algorithm:"))
        self.SortingAlgoCB.setItemText(0, _translate("SortWindow", "Merge"))
        self.SortingAlgoCB.setItemText(1, _translate("SortWindow", "Selection"))
        self.SortingAlgoCB.setItemText(2, _translate("SortWindow", "Insertion"))
        self.SortingAlgoCB.setItemText(3, _translate("SortWindow", "Bubble"))
        self.SortingAlgoCB.setItemText(4, _translate("SortWindow", "Quick"))
        self.SortingAlgoCB.setItemText(5, _translate("SortWindow", "Counting"))
        self.SortingAlgoCB.setItemText(6, _translate("SortWindow", "Bucket"))
        self.SortingAlgoCB.setItemText(7, _translate("SortWindow", "Radix"))
        self.SortingAlgoCB.setItemText(8, _translate("SortWindow", "Heap"))
        self.SortingAlgoCB.setItemText(9, _translate("SortWindow", "Cycle"))
        self.SortingAlgoCB.setItemText(10, _translate("SortWindow", "Bitonic"))
        self.SortingAlgoCB.setItemText(11, _translate("SortWindow", "Pancake"))
        self.SortingAlgoCB.setItemText(12, _translate("SortWindow", "Patience"))
        self.SortingAlgoCB.setItemText(13, _translate("SortWindow", "Smooth"))
        self.Multi_level_sort_checkBox.setText(_translate("SortWindow", "Multi-level Sorting"))
        self.Decre_incre_checkBox.setText(_translate("SortWindow", "Decreasing"))
        self.label_3.setText(_translate("SortWindow", "Time taken to sort:"))
        self.show_time_label.setText(_translate("SortWindow", "0 ms"))
