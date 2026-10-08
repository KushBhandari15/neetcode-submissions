class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []
        n = len(nums)
        def dfs():
            if len(subset) >= n:
                res.append(subset.copy())
                return
            
            for num in nums:
                if num not in subset:
                    subset.append(num)
                    dfs()
                    subset.pop()
        
        dfs()
        return res