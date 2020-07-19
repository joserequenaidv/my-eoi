import sys

from PyQt5.QtWidgets import QApplication

from mywidgets import MyMainWindow
from settings import *


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setApplicationName(APP_TITLE)

    window = MyMainWindow()
    window.show()

    sys.exit(app.exec())
