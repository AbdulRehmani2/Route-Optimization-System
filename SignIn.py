# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignIn.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import csv
from SignUp import Ui_Dialog_2 as SignUpDialog

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(470, 462)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 471, 461))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 471, 81))
        self.frame_2.setStyleSheet("background-color:#993300;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(0, 10, 471, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#fff;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(200, 40, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:#fff;")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(180, 110, 121, 41))
        font = QtGui.QFont()
        font.setFamily("CentSchbkCyrill BT")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#993300;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 200, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:#993300;")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(30, 270, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:#993300;")
        self.label_5.setObjectName("label_5")
        self.username = QtWidgets.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(140, 200, 251, 31))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(140, 260, 251, 31))
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(120, 320, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:#000;")
        self.label_6.setObjectName("label_6")
        self.SignUpButton = QtWidgets.QPushButton(self.frame)
        self.SignUpButton.setGeometry(QtCore.QRect(300, 320, 93, 28))
        self.SignUpButton.setStyleSheet("background-color:#993300;\n"
"color:#fff")
        self.SignUpButton.setObjectName("SignUpButton")
        self.SignInButton = QtWidgets.QPushButton(self.frame)
        self.SignInButton.setGeometry(QtCore.QRect(140, 400, 251, 31))
        self.SignInButton.setStyleSheet("background-color:#993300;\n"
"color:#fff")
        self.SignInButton.setObjectName("SignInButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", " Route Optimization and Management"))
        self.label_2.setText(_translate("Dialog", "System"))
        self.label_3.setText(_translate("Dialog", "Login"))
        self.label_4.setText(_translate("Dialog", "Username:"))
        self.label_5.setText(_translate("Dialog", "Password:"))
        self.label_6.setText(_translate("Dialog", "Don\'t have an account?"))
        self.SignUpButton.setText(_translate("Dialog", "SignUp"))
        self.SignInButton.setText(_translate("Dialog", "SignIn"))

def decryption(text, shift):
    decrypted_text = ""
    for char in text:
        shifted = ord(char) - (shift % 26)
        if char.isalpha():
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            decrypted_text += chr(shifted)
        elif char.isnumeric():
            if shifted > ord('9'):
                shifted -= 10
            elif shifted < ord('0'):
                shifted += 10
            decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text


def read_from_csv(username, password):
    with open('users.csv', mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if username == row[0]:
                decrypted_password = decryption(row[1], 3) 
                if password == decrypted_password:
                    decrypted_email = decryption(row[2], 3) 
                    return True, decrypted_email
                else:
                    return False, None
        return False, None 
    
class SignInDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.SignInButton.clicked.connect(self.sign_in)
        self.SignUpButton.clicked.connect(self.show_sign_up)

    def sign_in(self):
        username = self.username.text()
        password = self.password.text()
        authenticated, decrypted_email = read_from_csv(username, password)
        if authenticated:
            print("Login successful! Email:", decrypted_email)
        else:
            print("Invalid credentials. Please try again.")

    def show_sign_up(self):
        sign_up_dialog = QDialog()
        sign_up_ui = SignUpDialog()
        sign_up_ui.setupUi(sign_up_dialog)
        sign_up_dialog.exec_()

def main():
    app = QtWidgets.QApplication([])
    sign_in_dialog = SignInDialog()
    sign_in_dialog.show()
    app.exec_()

if __name__ == "__main__":
    main()