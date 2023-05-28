def prim_minimum_spanning_tree(graph):
    minimum_spanning_tree = []
    visited = set()
    # Start with any vertex
    start_vertex = list(graph.keys())[0]
    visited.add(start_vertex)
    while len(visited) < len(graph):
        min_weight = float('inf')
        min_edge = None
        for vertex in visited:
            for neighbor, weight in graph[vertex]:
                if neighbor not in visited and weight < min_weight:
                    min_weight = weight
                    min_edge = (vertex, neighbor)
        minimum_spanning_tree.append(min_edge)
        visited.add(min_edge[1])
    return minimum_spanning_tree

graph = {
    'A': [('B', 10), ('C', 6)],
    'B': [('A', 10), ('C', 5), ('D', 15)],
    'C': [('A', 6), ('B', 5), ('D', 4)],
    'D': [('B', 15), ('C', 4)]
}
minimum_spanning_tree = prim_minimum_spanning_tree(graph)
print(minimum_spanning_tree)