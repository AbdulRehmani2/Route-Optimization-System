# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, uic
import json
from Addcity2 import AddCity
from Removecity import RemoveCityWindow
from AddUser import addUser

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1117, 824)
        Dialog.setStyleSheet("background-color: #cccccc;\n"
"")
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
        self.Reload = QtWidgets.QPushButton(self.frame)
        self.Reload.setGeometry(QtCore.QRect(1000, 90, 111, 31))
        self.Reload.setStyleSheet("padding: 5px;\n"
"background-color: #0A1172;\n"
"color: white;")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("reloadIcon-removebg-preview.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Reload.setIcon(icon)
        self.Reload.setObjectName("Reload")
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(0, 130, 271, 691))
        self.frame_2.setStyleSheet("background-color: #0A1172;\n"
"")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.addcitybtn = QtWidgets.QPushButton(self.frame_2)
        self.addcitybtn.setGeometry(QtCore.QRect(40, 260, 201, 51))
        self.addcitybtn.setStyleSheet("padding: 5px;\n"
"background-color: #0A1172;\n"
"color: white;")
        self.addcitybtn.setObjectName("addcitybtn")
        self.removecitybtn = QtWidgets.QPushButton(self.frame_2)
        self.removecitybtn.setGeometry(QtCore.QRect(40, 360, 201, 51))
        self.removecitybtn.setStyleSheet("padding: 5px;\n"
"background-color: #0A1172;\n"
"color: white;")
        self.removecitybtn.setObjectName("removecitybtn")
        self.add_userbtn = QtWidgets.QPushButton(self.frame_2)
        self.add_userbtn.setGeometry(QtCore.QRect(40, 160, 201, 51))
        self.add_userbtn.setStyleSheet("padding: 5px;\n"
"background-color: #0A1172;\n"
"color: white;")
        self.add_userbtn.setObjectName("add_userbtn")
        self.sortbtn = QtWidgets.QPushButton(self.frame_2)
        self.sortbtn.setGeometry(QtCore.QRect(150, 650, 111, 31))
        self.sortbtn.setStyleSheet("padding: 5px;\n"
"background-color: #0A1172;\n"
"color: white;")
        self.sortbtn.setObjectName("sortbtn")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(265, 131, 851, 691))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)

        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setRowHeight(0, 30)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)  
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

  
        self.load_data()  # Call function to load data when UI is set up
        self.addcitybtn.clicked.connect(self.loadAddCity)
        self.removecitybtn.clicked.connect(self.loadRemoveCity)
        self.add_userbtn.clicked.connect(self.loadAddUser)
        self.add_city_dialog = None 
        self.removeDialog = None
        self.add_user_dialog=None
        self.Reload.clicked.connect(self.reload_data)
        self.sortbtn.clicked.connect(self.sort_table_by_city)

    def retranslateUi(self, Dialog):
        # ... (your existing retranslateUi function)
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "Route Optimization and Management System"))
        self.Reload.setText(_translate("Dialog", "Reload"))
        self.addcitybtn.setText(_translate("Dialog", "Add City"))
        self.removecitybtn.setText(_translate("Dialog", "Remove City"))
        self.add_userbtn.setText(_translate("Dialog", "Add User"))
        self.sortbtn.setText(_translate("Dialog", "Sort"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "City Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Latitude"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Longitude"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Adjacent Cities"))

    def loadAddCity(self):
        if self.add_city_dialog is None:
            self.add_city_dialog = QtWidgets.QDialog()
            self.add_city_ui = AddCity()
            self.add_city_ui.setupUi(self.add_city_dialog)
        self.add_city_dialog.show()

    def loadRemoveCity(self):
        if self.removeDialog is None:
            self.removeDialog = QtWidgets.QDialog()
            self.removeUi = RemoveCityWindow()
            self.removeUi.setupUi(self.removeDialog)
        self.removeDialog.show()
    
    def loadAddUser(self):
        if self.add_user_dialog is None:
            self.add_user_dialog = QtWidgets.QDialog()
            self.addUserUi = addUser()
            self.addUserUi.setupUi(self.add_user_dialog)
        self.add_user_dialog.show()

    def reload_data(self):
        self.load_data()

    def load_data(self):
        with open('data.txt', 'r') as file:
            data = json.loads(file.read())

        row_count = len(data)
        self.tableWidget.setRowCount(row_count)

        for idx, (city, info) in enumerate(data.items()):
            self.tableWidget.setItem(idx, 0, QtWidgets.QTableWidgetItem(city))
            self.tableWidget.setItem(idx, 1, QtWidgets.QTableWidgetItem(str(info['coordinates']['latitude'])))
            self.tableWidget.setItem(idx, 2, QtWidgets.QTableWidgetItem(str(info['coordinates']['longitude'])))

            adj_districts = ', '.join(info['adjacent_districts'])
            self.tableWidget.setItem(idx, 3, QtWidgets.QTableWidgetItem(adj_districts))

    def merge_sort(self, data):
        if len(data) <= 1:
            return data

        middle = len(data) // 2
        left_half = data[:middle]
        right_half = data[middle:]

        left_half = self.merge_sort(left_half)
        right_half = self.merge_sort(right_half)

        return self.merge(left_half, right_half)

    def merge(self, left, right):
        result = []
        left_idx = right_idx = 0

        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx][0] < right[right_idx][0]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1

        result.extend(left[left_idx:])
        result.extend(right[right_idx:])

        return result

    def sort_table_by_city(self):
        data = []
        for row in range(self.tableWidget.rowCount()):
            city_name = self.tableWidget.item(row, 0).text()
            latitude = float(self.tableWidget.item(row, 1).text())
            longitude = float(self.tableWidget.item(row, 2).text())
            adjacent_cities = self.tableWidget.item(row, 3).text()

            data.append((city_name, latitude, longitude, adjacent_cities))

        sorted_data = self.merge_sort(data)

        for row, city_data in enumerate(sorted_data):
            city_name, latitude, longitude, adjacent_cities = city_data
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(city_name))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(latitude)))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(longitude)))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(adjacent_cities))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
