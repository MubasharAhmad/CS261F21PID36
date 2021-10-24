from PyQt5.QtWidgets import QApplication
from Windows_UI_Controller.Start_Window import StartWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = StartWindow()
    win.show()
    sys.exit(app.exec_())
