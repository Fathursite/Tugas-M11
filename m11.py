import heapq

def tugasGraph(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

graph = {
    'A': {'B': 1, 'D': 3},
    'B': {'A': 1, 'C': 1, 'D': 4},
    'C': {'B': 1, 'D': 1},
    'D': {'A': 3, 'B': 4, 'C': 1}
}

start_node = 'A'
shortest_distances = tugasGraph(graph, start_node)

print(f"Shortest distances from {start_node}: {shortest_distances}")
