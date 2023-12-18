from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QMessageBox
from graph import Graph, createMap, distanceOnEarth, visualizeShortestPath
from AddUser import addUser
import json
import networkx as nx
import matplotlib.pyplot as plt
import csv

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
            
    def __writeToCsv(self, usernameText, passwordText, emailText):
        with open('users.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            encrypted_password = self.__encryption(passwordText, 3)
            encrypted_email = self.__encryption(emailText, 3) 
            role="User"
            writer.writerow([usernameText, encrypted_password, encrypted_email,role])
            
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
        authenticated, decrypted_email,role = self.__readCSV(usernameText, passwordText)
        if authenticated:
            QMessageBox.warning(None, "Login successful!", f"Email: {decrypted_email}")
            self.usernameText.clear()
            self.passwordText.clear()
            if role == "Admin":
                startAdminPage()
            else:
                startPage3()
        else:
            self.usernameText.clear()
            self.passwordText.clear()
            QMessageBox.warning(None, "Invalid credentials", "Please try again.")
            
    def __readCSV(self, username, password):
        with open('users.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if username == row[0]:
                    decrypted_password = self.__decryption(row[1], 3)
                    if password == decrypted_password:
                        decrypted_email = self.__decryption(row[2], 3) 
                        role=row[3]
                        return True, decrypted_email,role
                    else:
                        return False, None, None
            return False, None, None
    
    def __decryption(self, text, shift):
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
        print(source, destination)
        visualizeShortestPath(self.myGraph, source, destination)

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
    
    def initPage4(self):
        self.load_data()
        self.addcitybtn.clicked.connect(startAddPage)
        self.removecitybtn.clicked.connect(startRemovePage)
        self.Reload.clicked.connect(self.load_data)
        self.add_userbtn.clicked.connect(startPage7)
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


def visualizeShortestPath(graph, source, destination):
    G = nx.Graph()
    G2 = nx.Graph()
    graph.dijkstra(source)
    path = secondPath(source, destination)
    nodes = NodeToObject(path)
    newGraph = Graph()
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
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=1, node_color='skyblue', font_color='black', font_size=10, edge_color='blue')
    edgeLabels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edgeLabels, font_size=6)
    nx.draw(G2, pos, node_size=1, node_color='skyblue', font_color='black', font_size=10, edge_color='red')
    plt.title("Graph Visualization")
    plt.show()
    
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
    page1.initPage1()
    
def startPage2():
    page2.show()
    page1.hide()
    page3.hide()
    page2.initPage2()
    
def startPage3():
    page3.show()
    page2.hide()
    page1.hide()
    page3.initPage3()

def startAdminPage():
    page4.show()
    page2.hide()
    page1.hide()
    page4.initPage4()

def startAddPage():
    page5.show()
    page5.initPage5()
    
def startRemovePage():
    page6.show()
    page6.initPage6()

def startPage7():
    page7.show()
    page7.initPage7()

if __name__ == "__main__":
    startPage2()
    app.exec_()