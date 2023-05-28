import heapq

def dijkstra_minimum_spanning_tree(graph, source):
    distances = {vertex: float('inf') for vertex in graph}
    distances[source] = 0
    queue = [(0, source)]
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

graph = {
    'A': [('B', 5), ('C', 2)],
    'B': [('A', 5), ('C', 1)],
    'C': [('A', 2), ('B', 1), ('D', 4)],
    'D': [('C', 4)]
}
source = 'A'
distances = dijkstra_minimum_spanning_tree(graph, source)
print(distances)