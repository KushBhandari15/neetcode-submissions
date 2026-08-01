import math
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res, sol = [], []
        helper = set()
        n = len(nums)
        
        def backtrack():

            if len(sol) == n:
                res.append(sol[:])
                return

            for i in range(n):
                if i not in helper:
                    sol.append(nums[i])
                    helper.add(i)
                    backtrack()
                    sol.pop()
                    helper.remove(i)
        
        backtrack()
        return res
        