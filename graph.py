import math, heapq
import queue as q
import networkx as nx
from matplotlib import pyplot as plt

class Node:
    
    def __init__(self, value, latitude, longitude):
        self.value = value
        self.neighbors = []
        self.latitude = latitude
        self.longitude = longitude
        self.status = "unvisited"
        self.count = float("infinity")
        self.previous = None
        
    def hasNeighbor(self):
        return self.neighbors == []
    
    def getNeighbor(self):
        return self.neighbors

    def addNeighbor(self, vertex):
        self.neighbor.append(vertex)        
        
class Graph:
    def __init__(self):
        self.vertices = []
        
    def addVertex(self, vertex):
        self.vertices.append(vertex)
        
    def addEdge(self, u, v):
        u.neighbors.append(v)
        v.neighbors.append(u)
        
    def printVertices(self):
        for i in self.vertices:
            print(i.value, i.latitude, i.longitude)
            for j in i.neighbors:
                print(j.value)
                
    def BFS(self, node):
        node.status = "visited"
        Q = q.Queue()
        Q.put(node)
        while(not Q.empty()):
            element = Q.get()
            print(element.value)
            for i in element.neighbors:
                if(i.status == "unvisited"):
                    i.status = "visited"
                    Q.put(i)
                    
    def DFS(self, node):
        node.status = "visited"
        stack = []
        stack.append(node)
        while(len(stack) != 0):
            element = stack.pop()
            print(element.value)
            for i in element.neighbors:
                if(i.status == "unvisited"):
                    i.status = "visited"
                    stack.append(i)
                    
    def adjacencyMatrix(self):
        matrix = []
        for i in self.vertices:
            row = []
            for j in self.vertices:
                if(j in i.neighbors):
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        return matrix
    
    def dijkstra(self, node):
        for i in self.vertices:
            i.previous = None
            i.count = float("infinity")
        nodeList = [(0, node)]
        while(len(nodeList) != 0):
            element = heapq.heappop(nodeList)
            if(element[0] > element[1].count):
                continue
            for i in element[1].neighbors:
                distance = element[0] + distanceOnEarth(element[1].latitude, element[1].longitude, i.latitude, i.longitude)
                if(distance < i.count):
                    i.count = distance
                    i.previous = element[1]
                    heapq.heappush(nodeList, (distance, i))
            
def createMap(graph, data):
    list = []
    for i in data:
        district = Node(i, data[i]["coordinates"]["latitude"], data[i]["coordinates"]["longitude"])
        graph.addVertex(district)
        list.append(district.value)
    for i in graph.vertices:
        for j in data[i.value]["adjacent_districts"]:
            index = list.index(j)
            graph.addEdge(i, graph.vertices[index])
    return graph
        
    
def calculateDistance(lat1, lon1, lat2, lon2):
        lat1 = pow(abs(lat1-lat2), 2)
        lon1 = pow(abs(lon1-lon2), 2)
        return math.sqrt(lon1 + lat1)
    
def distanceOnEarth(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    a = pow(math.sin(abs(lat1 - lat2)/2), 2)
    b = math.cos(lat1)
    c = math.cos(lat2)
    d = pow(math.sin(abs(lon1 - lon2)/2), 2)
    e = math.sqrt(a + b * c * d)
    e = math.asin(e)
    return round(e * 2 * R, 1)

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
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=1, node_color='skyblue', font_color='black', font_size=6, edge_color='blue')
    edgeLabels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edgeLabels, font_size=6)
    nx.draw(G2, pos, node_size=1, node_color='skyblue', font_color='black', font_size=6, edge_color='red')
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
# file = open("./data.txt", "r")
# data = json.load(file)
        
# for i in data:
#     print(i["coordinates"]["latitude"])
    
# myGraph = Graph()
# myGraph = createMap(myGraph, data)
# myGraph.visualizeGraph()
# myGraph.printVertices()
# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)

# myGraph.addVertex(node1)
# myGraph.addVertex(node2)
# myGraph.addVertex(node3)
# myGraph.addVertex(node4)
# myGraph.addVertex(node5)

# myGraph.addEdge(node1, node2)
# myGraph.addEdge(node2, node3)
# myGraph.addEdge(node3, node4)
# myGraph.addEdge(node4, node5)
# myGraph.addEdge(node5, node1)
