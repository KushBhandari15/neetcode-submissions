class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        neig = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != 1:
                return 0
            
            grid[i][j] = 0
            area = 1

            for x, y in neig:
                area += dfs(i + x, j + y)
            
            return area
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j))
        
        return res
            

