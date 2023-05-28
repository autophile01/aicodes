from queue import PriorityQueue

class PuzzleNode:
    def __init__(self, state, parent=None, move=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        # Define comparison for priority queue based on f-score (cost + heuristic)
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def is_goal(self, goal_state):
        return self.state == goal_state


class EightPuzzleSolver:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.moves = {
            0: ('UP', -3),
            1: ('DOWN', 3),
            2: ('LEFT', -1),
            3: ('RIGHT', 1)
        }

    def solve(self):
        start_node = PuzzleNode(tuple(self.initial_state))
        queue = PriorityQueue()
        queue.put(start_node)
        visited = set()

        while not queue.empty():
            current_node = queue.get()

            if current_node.is_goal(tuple(self.goal_state)):
                # Goal state reached, reconstruct and return the path
                return self.reconstruct_path(current_node)

            visited.add(tuple(current_node.state))

            # Generate next possible moves
            empty_tile_index = current_node.state.index(0)
            for move, delta in self.moves.items():
                new_index = empty_tile_index + delta[1]

                # Check if the move is valid
                if self.is_valid_move(empty_tile_index, new_index, move):
                    new_state = self.swap_tiles(current_node.state, empty_tile_index, new_index)
                    new_cost = current_node.cost + 1
                    new_heuristic = self.calculate_heuristic(new_state)
                    new_node = PuzzleNode(new_state, current_node, delta[0], new_cost, new_heuristic)

                    if new_node.state not in visited:
                        queue.put(new_node)

        # No solution found
        return None

    def is_valid_move(self, empty_tile_index, new_index, move):
        # Check if the move is valid based on the board boundaries
        if move == 0:  # UP
            return new_index >= 0
        elif move == 1:  # DOWN
            return new_index <= 8
        elif move == 2:  # LEFT
            return empty_tile_index % 3 != 0
        elif move == 3:  # RIGHT
            return (empty_tile_index + 1) % 3 != 0

    def swap_tiles(self, state, index1, index2):
        # Swap the tiles in the state
        new_state = list(state)
        new_state[index1], new_state[index2] = new_state[index2], new_state[index1]
        return tuple(new_state)

    def calculate_heuristic(self, state):
        # Manhattan distance heuristic
        heuristic = 0
        for i in range(9):
            if state[i] != 0:
                current_row, current_col = divmod(i, 3)
                goal_row, goal_col = divmod(state[i] - 1, 3)
                heuristic += abs(current_row - goal_row) + abs(current_col - goal_col)
        return heuristic

    def reconstruct_path(self, node):
        # Reconstruct the path from the goal node to the initial node
        path = []
        while node.parent is not None:
            path.append(node.move)
            node = node.parent
        path.reverse()
        return path


# Example usage
initial_state = [1, 2, 3, 4, 5, 6, 7, 0, 8]
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

solver = EightPuzzleSolver(initial_state, goal_state)
solution = solver.solve()

if solution is not None:
    print("Solution steps:", solution)
else:
    print("No solution found.")
