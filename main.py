import graph as gr

# Create a new graph
graph = gr.Graph()

# Add vertices with coordinates
graph.add_vertex("A", 0, 0)
graph.add_vertex("B", 1, 2)
graph.add_vertex("C", 3, 1)
graph.add_vertex("D", 2, 3)

# Add weighted edges
graph.add_edge("A", "B", 2)
graph.add_edge("B", "C", 3)
graph.add_edge("C", "D", 1)
graph.add_edge("D", "A", 4)

# Get weight of an edge
print(graph.get_weight("A", "B"))  # Output: 2

# Get neighbors of a vertex
print(graph.get_neighbors("A"))  # Output: ['B', 'D']

# Get coordinates of a vertex
print(graph.get_coordinates("B"))  # Output: (1, 2)

# Print the graph
print(graph)