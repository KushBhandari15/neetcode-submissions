class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])

        neig = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        queue = deque()
        fresh_count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1

        
        if fresh_count == 0:
            return 0

        time = 0
        while queue and fresh_count > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for x, y in neig:
                    r_idx, c_idx = r + x, c + y
                    if (0 <= r_idx < rows and
                        0 <= c_idx < cols and
                        grid[r_idx][c_idx] == 1):
                        
                        fresh_count -= 1
                        grid[r_idx][c_idx] = 2
                        queue.append((r_idx, c_idx))
            time += 1

        return time if fresh_count == 0 else -1


