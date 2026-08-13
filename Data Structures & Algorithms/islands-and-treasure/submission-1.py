class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        rows = len(grid)
        cols = len(grid[0])
        neig = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j))

        while queue:
            r, c = queue.popleft()
            for x, y in neig:
                r_idx, c_idx = r + x, c + y

                if (0 <= r_idx < rows and
                    0 <= c_idx < cols and
                    grid[r_idx][c_idx] == 2147483647):

                    grid[r_idx][c_idx] = grid[r][c] + 1
                    queue.append((r_idx, c_idx))
        