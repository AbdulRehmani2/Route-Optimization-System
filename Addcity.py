import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import json

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1118, 825)
        Dialog.setStyleSheet("background-color: #cccccc;\n"
                             "border-left: 4px solid #0A1172;\n"
                             "border-right: 4px solid #0A1172;\n"
                             "border-bottom: 4px solid #0A1172;")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1121, 131))
        self.frame.setStyleSheet("background-color: #0A1172;\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(150, 40, 841, 51))
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: white;")
        self.label_5.setObjectName("label_5")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(490, 200, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("border: none;\n"
                                 "color: #0a1172;\n"
                                 "")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(390, 310, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("border: none;\n"
                                   "border-bottom: 2px solid #0a1172;")
        self.label_2.setObjectName("label_2")
        self.cityname = QtWidgets.QLineEdit(Dialog)
        self.cityname.setGeometry(QtCore.QRect(570, 300, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cityname.setFont(font)
        self.cityname.setStyleSheet("border: none;\n"
                                    "border-bottom: 2px solid #0A1172;\n"
                                    "")
        self.cityname.setText("")
        self.cityname.setObjectName("cityname")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(390, 380, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("border: none;\n"
                                   "border-bottom: 2px solid #0a1172;")
        self.label_3.setObjectName("label_3")
        self.latitude = QtWidgets.QLineEdit(Dialog)
        self.latitude.setGeometry(QtCore.QRect(570, 370, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.latitude.setFont(font)
        self.latitude.setStyleSheet("border: none;\n"
                                    "border-bottom: 2px solid #0A1172;\n"
                                    "")
        self.latitude.setText("")
        self.latitude.setObjectName("latitude")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(390, 450, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("border: none;\n"
                                   "border-bottom: 2px solid #0a1172;")
        self.label_4.setObjectName("label_4")
        self.longitude = QtWidgets.QLineEdit(Dialog)
        self.longitude.setGeometry(QtCore.QRect(570, 440, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.longitude.setFont(font)
        self.longitude.setStyleSheet("border: none;\n"
                                     "border-bottom: 2px solid #0A1172;\n"
                                     "")
        self.longitude.setText("")
        self.longitude.setObjectName("longitude")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(80, 530, 431, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("border: none;\n"
                                   "border-bottom: 2px solid #0a1172;")
        self.label_6.setObjectName("label_6")
        self.adjacentDistricts = QtWidgets.QLineEdit(Dialog)
        self.adjacentDistricts.setGeometry(QtCore.QRect(570, 520, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.adjacentDistricts.setFont(font)
        self.adjacentDistricts.setStyleSheet("border: none;\n"
                                             "border-bottom: 2px solid #0A1172;\n"
                                             "")
        self.adjacentDistricts.setText("")
        self.adjacentDistricts.setObjectName("adjacentDistricts")
        self.addcity = QtWidgets.QPushButton(Dialog)
        self.addcity.setGeometry(QtCore.QRect(870, 700, 121, 51))
        self.addcity.setStyleSheet("padding: 5px;\n"
                                   "background-color: #0A1172;\n"
                                   "color: white;")
        self.addcity.setObjectName("addcity")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.addcity.clicked.connect(self.save_city_details)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "Route Optimization and Management System"))
        self.label.setText(_translate("Dialog", "Add new City"))
        self.label_2.setText(_translate("Dialog", "City name:"))
        self.label_3.setText(_translate("Dialog", "Latitude:"))
        self.label_4.setText(_translate("Dialog", "Longitude:"))
        self.label_6.setText(_translate("Dialog", "Adjacent Districts(separate each with comma):"))
        self.addcity.setText(_translate("Dialog", "Add City"))

    def save_city_details(self):
        city_name = self.cityname.text()
        city_latitude = float(self.latitude.text())
        city_longitude = float(self.longitude.text())
        adjacent_districts = self.adjacentDistricts.text().split(',')

        try:
            with open('data.txt', 'r') as file:
                city_data = json.load(file)
        except FileNotFoundError:
            city_data = {}

        city_data[city_name] = {
            "coordinates": {
                "latitude": city_latitude,
                "longitude": city_longitude
            },
            "adjacent_districts": [district.strip() for district in adjacent_districts]
        }

        with open('data.txt', 'w') as file:
            json.dump(city_data, file, indent=2)

        QtWidgets.QMessageBox.information(None, "City Added", f"{city_name} added successfully!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
