class Graph:
    def __init__(self):
        self.vertices = {}  # Dictionary to store the vertices and their information
    
    def add_vertex(self, vertex, x, y):
        self.vertices[vertex] = {'x': x, 'y': y, 'connections': {}}  # Initialize a dictionary to store the connections and their weights
    
    def add_edge(self, start_vertex, end_vertex, weight):
        if start_vertex in self.vertices and end_vertex in self.vertices:
            self.vertices[start_vertex]['connections'][end_vertex] = weight  # Add the weighted edge from start_vertex to end_vertex
            self.vertices[end_vertex]['connections'][start_vertex] = weight  # Add the weighted edge from end_vertex to start_vertex
    
    def get_weight(self, start_vertex, end_vertex):
        if start_vertex in self.vertices and end_vertex in self.vertices:
            return self.vertices[start_vertex]['connections'].get(end_vertex, float('inf'))  # Return the weight if the edge exists, otherwise return infinity
        else:
            return float('inf')
    
    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return list(self.vertices[vertex]['connections'].keys())  # Return the neighboring vertices
        else:
            return []
    
    def get_coordinates(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]['x'], self.vertices[vertex]['y']  # Return the x and y coordinates for the given vertex
    
    def __str__(self):
        graph_str = ""
        for vertex, data in self.vertices.items():
            neighbors = data['connections']
            neighbors_str = ", ".join([f"{neighbor} ({weight})" for neighbor, weight in neighbors.items()])
            graph_str += f"{vertex} ({data['x']}, {data['y']}): {neighbors_str}\n"
        return graph_str