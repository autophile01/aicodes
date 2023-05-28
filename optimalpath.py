from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = {}
        self.graph[u][v] = weight

    def heuristic(self, node, goal):
        # Implement your heuristic function here
        # This function should estimate the cost from 'node' to 'goal'
        # It should return a numerical value
        pass

    def astar(self, start, goal):
        visited = set()
        queue = PriorityQueue()
        queue.put((0, start))  # Priority queue stores (f_score, node) tuples
        g_scores = {node: float('inf') for node in self.graph}
        g_scores[start] = 0
        f_scores = {node: float('inf') for node in self.graph}
        f_scores[start] = self.heuristic(start, goal)
        parent_map = {}  # Dictionary to store the parent nodes

        while not queue.empty():
            _, current_node = queue.get()

            if current_node == goal:
                # Goal reached, return the path
                return self.reconstruct_path(start, goal, parent_map)

            visited.add(current_node)

            for neighbor, weight in self.graph[current_node].items():
                if neighbor in visited:
                    continue

                tentative_g_score = g_scores[current_node] + weight

                if tentative_g_score < g_scores[neighbor]:
                    g_scores[neighbor] = tentative_g_score
                    f_scores[neighbor] = tentative_g_score + self.heuristic(neighbor, goal)
                    queue.put((f_scores[neighbor], neighbor))
                    parent_map[neighbor] = current_node

        # No path found
        return None

    def reconstruct_path(self, start, goal, parent_map):
        path = [goal]
        current_node = goal

        while current_node != start:
            current_node = parent_map[current_node]
            path.append(current_node)

        path.reverse()
        return path


# Create a sample graph
graph = Graph()
graph.add_edge('A', 'B', 5)
graph.add_edge('A', 'C', 3)
graph.add_edge('B', 'D', 2)
graph.add_edge('C', 'D', 8)
graph.add_edge('C', 'E', 1)
graph.add_edge('D', 'E', 4)
graph.add_edge('D', 'F', 3)
graph.add_edge('E', 'F', 2)

# Define the heuristic function (Manhattan distance in this example)
def heuristic(node, goal):
    h_values = {
        'A': 6,
        'B': 4,
        'C': 3,
        'D': 1,
        'E': 2,
        'F': 0
    }
    return h_values[node]

# Set the heuristic function in the graph
graph.heuristic = heuristic

# Perform A* search
start_node = 'A'
goal_node = 'E'

# Check if the start and goal nodes are present in the graph
if start_node in graph.graph and goal_node in graph.graph:
    path = graph.astar(start_node, goal_node)

    # Print the optimal path
    if path:
        print("Optimal path:", ' -> '.join(path))
    else:
        print("No path found")
else:
    print("Start or goal node not present in the graph")