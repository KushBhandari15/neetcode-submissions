class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res, sol = [], []
        n = len(nums)

        def helper(i):

            if i == n:
                res.append(sol[:])
                return
            
            # Don't pick up nums[i]
            helper(i+1)
            # Pickup nums[i]
            sol.append(nums[i])
            helper(i+1)
            sol.pop()
        
        helper(0)
        return res
