#  search window management file
import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from threading import Thread

# to access files from another folder
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from Windows_UI_Py_Files.searchWindow import Ui_SearchWindow


class SearchWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)
        self.header = ["Name","Id","Price","Pages","Author","Language","Type"]
        th = Thread(target= self.load)
        th.start()

        # setting the width of each column in table
        for i in range(8):
            self.ui.tableWidget.setColumnWidth(i, self.ui.tableWidget.width() / 7)

        self.ui.GoBackBtn_SearchWindow.clicked.connect(self.GoBackBtn_clicked)
        self.ui.tableWidget.horizontalHeader().sectionClicked.connect(self.headerClicked)
        self.ui.search_input_complex_btn.clicked.connect(self.go_btn_clicked)
    
    # for composite filter
    def go_btn_clicked(self):
        text = self.ui.search_input_complex.text()
        if text == "":
            self.showMsg("Field should not be empty or \ncheck what you have entered?", QtWidgets.QMessageBox.Warning)
        else:
            from searching.compositeFilter import CompositeFilter
            fil = CompositeFilter(self.tableData)
            fil.search(text)
            self.loadOutput()
            if self.output == []:
                self.showMsg("Record not found", QtWidgets.QMessageBox.Warning)
    
    def headerClicked(self, logIcalindex):
        col = self.header[logIcalindex]
        # print(col)
        from searching.search import Search
        Search.Key = col

        searchAlgo = self.ui.SearchAlgoCB.currentText()
        text = self.ui.search_input.text()
        isFilter = self.ui.filters_checkBox.isChecked()
        if isFilter == False:
            if text == "":
                self.showMsg("Field should not be empty", QtWidgets.QMessageBox.Warning)
            # linear search
            elif searchAlgo == "linear":
                from searching.linearSearch import LinearSearch
                search = LinearSearch(self.tableData)
                search.search(text)
                self.loadOutput()
                if self.output == []:
                    self.showMsg("Record not found", QtWidgets.QMessageBox.Warning)
            # binary search
            elif searchAlgo == "binary":
                from searching.binarySearch import BinarySearch
                from sorting.sort import Sort
                Sort.Key = col
                from sorting.mergeSort import MergeSort
                mergeSort = MergeSort(self.tableData)
                result = mergeSort.sort()
                
                search = BinarySearch(result)
                search.search(text)
                self.loadOutput()
                if self.output == []:
                    self.showMsg("Record not found", QtWidgets.QMessageBox.Warning)
            # exponential search
            elif searchAlgo == "exponential":
                from searching.exponentialSearch import ExponentialSearch
                from sorting.sort import Sort
                Sort.Key = col
                from sorting.mergeSort import MergeSort
                mergeSort = MergeSort(self.tableData)
                result = mergeSort.sort()
                
                search = ExponentialSearch(result)
                search.search(text)
                self.loadOutput()
                if self.output == []:
                    self.showMsg("Record not found", QtWidgets.QMessageBox.Warning)
        else:
            if text == "":
                self.showMsg("Field should not be empty", QtWidgets.QMessageBox.Warning)
            else:
                from searching.filterData import FilterData
                fil = FilterData(self.tableData)
                fil.search(text)
                self.loadOutput()
                if self.output == []:
                    self.showMsg("Record not found", QtWidgets.QMessageBox.Warning)


    # method to show message
    def showMsg(self, text, icon):
        msg = QtWidgets.QMessageBox()
        msg.setText(text)
        msg.setIcon(icon)
        x = msg.exec_()
    
    # when GoBackBtn will be clicked this method will be called
    def GoBackBtn_clicked(self):
        from Windows_UI_Controller.Sort_Window import SortWindow
        self.sortWindow = SortWindow()
        self.sortWindow.show()
        self.close()

    def loadOutput(self):
        from Scrap_Window import LoadCSV
        load = LoadCSV()
        load.path = r"CSV_Files/output.csv"
        load.start()
        load.join()
        self.output = load.data
        # print(type(self.tableData[0]["Price"]))
        self.showDataToTable(self.output)
    
    def load(self):
        from Scrap_Window import LoadCSV
        load = LoadCSV()
        load.path = r"CSV_Files/UI_Scrapped_data.csv"
        load.start()
        load.join()
        self.tableData = load.data
        # print(type(self.tableData[0]["Price"]))
        self.showDataToTable(self.tableData)
    
    # method to show data on table
    def showDataToTable(self, Data):
        row_number = 0
        self.ui.tableWidget.setRowCount(len(Data))
        for line in Data:
            self.ui.tableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(line['Name'])))
            self.ui.tableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(line['Id'])))
            self.ui.tableWidget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(line['Price'])))
            self.ui.tableWidget.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(line['Pages'])))
            self.ui.tableWidget.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str(line['Author'])))
            self.ui.tableWidget.setItem(row_number, 5, QtWidgets.QTableWidgetItem(str(line['Language'])))
            self.ui.tableWidget.setItem(row_number, 6, QtWidgets.QTableWidgetItem(str(line['Type'])))
            row_number += 1


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = SearchWindow()
    win.show()
    sys.exit(app.exec_())
