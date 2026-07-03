class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        res = 0

        def dfs(i, j):
            
            stack = [(i, j)]
            grid[i][j] = "0"

            while stack:

                curr_i, curr_j = stack.pop()
                neighbor = [[-1, 0], [1, 0], [0, -1], [0, 1]]

                for x, y in neighbor:
                    r_idx, c_idx = curr_i+x, curr_j+y
                    if (r_idx < 0 or r_idx >= rows
                        or c_idx < 0 or c_idx >= cols):
                        continue

                    if grid[r_idx][c_idx] == "1":
                        stack.append((r_idx, c_idx))
                        grid[r_idx][c_idx] = 0
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        
        return res
        

