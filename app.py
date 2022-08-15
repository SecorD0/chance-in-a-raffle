import sys

from PyQt5 import QtWidgets

from windows.functionality.main import Window

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())
