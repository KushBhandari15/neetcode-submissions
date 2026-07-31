class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res, sol = [], []
        n = len(nums)

        def helper(i, curr_target):
            
            if curr_target == 0:
                res.append(sol[:])
                return
            if i == n or curr_target < 0:
                return
            
            # 1. Add nums[i]
            sol.append(nums[i])
            helper(i, curr_target - nums[i])
            sol.pop()

            # 2. Skip nums[i]
            helper(i+1, curr_target)


        helper(0, target)
        return res

            

            