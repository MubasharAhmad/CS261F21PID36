#  scrap window management file
import sys
from typing import Text
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5.QtGui import QPalette
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from threading import Thread

# to access files from another folder
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from Windows_UI_Py_Files.scarpeWindow import Ui_ScrapWindow
from scrapping import Scrapping
from threading import Thread
# from time import sleep
from File_Handling.txtFile import TxtFile

class ScrapOnDiffThread(Thread):
    def run(self):
        self.obj.start_scrapping()

    def set(self, obj):
        self.obj = obj


class LoadCSV(Thread):
    data = []
    def run(self):
        self.df = pd.read_csv("CSV_Files/books.csv")
        self.data = self.df.to_dict('records')


class ScrapWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ScrapWindow()
        self.ui.setupUi(self)
        self.scrapping = Scrapping(self.ui.progressBar, self.ui.startBtn_ScrapeWindow, self.ui.stopBtn_ScrapeWindow, self.ui.label_2, self.ui.ScrapeWindowTable)

        self.f = TxtFile()
        self.data = self.f.readFile(r"TextFiles\data.txt")
        self.num = int(self.data[2])
        self.num = (self.num / 1000000) * 100
        self.ui.progressBar.setFormat("%.0002f %%" % self.num)
        self.ui.progressBar.setValue(self.num)

        self.LoadBtn_Clicked = False


        # setting the width of each column in table
        for i in range(8):
            self.ui.ScrapeWindowTable.setColumnWidth(i, self.ui.ScrapeWindowTable.width() / 7)

        self.ui.sortDataBtn_ScrapeWindow.clicked.connect(self.sortDataBtn_clicked)
        self.ui.searchDataBtn_ScrapeWindow.clicked.connect(self.searchDataBtn_clicked)
        self.ui.startBtn_ScrapeWindow.clicked.connect(self.startBtn_clicked)
        self.ui.stopBtn_ScrapeWindow.clicked.connect(self.stopBtn_clicked)
        self.ui.loadBtn_ScrapeWindow.clicked.connect(self.loadBtn_clicked)
        # self.ui.ScrapeWindowTable.setAlternatingRowColors(True)
        # self.ui.ScrapeWindowTable.setForegroundRole(QtGui.QPalette.ColorRole.Foreground)

        # value = 10.99
        self.ui.progressBar.setMaximum(100)
        
        # self.ui.label_2.setText()
    
    def startBtn_clicked(self):
        t1 = ScrapOnDiffThread()
        t1.set(self.scrapping)
        t1.start()
        print("start btn clicked")

    def stopBtn_clicked(self):
        self.scrapping.running = False
        print("stop btn clicked")

    def loadBtn_clicked(self):
        print("load btn clicked")
        if self.LoadBtn_Clicked == False:
            csv = LoadCSV()
            self.LoadBtn_Clicked = True
            csv.start()
            csv.join()
            self.tableData = csv.data
            th = Thread(target=self.tableThread)
            th.start()
            th.join()
        else:
            self.showMessage("File can be loaded once!")

    def tableThread(self):
        self.showDataToTable()

    def showDataToTable(self):
        row_number = 0
        self.ui.ScrapeWindowTable.setRowCount(len(self.tableData))
        for line in self.tableData:
            self.ui.ScrapeWindowTable.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(line['Name'])))
            self.ui.ScrapeWindowTable.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(line['Id'])))
            self.ui.ScrapeWindowTable.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(line['Price'])))
            self.ui.ScrapeWindowTable.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(line['Pages'])))
            self.ui.ScrapeWindowTable.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str(line['Author'])))
            self.ui.ScrapeWindowTable.setItem(row_number, 5, QtWidgets.QTableWidgetItem(str(line['Language'])))
            self.ui.ScrapeWindowTable.setItem(row_number, 6, QtWidgets.QTableWidgetItem(str(line['Type'])))
            row_number += 1

    def showMessage(self, message):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("msg box")
        msg.setText(message)
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        # msg.setIcon(QMessageBox.Critical)
        # msg.setIcon(QMessageBox.Information)
        # msg.setIcon(QtWidgets.QMessageBox.Question)
        # msg.setDetailedText("Details are here")
        x = msg.exec_()
    
     # when sortDataBtn will be clicked this method will be called
    def sortDataBtn_clicked(self):
        from Windows_UI_Controller.Sort_Window import SortWindow
        self.sortWindow = SortWindow()
        self.sortWindow.show()
        self.close()
    
    # when searchDataBtn will be clicked this method will be called
    def searchDataBtn_clicked(self):
        from Windows_UI_Controller.Search_Window import SearchWindow
        self.searchWindow = SearchWindow()
        self.searchWindow.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ScrapWindow()
    win.show()
    sys.exit(app.exec_())

