class GraphColoring:
    def __init__(self, graph, colors):
        self.graph = graph
        self.colors = colors
        self.num_vertices = len(graph)
        self.best_solution = None
        self.min_conflicts = float('inf')

    def solve(self):
        initial_solution = [-1] * self.num_vertices
        self._branch_and_bound(initial_solution, 0)
        return self.best_solution

    def _branch_and_bound(self, solution, vertex):
        if vertex == self.num_vertices:
            # Found a valid coloring
            conflicts = self._count_conflicts(solution)
            if conflicts == 0:
                self.best_solution = solution.copy()
            return

        for color in self.colors:
            solution[vertex] = color

            # Check if assigning this color creates conflicts
            if not self._has_conflicts(solution, vertex):
                self._branch_and_bound(solution, vertex + 1)

            solution[vertex] = -1

    def _count_conflicts(self, solution):
        conflicts = 0
        for vertex in range(self.num_vertices):
            for neighbor in self.graph[vertex]:
                if solution[vertex] == solution[neighbor]:
                    conflicts += 1
        return conflicts

    def _has_conflicts(self, solution, vertex):
        for neighbor in self.graph[vertex]:
            if solution[vertex] == solution[neighbor]:
                return True
        return False


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
    
   
