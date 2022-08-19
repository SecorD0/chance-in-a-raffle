from PyQt5 import QtGui, QtWidgets

from utils.files import resource_path
from windows.interface.main import Ui_main_window


def comb(n, k):
    if 0 <= k <= n:
        nn = 1
        kk = 1
        for t in range(1, min(k, n - k) + 1):
            nn *= n
            kk *= t
            n -= 1
        return nn // kk
    return 0


class Main_window(QtWidgets.QWidget, Ui_main_window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # --- Window setting
        self.setFixedSize(280, 145)
        self.setWindowIcon(QtGui.QIcon(resource_path('images/icons/app.ico')))

        # --- Button signals
        self.pushButton_calculate.clicked.connect(self.calculate)

    def calculate(self):
        try:
            total = int(self.lineEdit_total.text().replace(' ', ''))
            taken = int(self.lineEdit_taken.text().replace(' ', ''))
            winning = int(self.lineEdit_winning.text().replace(' ', ''))

            if taken == 1:
                chance = winning / total * 100
            else:
                chance = (1 - comb(total - winning, taken) / comb(total, taken)) * 100

            self.lineEdit_chance.setText(str(round(chance, 2)).replace('.', ',') + '%')

        except ValueError:
            QtWidgets.QMessageBox.critical(self, 'Error!', "One of the entered values isn't a number!",
                                           QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)

        except:
            QtWidgets.QMessageBox.critical(self, 'Error!', 'Something went wrong!', QtWidgets.QMessageBox.Ok,
                                           QtWidgets.QMessageBox.Ok)
