#  sort window management file
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# to access files from another folder
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from Windows_UI_Py_Files.sortWindow import Ui_SortWindow


class SortWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SortWindow()
        self.ui.setupUi(self)

        # setting the width of each column in table
        for i in range(8):
            self.ui.tableWidget.setColumnWidth(i, self.ui.tableWidget.width() / 7)

        self.ui.SearchBtn_SortWindow.clicked.connect(self.SearchBtn_clicked)
        self.ui.GoBackBtn_SortWindow.clicked.connect(self.GoBackBtn_clicked)
    
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = SortWindow()
    win.show()
    sys.exit(app.exec_())
