import sys
import random
import string
from PyQt6 import QtCore, QtGui, QtWidgets
from PG2 import Ui_SecondWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 430)
        MainWindow.setMinimumSize(QtCore.QSize(500, 430))
        MainWindow.setMaximumSize(QtCore.QSize(500, 430))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.TitleLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.TitleLabel.setGeometry(QtCore.QRect(140, 0, 351, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setObjectName("TitleLabel")
        self.LengthLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.LengthLabel.setGeometry(QtCore.QRect(10, 80, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.LengthLabel.setFont(font)
        self.LengthLabel.setObjectName("LengthLabel")
        self.NumberLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.NumberLabel.setGeometry(QtCore.QRect(10, 110, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.NumberLabel.setFont(font)
        self.NumberLabel.setObjectName("NumberLabel")
        self.GenerateButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.GenerateButton.setGeometry(QtCore.QRect(200, 260, 171, 61))
        self.GenerateButton.setObjectName("GenerateButton")
        self.UppercaseBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.UppercaseBox.setGeometry(QtCore.QRect(10, 160, 211, 20))
        self.UppercaseBox.setObjectName("UppercaseBox")
        self.DigitsBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.DigitsBox.setGeometry(QtCore.QRect(10, 190, 151, 20))
        self.DigitsBox.setObjectName("DigitsBox")
        self.CharactersBox = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.CharactersBox.setGeometry(QtCore.QRect(10, 220, 201, 20))
        self.CharactersBox.setObjectName("CharactersBox")
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(130, 70, 41, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(160, 110, 41, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.TitleLabel.setText(_translate("MainWindow", "Password Generator"))
        self.LengthLabel.setText(_translate("MainWindow", "Password Length:"))
        self.NumberLabel.setText(_translate("MainWindow", "Number of passwords:"))
        self.GenerateButton.setText(_translate("MainWindow", "Generate Password(s)"))
        self.UppercaseBox.setText(_translate("MainWindow", "Include Uppercase Letters"))
        self.DigitsBox.setText(_translate("MainWindow", "Include Digits"))
        self.CharactersBox.setText(_translate("MainWindow", "Include Special Characters"))

class MainApplication:
        def __init__(self):
            self.app = QtWidgets.QApplication(sys.argv)
            self.main_window = QtWidgets.QMainWindow()
            self.ui_main = Ui_MainWindow()
            self.ui_main.setupUi(self.main_window)

            self.second_window = QtWidgets.QMainWindow()
            self.ui_second = Ui_SecondWindow()
            self.ui_second.setupUi(self.second_window)

            self.ui_main.GenerateButton.clicked.connect(self.generate_passwords)
            self.ui_second.ReturnButton.clicked.connect(self.show_main_window)

        def generate_passwords(self):
            try:
                length = int(self.ui_main.textEdit.toPlainText())
                count = int(self.ui_main.textEdit_2.toPlainText())
            except ValueError:
                self.ui_second.PasswordBrowser.setText("Please enter a number for password length and number of password.")
                self.show_second_window()
                return

            if length < 4 or length > 8 or count < 1 or count > 3:
                self.ui_second.PasswordBrowser.setText("Length must be 4-8. Count must be 1-3.")
                self.show_second_window()
                return

            char_pool = string.ascii_lowercase
            include_uppercase = self.ui_main.UppercaseBox.isChecked()
            include_digits = self.ui_main.DigitsBox.isChecked()
            include_specials = self.ui_main.CharactersBox.isChecked()

            if include_uppercase:
                char_pool += string.ascii_uppercase
            if include_digits:
                char_pool += string.digits
            if include_specials:
                char_pool += string.punctuation

            if not (include_uppercase or include_digits or include_specials):
                self.ui_second.PasswordBrowser.setText("No options selected. Please check at least one box.")
                self.show_second_window()
                return

            passwords = [
                ''.join(random.choices(char_pool, k=length))
                for _ in range(count)
            ]

            self.ui_second.PasswordBrowser.setText('\n'.join(passwords))
            self.show_second_window()

        def show_main_window(self):
                self.second_window.hide()
                self.main_window.show()

        def show_second_window(self):
            self.main_window.hide()
            self.second_window.show()

        def run(self):
            self.main_window.show()
            sys.exit(self.app.exec())

if __name__ == "__main__":
    app = MainApplication()
    app.run()