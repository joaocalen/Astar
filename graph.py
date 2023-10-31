import math

class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}
    
    def add_edge(self, start_vertex, end_vertex, weight):
        self.vertices[start_vertex][end_vertex] = weight
        self.vertices[end_vertex][start_vertex] = weight

    def get_coordinates(self, vertex):
        if vertex in self.vertices:
            return map(int, vertex.split('-'))  # Return the x and y coordinates for the given vertex
    
    def heuristic_cost_estimate(self, current_vertex, goal_vertex, heuristic):
        current_x, current_y = self.get_coordinates(current_vertex)
        goal_x, goal_y = self.get_coordinates(goal_vertex)
        if heuristic == 1:
            return math.sqrt((current_x - goal_x)**2 + (current_y - goal_y)**2)
        else:
            return abs(current_x - goal_x) + abs(current_y - goal_y)  # Manhattan distance
    
    def __str__(self):
        result = "Graph:\n"
        for vertex, edges in self.vertices.items():
            result += f"Vertex: {vertex}\n"
            for neighbor, weight in edges.items():
                result += f"  -> {neighbor} (Weight: {weight})\n"
        return result

def build_graph_from_grid_map(map_file):
    graph = Graph()
    grid_map = []
    
    with open(map_file, 'r') as file:
        for line in file:
            line = line.strip()
            grid_map.append(list(line))

    num_rows = len(grid_map)
    num_cols = len(grid_map[0])
    start_node = "0-0"
    goal_node = "0-0"

    for i in range(num_rows):
        for j in range(num_cols):
            cell = grid_map[i][j]            
            if cell != '#':  # Consider '#' as an obstacle or wall
                vertex = f"{i}-{j}"
                graph.add_vertex(vertex)
                if cell == 'S':
                    start_node = vertex
                elif cell == 'G':
                    goal_node = vertex
                # Check neighboring cells (up, down, left, right)
                
                if i > 0 and grid_map[i - 1][j] != '#':
                    
                    neighbor = f"{i - 1}-{j}"
                    if neighbor not in graph.vertices:
                        graph.add_vertex(neighbor)
                    graph.add_edge(vertex, neighbor, graph.heuristic_cost_estimate(vertex,neighbor,1))
                if i < num_rows - 1 and grid_map[i + 1][j] != '#':
                    neighbor = f"{i + 1}-{j}"
                    if neighbor not in graph.vertices:
                        graph.add_vertex(neighbor)
                    graph.add_edge(vertex, neighbor, graph.heuristic_cost_estimate(vertex,neighbor,1))
                if j > 0 and grid_map[i][j - 1] != '#':
                    neighbor = f"{i}-{j - 1}"
                    if neighbor not in graph.vertices:
                        graph.add_vertex(neighbor)
                    graph.add_edge(vertex, neighbor, graph.heuristic_cost_estimate(vertex,neighbor,1))
                if j < num_cols - 1 and grid_map[i][j + 1] != '#':
                    neighbor = f"{i}-{j + 1}"
                    if neighbor not in graph.vertices:
                        graph.add_vertex(neighbor)
                    graph.add_edge(vertex, neighbor, graph.heuristic_cost_estimate(vertex,neighbor,1))
                if i > 0 and j > 0 and grid_map[i - 1][j - 1] != '#':
                    neighbor = f"{i - 1}-{j - 1}"
                    if neighbor not in graph.vertices:
                        graph.add_vertex(neighbor)
                    graph.add_edge(vertex, neighbor, graph.heuristic_cost_estimate(vertex,neighbor,1))
                if i > 0 and j < num_cols - 1 and grid_map[i - 1][j + 1] != '#':
                    neighbor = f"{i - 1}-{j + 1}"
                    if neighbor not in graph.vertices:
                        graph.add_vertex(neighbor)
                    graph.add_edge(vertex, neighbor, graph.heuristic_cost_estimate(vertex,neighbor,1))
                if i < num_rows - 1 and j > 0 and grid_map[i + 1][j - 1] != '#':
                    neighbor = f"{i + 1}-{j - 1}"
                    if neighbor not in graph.vertices:
                        graph.add_vertex(neighbor)
                    graph.add_edge(vertex, neighbor, graph.heuristic_cost_estimate(vertex,neighbor,1))
                if i < num_rows - 1 and j < num_cols - 1 and grid_map[i + 1][j + 1] != '#':
                    neighbor = f"{i + 1}-{j + 1}"
                    if neighbor not in graph.vertices:
                        graph.add_vertex(neighbor)
                    graph.add_edge(vertex, neighbor, graph.heuristic_cost_estimate(vertex,neighbor,1))

    return graph, start_node, goal_node