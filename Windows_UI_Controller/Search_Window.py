#  search window management file
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# to access files from another folder
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from Windows_UI_Py_Files.searchWindow import Ui_SearchWindow


class SearchWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self)

        # setting the width of each column in table
        for i in range(8):
            self.ui.tableWidget.setColumnWidth(i, self.ui.tableWidget.width() / 7)

        self.ui.GoBackBtn_SearchWindow.clicked.connect(self.GoBackBtn_clicked)

    # when GoBackBtn will be clicked this method will be called
    def GoBackBtn_clicked(self):
        from Windows_UI_Controller.Sort_Window import SortWindow
        self.sortWindow = SortWindow()
        self.sortWindow.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = SearchWindow()
    win.show()
    sys.exit(app.exec_())
