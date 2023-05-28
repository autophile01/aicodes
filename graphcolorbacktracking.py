class GraphColoring:
    def __init__(self, graph, colors):
        self.graph = graph
        self.colors = colors
        self.num_vertices = len(graph)
        self.solution = [-1] * self.num_vertices
        self.best_solution = None
        self.min_conflicts = float('inf')

    def solve(self):
        self._backtrack(0)
        return self.best_solution

    def _backtrack(self, vertex):
        if vertex == self.num_vertices:
            # Found a valid coloring
            conflicts = self._count_conflicts()
            if conflicts < self.min_conflicts:
                self.min_conflicts = conflicts
                self.best_solution = self.solution.copy()
            return

        for color in self.colors:
            if self._is_safe(vertex, color):
                self.solution[vertex] = color
                self._backtrack(vertex + 1)
                self.solution[vertex] = -1

    def _is_safe(self, vertex, color):
        for neighbor in self.graph[vertex]:
            if self.solution[neighbor] == color:
                return False
        return True

    def _count_conflicts(self):
        conflicts = 0
        for vertex in range(self.num_vertices):
            for neighbor in self.graph[vertex]:
                if self.solution[vertex] == self.solution[neighbor]:
                    conflicts += 1
        return conflicts


# Example usage
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2],
}

colors = [0, 1, 2]  # Assign integer indices to colors

graph_coloring = GraphColoring(graph, colors)
solution = graph_coloring.solve()

print("Vertex Coloring:")
for vertex, color_index in enumerate(solution):
    print(f"Vertex {vertex}: {colors[color_index]}")
