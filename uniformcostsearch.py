import heapq

class Node:
    def __init__(self, state, cost, parent=None):
        self.state = state
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

def uniform_cost_search(start_state, goal_state, graph):
    visited = set()
    frontier = []
    heapq.heappush(frontier, Node(start_state, 0))

    while frontier:
        current_node = heapq.heappop(frontier)
        current_state = current_node.state

        if current_state == goal_state:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return list(reversed(path))

        visited.add(current_state)

        neighbors = graph[current_state]
        for neighbor in neighbors:
            neighbor_state, step_cost = neighbor
            total_cost = current_node.cost + step_cost

            if neighbor_state not in visited:
                heapq.heappush(frontier, Node(neighbor_state, total_cost, current_node))
            else:
                for node in frontier:
                    if node.state == neighbor_state and total_cost < node.cost:
                        frontier.remove(node)
                        heapq.heappush(frontier, Node(neighbor_state, total_cost, current_node))
                        break

    return None

# Example usage
graph = {
    'A': [('B', 5), ('C', 1)],
    'B': [('D', 2), ('E', 4)],
    'C': [('F', 3)],
    'D': [('G', 6)],
    'E': [('H', 3)],
    'F': [('I', 2)],
    'G': [],
    'H': [],
    'I': []
}

start_state = 'A'
goal_state = 'I'

path = uniform_cost_search(start_state, goal_state, graph)
print(path)
