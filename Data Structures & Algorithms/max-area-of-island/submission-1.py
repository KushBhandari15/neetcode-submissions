class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        res = 0
        rows = len(grid)
        cols = len(grid[0])
        neig = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(i, j, count):
            if grid[i][j] != 1:
                return count
            
            grid[i][j] = -1
            count += 1
            for x, y in neig:
                r_idx, c_idx = i + x, j + y
                if (r_idx < 0 or r_idx >= rows
                        or c_idx < 0 or c_idx >= cols):
                        continue
                count = dfs(r_idx, c_idx, count)
            
            return count
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    res = max(res, dfs(i, j, 0))
        
        return res
            

