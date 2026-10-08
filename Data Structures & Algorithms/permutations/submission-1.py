class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []
        helper = set()
        n = len(nums)
        def dfs():
            if len(subset) >= n:
                res.append(subset.copy())
                return
            
            for num in nums:
                if num not in helper:
                    subset.append(num)
                    helper.add(num)
                    dfs()
                    subset.pop()
                    helper.remove(num)
        
        dfs()
        return res