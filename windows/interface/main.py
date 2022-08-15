from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(280, 145)
        self.layoutWidget = QtWidgets.QWidget(main_window)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 261, 132))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_total = QtWidgets.QLabel(self.layoutWidget)
        self.label_total.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_total.setObjectName("label_total")
        self.gridLayout.addWidget(self.label_total, 0, 0, 1, 1)
        self.lineEdit_total = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_total.setObjectName("lineEdit_total")
        self.gridLayout.addWidget(self.lineEdit_total, 0, 1, 1, 1)
        self.label_taken = QtWidgets.QLabel(self.layoutWidget)
        self.label_taken.setObjectName("label_taken")
        self.gridLayout.addWidget(self.label_taken, 1, 0, 1, 1)
        self.lineEdit_taken = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_taken.setObjectName("lineEdit_taken")
        self.gridLayout.addWidget(self.lineEdit_taken, 1, 1, 1, 1)
        self.label_winning = QtWidgets.QLabel(self.layoutWidget)
        self.label_winning.setObjectName("label_winning")
        self.gridLayout.addWidget(self.label_winning, 2, 0, 1, 1)
        self.lineEdit_winning = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_winning.setObjectName("lineEdit_winning")
        self.gridLayout.addWidget(self.lineEdit_winning, 2, 1, 1, 1)
        self.label_chance = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(69)
        sizePolicy.setVerticalStretch(13)
        sizePolicy.setHeightForWidth(self.label_chance.sizePolicy().hasHeightForWidth())
        self.label_chance.setSizePolicy(sizePolicy)
        self.label_chance.setObjectName("label_chance")
        self.gridLayout.addWidget(self.label_chance, 4, 0, 1, 1)
        self.lineEdit_chance = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_chance.setReadOnly(True)
        self.lineEdit_chance.setClearButtonEnabled(False)
        self.lineEdit_chance.setObjectName("lineEdit_chance")
        self.gridLayout.addWidget(self.lineEdit_chance, 4, 1, 1, 1)
        self.pushButton_calculate = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_calculate.setObjectName("pushButton_calculate")
        self.gridLayout.addWidget(self.pushButton_calculate, 3, 0, 1, 2)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Chance in a raffle"))
        self.label_total.setText(_translate("main_window", "Total"))
        self.label_taken.setText(_translate("main_window", "Taken"))
        self.label_winning.setText(_translate("main_window", "Winning"))
        self.label_chance.setText(_translate("main_window", "Chance to win"))
        self.pushButton_calculate.setText(_translate("main_window", "Calculate"))