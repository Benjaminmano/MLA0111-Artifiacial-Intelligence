from collections import deque

class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # Down, Up, Right, Left

    def is_valid_move(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

    def bfs(self, start_row, start_col):
        visited = set()
        queue = deque([(start_row, start_col)])
        moves_count = 0

        while queue:
            for _ in range(len(queue)):
                row, col = queue.popleft()
                if self.grid[row][col] == 'D':
                    self.grid[row][col] = 'C'  # Clean the cell
                    moves_count += 1
                for dr, dc in self.moves:
                    new_row, new_col = row + dr, col + dc
                    if self.is_valid_move(new_row, new_col) and (new_row, new_col) not in visited and self.grid[new_row][new_col] == 'D':
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))

        return moves_count

    def clean_all(self):
        total_moves = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.grid[i][j] == 'D':
                    total_moves += self.bfs(i, j)
        return total_moves

# Example usage:
grid = [
    ['D', 'C', 'D', 'D'],
    ['D', 'D', 'D', 'C'],
    ['C', 'D', 'C', 'D'],
    ['D', 'D', 'D', 'D']
]

vacuum_cleaner = VacuumCleaner(grid)
total_moves = vacuum_cleaner.clean_all()
print("Total moves required to clean all dirty cells:", total_moves)
