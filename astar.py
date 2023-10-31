import heapq

def astar(graph, start_vertex, goal_vertex):
    open_set = []
    heapq.heappush(open_set, (0, start_vertex))  # Priority queue of (f-score, vertex)
    
    g_scores = {start_vertex: 0}  # Dictionary to track actual cost from start_vertex
    previous = {}  # Dictionary to track previous vertex in the optimal path
    
    while open_set:
        _, current_vertex = heapq.heappop(open_set)        
        if current_vertex == goal_vertex:
            # Reconstruct path from goal to start
            path = [current_vertex]
            while current_vertex in previous:
                current_vertex = previous[current_vertex]
                path.append(current_vertex)
            path.reverse()
            final_cost = g_scores[goal_vertex]
            return path, final_cost
        
        for neighbor in graph.vertices[current_vertex]:
            edge_weight = graph.vertices[current_vertex][neighbor]
            tentative_g_score = g_scores[current_vertex] + edge_weight

            if neighbor not in g_scores or tentative_g_score < g_scores[neighbor]:
                g_scores[neighbor] = tentative_g_score
                f_score = tentative_g_score + graph.heuristic_cost_estimate(neighbor, goal_vertex,2)
                heapq.heappush(open_set, (f_score, neighbor))
                previous[neighbor] = current_vertex

    return None, float('inf')  # No path found, return infinite cost