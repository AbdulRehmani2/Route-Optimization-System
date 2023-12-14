import json
import networkx as nx
import heapq
import matplotlib.pyplot as plt


class Node:
    def __init__(self, value, latitude, longitude):
        self.value = value
        self.neighbors = []
        self.latitude = latitude
        self.longitude = longitude
        self.status = "unvisited"

    def __lt__(self, other):
        return self.value < other.value

    def hasNeighbor(self):
        return not self.neighbors == []

    def getNeighbors(self):
        return self.neighbors

    def addNeighbor(self, vertex, distance, travel_time, cost):
        self.neighbors.append((vertex, distance, travel_time, cost))


class Graph:
    def __init__(self):
        self.vertices = []

    def addVertex(self, vertex):
        self.vertices.append(vertex)

    def addEdge(self, u, v, distance, travel_time, cost):
        u.addNeighbor(v, distance, travel_time, cost)
        v.addNeighbor(u, distance, travel_time, cost)
        
    def printVertices(self):
        for i in self.vertices:
            print(i.value, i.latitude, i.longitude)
            for j, dist, time, cost in i.getNeighbors():
                print(f"  -> {j.value}  Distance: {dist}  Time: {time}  Cost: {cost}")

    def dijkstra(self, start, end):
        distances = {vertex: float('infinity') for vertex in self.vertices}
        predecessors = {vertex: None for vertex in self.vertices}
        distances[start] = 0
        priority_queue = [(0, start)]
        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, distance, _, _ in current_vertex.getNeighbors():
                new_distance = distances[current_vertex] + distance
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = current_vertex
                    heapq.heappush(priority_queue, (new_distance, neighbor))

        # Reconstruct the path
        path = []
        current = end
        while current is not None:
            path.insert(0, current)
            current = predecessors[current]

        return path, distances[end]

def createMap(graph, data):
    city_list = []
    for city_name, city_data in data.items():
        city = Node(city_name, city_data["coordinates"]["latitude"], city_data["coordinates"]["longitude"])
        graph.addVertex(city)
        city_list.append(city_name)
    for city in graph.vertices:
        print(f"City: {city.value}, Latitude: {city.latitude}, Longitude: {city.longitude}")
        for adjacent_city, details in data[city.value]["adjacent_districts"].items():
            index = next((i for i, city in enumerate(city_list) if city.lower() == adjacent_city.lower()), None)
            if index is not None and index < len(graph.vertices):
                graph.addEdge(city, graph.vertices[index], details["distance"], details["travel_time"], details["cost"])
            else:
                print(f"Warning: {adjacent_city} not found in city_list.")
    return graph



def visualize_graph(graph, shortest_path=None):
    G = nx.Graph()

    for vertex in graph.vertices:
        city = vertex.value
        G.add_node(city, pos=(vertex.longitude, vertex.latitude))

        for neighbor, distance, _, _ in vertex.getNeighbors():
            G.add_edge(city, neighbor.value, weight=distance)

    edge_colors = ['black' for _ in G.edges()]

    if shortest_path:
        for i in range(len(shortest_path) - 1):
            edge1 = shortest_path[i].value
            edge2 = shortest_path[i + 1].value
            edge_index = list(G.edges).index((edge1, edge2)) if (edge1, edge2) in list(G.edges) else list(G.edges).index((edge2, edge1))
            edge_colors[edge_index] = 'red'

    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=8, font_color='black', font_weight='bold', edge_color=edge_colors)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()



def get_user_input():
    start_city = input("Enter the start city: ").strip()
    target_city = input("Enter the target city: ").strip()
    print(f"Start city: {start_city}, Target city: {target_city}")
    return start_city, target_city

try:
    with open('updata.txt', 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print("Error: 'updata.txt' file not found.")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON in 'updata.txt': {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

myGraph = Graph()
myGraph = createMap(myGraph, data)

# visualize_graph(myGraph)

start_city_name, target_city_name = get_user_input()

start_city = next((node for node in myGraph.vertices if node.value.lower() == start_city_name.lower()), None)
target_city = next((node for node in myGraph.vertices if node.value.lower() == target_city_name.lower()), None)

if start_city and target_city:
    shortest_path, shortest_distance = myGraph.dijkstra(start_city, target_city)
    print(f"Shortest Path from {start_city_name} to {target_city_name}: {shortest_path}")
    print(f"Shortest Distance: {shortest_distance} units")
    visualize_graph(myGraph, shortest_path)
else:
    print("Start or target city not found in the graph.")
    

