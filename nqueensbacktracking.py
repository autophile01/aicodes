class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.solutions = []

    def solve(self):
        self._backtrack(0)
        return self.solutions

    def _backtrack(self, col):
        if col == self.n:
            solution = self.board.copy()
            self.solutions.append(solution)
            return True

        for row in range(self.n):
            if self._is_safe(row, col):
                self.board[col] = row
                self._backtrack(col + 1)
                self.board[col] = -1

    def _is_safe(self, row, col):
        for i in range(col):
            if (
                self.board[i] == row
                or self.board[i] - row == i - col
                or self.board[i] - row == col - i
            ):
                return False
        return True


# Example usage
n = 4
n_queens = NQueens(n)
solutions = n_queens.solve()

print(f"Number of solutions for {n}-queens: {len(solutions)}")
for i, solution in enumerate(solutions):
    print(f"Solution {i+1}:")
    for row in solution:
        queens_row = ["Q" if i == row else "-" for i in range(n)]
        print(" ".join(queens_row))
    print()
