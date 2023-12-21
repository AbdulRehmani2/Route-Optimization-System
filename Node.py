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