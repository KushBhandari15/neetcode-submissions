class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {}
        def dfs(i):
            if i == n:
                return 1
            elif i > n:
                return 0
            if i in cache:
                return cache[i]
            
            total = dfs(i + 1) + dfs(i + 2)
            cache[i] = total           
            return cache[i]
        
        return dfs(0)