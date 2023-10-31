import graph as gr
import astar

# Create a new graph
graph, start_vertex, goal_vertex = gr.build_graph_from_grid_map("instances/gridmap2.txt")

# Print the graph
print(graph)

# Apply A* algorithm
path, final_cost = astar.astar(graph, start_vertex, goal_vertex)

if path:
    print("Path found:", " -> ".join(path))
    print("Final cost:", final_cost)
else:
    print("No path found")