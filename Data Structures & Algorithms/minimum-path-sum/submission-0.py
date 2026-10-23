class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        cache = {}

        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]
            if r == rows - 1 and c == cols - 1:
                return grid[r][c]
            if r >= rows or c >= cols:
                return 201
            
            down, right = 0, 0
            down += grid[r][c] + dfs(r + 1, c)
            right += grid[r][c] + dfs(r, c + 1)

            cache[(r, c)] = min(down, right)
            return cache[(r, c)]
        
        return dfs(0, 0)