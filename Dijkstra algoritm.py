import heapq

def dijkstra(graph, start):
    """
    Implements Dijkstra's algorithm to find the shortest path from start node to all other nodes in the graph.
    
    :param graph: Dictionary representing the adjacency list of the graph. 
                 { node: {neighbor1: weight1, neighbor2: weight2, ...}, ... }
    :param start: The starting node
    :return: Dictionary of shortest distances from start to each node
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If this path is not better, skip
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance <= distances[neighbor]:
                #distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

if __name__ == "__main__":
    # Example usage
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    start_node = 'A'
    distances = dijkstra(graph, start_node)
    print("Shortest distances from node", start_node)
    for node in distances:
        print(f"Distance to {node}: {distances[node]}")