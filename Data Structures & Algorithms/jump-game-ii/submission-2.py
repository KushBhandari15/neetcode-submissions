class Solution:
    def jump(self, nums: List[int]) -> int:
        
        cache = {}

        def dfs(i):
            if i >= len(nums) - 1:
                return 0
            if i in cache:
                return cache[i]
                
            res = float('inf')
            for j in range(1, nums[i] + 1):
                curr = 1
                curr += dfs(i + j)
                res = min(res, curr)
            
            cache[i] = res
            return cache[i]
        
        return dfs(0)