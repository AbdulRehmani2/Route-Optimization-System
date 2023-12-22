from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QMessageBox
from graph import Graph, createMap, distanceOnEarth, visualizeShortestPath
import json
import networkx as nx
import matplotlib.pyplot as plt
from hash import hashTable

class MyMainWindow(QtWidgets.QMainWindow, QtWidgets.QDialog):
    def __init__(self, path):
        super(MyMainWindow, self).__init__()
        uic.loadUi(path, self)
        
    def initPage1(self):
        self.SignUpButton.clicked.connect(self.__signUp)
        self.BackButton.clicked.connect(startPage2)
        self.passwordText.setEchoMode(QtWidgets.QLineEdit.Password)
        
    def __signUp(self):
        usernameText = self.usernameText.text()
        passwordText = self.passwordText.text()
        emailText = self.emailText.text()
        if self.__register(usernameText,emailText,passwordText):
            self.__writeToCsv(usernameText, passwordText, emailText)
            QMessageBox.warning(self, "Message", "Account created successfully!")
            self.clearText()
            startPage2()
        else:
            self.clearText()
            
    def clearText(self):
        self.emailText.clear()
        self.usernameText.clear()
        self.passwordText.clear()
            
    # def __writeToCsv(self, usernameText, passwordText, emailText):
    #     with open('users.csv', mode='a', newline='') as file:
    #         writer = csv.writer(file)
    #         encrypted_password = self.__encryption(passwordText, 3)
    #         encrypted_email = emailText
    #         role="User"
    #         writer.writerow([usernameText, encrypted_password, encrypted_email,role])
    
    def __writeToCsv(self, username, passwordText, emailText):
        hash.addElement(username, self.__encryption(passwordText, 3), emailText, "User")
        hash.storeTable()
        # hash.printTable()
            
    def __encryption(self, text, shift):
        encrypted_text = ""
        for char in text:
            shifted = ord(char) + (shift % 26)
            if char.isalpha():
                if char.islower():
                    if shifted > ord('z'):
                        shifted -= 26
                    elif shifted < ord('a'):
                        shifted += 26
                    encrypted_text += chr(shifted)
                elif char.isupper():
                    if shifted > ord('Z'):
                        shifted -= 26
                    elif shifted < ord('A'):
                        shifted += 26
                    encrypted_text += chr(shifted)
            elif char.isnumeric():
                if shifted > ord('9'):
                    shifted -= 10
                elif shifted < ord('0'):
                    shifted += 10
                encrypted_text += chr(shifted)
            else:
                encrypted_text += char
        return encrypted_text
    
    def __register(self,usernameText,emailText,passwordText):
        if not usernameText or not emailText or not passwordText:
            QMessageBox.warning(None, "Registration Error", "Please fill in all the required fields.")
            return False
        if not self.__isValid(emailText):
            QMessageBox.warning(None, "Registration Error", "Invalid email address. Please enter a valid email address.")
            return  False
        return True
    
    def __isValid(self, email):
            return '@' in email
        
    def initPage2(self):
        self.SignUpButton.clicked.connect(self.__signIn)
        self.BackButton.clicked.connect(startPage1)
        self.passwordText.setEchoMode(QtWidgets.QLineEdit.Password)
        
    def __signIn(self):
        usernameText = self.usernameText.text()
        passwordText = self.passwordText.text()
        print(usernameText, passwordText)
        login = self.__readCSV(usernameText, passwordText)
        if(login == None):
            self.usernameText.clear()
            self.passwordText.clear()
            QMessageBox.warning(None, "Invalid credentials", "Please try again.")
        else:
            authenticated, decrypted_email,role = True, login.key2, login.key3
            if authenticated:
                QMessageBox.warning(None, "Login successful!", f"Email: {decrypted_email}")
                self.usernameText.clear()
                self.passwordText.clear()
                if role == "Admin":
                    startAdminPage()
                else:
                    startPage3()
            # else:
            #     self.usernameText.clear()
            #     self.passwordText.clear()
            #     QMessageBox.warning(None, "Invalid credentials", "Please try again.")
            
    # def __readCSV(self, username, password):
    #     with open('users.csv', mode='r') as file:
    #         reader = csv.reader(file)
    #         for row in reader:
    #             if username == row[0]:
    #                 storedPassword = row[1]
    #                 if self.__encryption(password, 3) == storedPassword:
    #                     storedEmail = row[2] 
    #                     role=row[3]
    #                     return True, storedEmail,role
    #                 else:
    #                     return False, None, None
    #         return False, None, None
    
    def __readCSV(self, username, password):
        user = hash.searchElement(username)
        if user != None:
            if(self.__encryption(password, 3) == user.key):
                return user
        else:
            return None
            
    
    def initPage3(self):
        self.myGraph = Graph()
        file = open("./data.txt", "r")
        data = json.load(file)
        createMap(self.myGraph, data)
        for i in self.myGraph.vertices:
            self.sourceInput.addItem(i.value)
            self.destinationInput.addItem(i.value)
        self.ShowMap.clicked.connect(self.__visualizeGraph)
        self.ShortestButton.clicked.connect(self.__showPath)
        self.BackButton.clicked.connect(startPage2)
        
    def __visualizeGraph(self):
        G = nx.Graph()
        for node in self.myGraph.vertices:
            G.add_node(node.value, pos=(node.longitude, node.latitude))
            for neighbor in node.getNeighbor():
                G.add_edge(node.value, neighbor.value, label=f"{distanceOnEarth(node.latitude, node.longitude, neighbor.latitude, neighbor.longitude)}")
        
        pos = nx.get_node_attributes(G, 'pos')
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=1, node_color='skyblue', font_color='black', font_size=9, edge_color='blue')
        edgeLabels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edgeLabels, font_size=6)
        plt.title("Graph Visualization")
        plt.show()
        
    def __showPath(self):
        source = self.sourceInput.currentText()
        destination = self.destinationInput.currentText()
        source = searchNode(self.myGraph, source)
        destination = searchNode(self.myGraph, destination)
        mode = self.transportation.currentText()
        # print(source, destination, mode)
        visualizeShortestPath(self.myGraph, source, destination, mode)

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
        
    def remove_city(self):
        city_name = self.cityname.text().strip()

        with open('data.txt', 'r') as file:
            data = json.load(file)

        if city_name in data:
            for city, info in data.items():
                if city != city_name and city_name in info['adjacent_districts']:
                    info['adjacent_districts'].remove(city_name)

            del data[city_name]

            with open('data.txt', 'w') as file:
                json.dump(data, file, indent=2)
            
            print(f"{city_name} has been removed.")
        else:
            print(f"{city_name} does not exist in the data.")

        self.cityname.clear()
    
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


    def initPage4(self):
        self.load_data()
        self.addcitybtn.clicked.connect(startAddPage)
        self.removecitybtn.clicked.connect(startRemovePage)
        self.Reload.clicked.connect(self.load_data)
        self.sortbtn.clicked.connect(self.sort_table_by_city)
        self.add_userbtn.clicked.connect(startPage7)
        self.backbtn.clicked.connect(startPage2)
        self.tableWidget.setColumnWidth(0, 200)
        self.tableWidget.setRowHeight(0, 30)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)  
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

    def initPage5(self):
        self.addcity.clicked.connect(self.save_city_details)
        
    def initPage6(self):
        self.Removebtn.clicked.connect(self.remove_city)
        
    def initPage7(self):
        self.addUser.clicked.connect(self.__signUp)
        self.passwordText.setEchoMode(QtWidgets.QLineEdit.Password)


def visualizeShortestPath(graph, source, destination, mode):
    G = nx.Graph()
    G2 = nx.Graph()
    graph.dijkstra(source)
    path = secondPath(source, destination)
    nodes = NodeToObject(path)
    newGraph = Graph()
    distance = destination.count if source != destination else 0
    time = calculateTime(mode, distance) if distance != 0 else distance
    createMap(newGraph, nodes)
    for node in graph.vertices:
        G.add_node(node.value, pos=(node.longitude, node.latitude))
        for neighbor in node.getNeighbor():
            G.add_edge(node.value, neighbor.value, label=f"{distanceOnEarth(node.latitude, node.longitude, neighbor.latitude, neighbor.longitude)}")

    for node in newGraph.vertices:
        G2.add_node(node.value, pos=(node.longitude, node.latitude))
        for neighbor in node.getNeighbor():
            G2.add_edge(node.value, neighbor.value, label=f"{distanceOnEarth(node.latitude, node.longitude, neighbor.latitude, neighbor.longitude)}")

    pos = nx.get_node_attributes(G, 'pos')
    plt.text(20, 60, 'This is a text annotation', fontsize=12, color='red', ha='center', va='bottom')
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=1, node_color='skyblue', font_color='black', font_size=10, edge_color='blue')
    edgeLabels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edgeLabels, font_size=6)
    nx.draw(G2, pos, node_size=1, node_color='skyblue', font_color='black', font_size=10, edge_color='red')
    plt.title(f"Total Distance : {round(distance, 1)}Km \n Travelling on : {mode} \n Time Taken : {time}h")
    plt.show()
    
def calculateTime(mode, distance):
    speed = 0
    if(distance == 0):
        return
    print(mode)
    if mode == "Bicycle":
        speed = 20
    elif mode == "Car":
        speed = 50
    elif mode == "Foot":
        speed = 10
    return round((distance/speed), 1)

def secondPath(source, target):
    node = target
    path = []
    while(node != source):
        path.append(node)
        node = node.previous
    path.append(source)
    path.reverse()
    return path

def NodeToObject(path):
    nodes = {}
    for i in range(len(path)):
        neighbors = []
        if(i != len(path) - 1):
            neighbors = [path[i+1].value]
        # for j in path[i].neighbors:
        #     if(j in path):
        #         neighbors.append(j)
        node = {"coordinates":{"latitude" : path[i].latitude, "longitude" : path[i].longitude}, "adjacent_districts" : neighbors}
        nodes[path[i].value] = node
    return nodes
        
def searchNode(graph, value):
    for i in graph.vertices:
        if(i.value == value):
            return i
        
app = QtWidgets.QApplication([])
page1 = MyMainWindow("./SignUp.ui")
page2 = MyMainWindow("./SignIn.ui")
page3 = MyMainWindow("./Map.ui")
page4 = MyMainWindow("./Admin.ui")
page5 = MyMainWindow("./Addcity.ui")
page6 = MyMainWindow("./Removecity.ui")
page7 = MyMainWindow("./AddUser.ui")

def startPage1():
    page1.show()
    page2.hide()
    page3.hide()
    page4.hide()
    page5.hide()
    page6.hide()
    page7.hide()
    
def startPage2():
    page2.show()
    page1.hide()
    page3.hide()
    page4.hide()
    page5.hide()
    page6.hide()
    page7.hide()
    
def startPage3():
    page3.show()
    page2.hide()
    page1.hide()
    page4.hide()
    page5.hide()
    page6.hide()
    page7.hide()

def startAdminPage():
    page4.show()
    page2.hide()
    page1.hide()
    page3.hide()
    page5.hide()
    page6.hide()
    page7.hide()

def startAddPage():
    page5.show()
    page2.hide()
    page1.hide()
    page3.hide()
    page4.hide()
    page6.hide()
    page7.hide()
    
def startRemovePage():
    page6.show()
    page5.hide()
    page2.hide()
    page1.hide()
    page3.hide()
    page4.hide()
    page7.hide()

def startPage7():
    page7.show()
    page5.hide()
    page2.hide()
    page1.hide()
    page3.hide()
    page4.hide()
    page6.hide()
    
page1.initPage1()
page2.initPage2()
page3.initPage3()
page4.initPage4()
page5.initPage5()
page6.initPage6()
page7.initPage7()
hash = hashTable(500)
hash.loadTable()

if __name__ == "__main__":
    startPage1()
    app.exec_()