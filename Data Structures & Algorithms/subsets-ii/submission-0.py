class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res, sol = [], []
        n = len(nums)

        nums.sort()

        def backtrack(i):

            if i == n:
                res.append(sol[:])
                return
            
            # 1. Use the current number
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()

            # 2. Skip cuurent number
            while i + 1 < n and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1)
        
        backtrack(0)
        return res