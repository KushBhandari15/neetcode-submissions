class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        cache = {}

        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return 0
            if obstacleGrid[r][c] == 1:
                return 0
            if r == rows - 1 and c == cols - 1:
                return 1
            
            down, right = 0, 0
            down += dfs(r + 1, c)
            right += dfs(r, c + 1)

            cache[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return cache[(r, c)]
        
        return dfs(0, 0)
