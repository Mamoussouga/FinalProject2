from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SecondWindow(object):
    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(500, 430)
        SecondWindow.setMinimumSize(QtCore.QSize(500, 430))
        SecondWindow.setMaximumSize(QtCore.QSize(500, 430))
        self.centralwidget = QtWidgets.QWidget(parent=SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TitleLabel2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.TitleLabel2.setGeometry(QtCore.QRect(140, 0, 351, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.TitleLabel2.setFont(font)
        self.TitleLabel2.setObjectName("TitleLabel2")
        self.GeneratedLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.GeneratedLabel.setGeometry(QtCore.QRect(10, 80, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.GeneratedLabel.setFont(font)
        self.GeneratedLabel.setObjectName("GeneratedLabel")
        self.ReturnButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.ReturnButton.setGeometry(QtCore.QRect(200, 260, 171, 61))
        self.ReturnButton.setObjectName("ReturnButton")
        self.PasswordBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.PasswordBrowser.setGeometry(QtCore.QRect(130, 120, 291, 121))
        self.PasswordBrowser.setObjectName("PasswordBrowser")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 24))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.TitleLabel2.setText(_translate("SecondWindow", "Password Generator"))
        self.GeneratedLabel.setText(_translate("SecondWindow", "Generated Password(s):"))
        self.ReturnButton.setText(_translate("SecondWindow", "Return to Main Menu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec())
