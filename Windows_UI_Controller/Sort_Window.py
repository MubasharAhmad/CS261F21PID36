#  sort window management file
import sys
from threading import Thread
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

# to access files from another folder
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from File_Handling.txtFile import TxtFile
from Windows_UI_Py_Files.sortWindow import Ui_SortWindow


class SortWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SortWindow()
        self.ui.setupUi(self)
        th = Thread(target= self.load)
        th.start()
        self.f = True
        self.header = ["Name","Id","Price","Pages","Author","Language","Type"]
        f = open(r"TextFiles\multiSortingData.txt", "w")
        f.writelines([])
        f.close()
        # setting the width of each column in table
        for i in range(8):
            self.ui.tableWidget.setColumnWidth(i, self.ui.tableWidget.width() / 7)

        self.ui.SearchBtn_SortWindow.clicked.connect(self.SearchBtn_clicked)
        self.ui.GoBackBtn_SortWindow.clicked.connect(self.GoBackBtn_clicked)
        self.ui.tableWidget.horizontalHeader().sectionClicked.connect(self.headerClicked)
    
    def headerClicked(self, logicalIndex):
        from time_manager.time import Time
        t = Time()
        from sorting.sort import Sort
        colHeader = self.header[logicalIndex]
        Sort.Key = colHeader
        cbText = self.ui.SortingAlgoCB.currentText()
        reverse = self.ui.Decre_incre_checkBox.isChecked()
        multiSorting = self.ui.Multi_level_sort_checkBox.isChecked()

        if multiSorting == False:
        # selection sort
            if cbText == "Selection":
                from sorting.selectionSort import SelectionSort
                selection = SelectionSort(self.tableData)

                t.start()
                result = selection.sort(reverse)
                self.ui.show_time_label.setText(t.end())
                self.ui.show_time_label.adjustSize()

                self.showDataToTable(result)
            # insertion sort
            elif cbText == "Insertion":
                from sorting.insertionSort import InsertionSort
                insertion = InsertionSort(self.tableData)

                t.start()
                result = insertion.sort(reverse)
                self.ui.show_time_label.setText(t.end())
                self.ui.show_time_label.adjustSize()

                self.showDataToTable(result)
            # bubble sort
            elif cbText == "Bubble":
                from sorting.bubbleSort import BubbleSort
                bubble = BubbleSort(self.tableData)

                t.start()
                result = bubble.sort(reverse)
                self.ui.show_time_label.setText(t.end())
                self.ui.show_time_label.adjustSize()

                self.showDataToTable(result)
            # merge sort
            elif cbText == "Merge":
                from sorting.mergeSort import MergeSort
                merge = MergeSort(self.tableData)

                t.start()
                result = merge.sort(reverse)
                self.ui.show_time_label.setText(t.end())
                self.ui.show_time_label.adjustSize()

                self.showDataToTable(result)
            # heap sort
            elif cbText == "Heap":
                from sorting.heapSort import HeapSort
                heap = HeapSort(self.tableData)

                t.start()
                result = heap.sort(reverse)
                self.ui.show_time_label.setText(t.end())
                self.ui.show_time_label.adjustSize()

                self.showDataToTable(result)
            # bitonic sort
            elif cbText == "Bitonic":
                from sorting.bitonicSort import BitonicSort
                bitonic = BitonicSort(self.tableData)

                t.start()
                result = bitonic.sort(reverse)
                self.ui.show_time_label.setText(t.end())
                self.ui.show_time_label.adjustSize()

                self.showDataToTable(result)
            # cycle sort
            elif cbText == "Cycle":
                from sorting.cycleSort import CycleSort
                cycle = CycleSort(self.tableData)

                t.start()
                result = cycle.sort(reverse)
                self.ui.show_time_label.setText(t.end())
                self.ui.show_time_label.adjustSize()

                self.showDataToTable(result)
            # quick sort
            elif cbText == "Quick":
                from sorting.quickSort import QuickSort
                quick = QuickSort(self.tableData)

                t.start()
                result = quick.sort(reverse)
                self.ui.show_time_label.setText(t.end())
                self.ui.show_time_label.adjustSize()

                self.showDataToTable(result)
            # radix sort
            elif cbText == "Radix":
                from sorting.radixSort import RadixSort
                radix = RadixSort(self.tableData, 1)

                t.start()
                result = radix.sort(reverse)
                self.ui.show_time_label.setText(t.end())
                self.ui.show_time_label.adjustSize()

                self.showDataToTable(result)
            # pancake sort
            elif cbText == "Pancake":
                from sorting.pancakeSort import PancakeSort
                pancake = PancakeSort(self.tableData)

                t.start()
                result = pancake.sort(reverse)
                self.ui.show_time_label.setText(t.end())
                self.ui.show_time_label.adjustSize()

                self.showDataToTable(result)
            # patience sort
            elif cbText == "Patience":
                from sorting.patienceSort import PatienceSort
                patience = PatienceSort(self.tableData)

                t.start()
                result = patience.sort(reverse)
                self.ui.show_time_label.setText(t.end())
                self.ui.show_time_label.adjustSize()

                self.showDataToTable(result)
        # for implementing multi level sorting
        elif multiSorting and cbText == "Merge":
            from Scrap_Window import LoadCSV
            load = LoadCSV()
            load.path = r"CSV_Files/multiLevelSortingOutput.csv"
            load.start()
            load.join()
            t = TxtFile()
            data = ""
            try:
                data = (t.readFile(r"TextFiles\multiSortingData.txt"))[0]
            except:
                pass
            from sorting.multiLevelSorting import MultiLevelSorting
            multi = MultiLevelSorting(load.data, data)
            sortedData = multi.sort()

            self.showDataToTable(sortedData)

    def load(self):
        from Scrap_Window import LoadCSV
        load = LoadCSV()
        load.path = r"CSV_Files/UI_Scrapped_data.csv"
        load.start()
        load.join()
        self.tableData = load.data
        # print(type(self.tableData[0]["Price"]))
        self.showDataToTable(self.tableData)
    
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

    # when SearchBtn will be clicked this method will be called
    def SearchBtn_clicked(self):
        from Windows_UI_Controller.Search_Window import SearchWindow
        self.searchWindow = SearchWindow()
        self.searchWindow.show()
        self.close()
    
    # when GoBackBtn will be clicked this method will be called
    def GoBackBtn_clicked(self):
        from Windows_UI_Controller.Scrap_Window import ScrapWindow
        self.scrapWindow = ScrapWindow()
        self.scrapWindow.show()
        self.close()
    
    def showMessage(self, message, icon):
        msg = QtWidgets.QMessageBox()
        msg.setText(message)
        # QtWidgets.QMessageBox.Information
        msg.setIcon(icon)
        x = msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = SortWindow()
    win.show()
    sys.exit(app.exec_())
