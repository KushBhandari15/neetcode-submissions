class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        cache = {}

        def dfs(total):
            if total in cache:
                return cache[total]
            if total == target:
                return 1
            if total > target:
                return 0

            match = 0
            for num in nums:
                match += dfs(total + num)
            
            cache[total] = match
            return cache[total]

        res = 0
        for num in nums:
            res += dfs(num)
        
        return res