#  start-window management file
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

# to access files from another folder
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from Windows_UI_Py_Files.startWindow import Ui_StartWindow


class StartWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_StartWindow()
        self.ui.setupUi(self)
        self.ui.startBtn.clicked.connect(self.startBtn_clicked)

    # when startBtn will be clicked this method will be called
    def startBtn_clicked(self):
        # from Scrap_Window import ScrapWindow
        from Windows_UI_Controller.Scrap_Window import ScrapWindow
        self.scrapWindow = ScrapWindow()
        self.scrapWindow.show()

        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = StartWindow()
    win.show()
    sys.exit(app.exec_())
