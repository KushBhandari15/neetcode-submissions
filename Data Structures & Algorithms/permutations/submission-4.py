class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []
        seen = set()
        def dfs():
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            for num in nums:
                if num not in seen:
                    subset.append(num)
                    seen.add(num)
                    dfs()
                    subset.pop()
                    seen.remove(num)
        
        dfs()
        return res