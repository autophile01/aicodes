class UnionFind:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root1] = root2
                self.rank[root2] += 1


def kruskal_minimum_spanning_tree(graph):
    minimum_spanning_tree = []
    vertices = set()
    for edge in graph:
        vertices.add(edge[0])
        vertices.add(edge[1])
    union_find = UnionFind(vertices)
    graph.sort(key=lambda x: x[2])  # Sort edges by weights
    for edge in graph:
        vertex1, vertex2, weight = edge
        if union_find.find(vertex1) != union_find.find(vertex2):
            union_find.union(vertex1, vertex2)
            minimum_spanning_tree.append(edge)
    return minimum_spanning_tree

graph = [('A', 'B', 10), ('A', 'C', 6), ('B', 'C', 5), ('B', 'D', 15), ('C', 'D', 4)]
minimum_spanning_tree = kruskal_minimum_spanning_tree(graph)
print(minimum_spanning_tree)