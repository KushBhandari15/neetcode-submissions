class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res, sol = [], []
        n = len(nums)

        def helper(i):
            
            add = sum(sol)
            if add == target and sol not in res:
                res.append(sol[:])
                return
            if i == n or add > target:
                return
            
            
            # Three options

            # 1. Skip nums[i]
            helper(i+1)

            # 2. Add nums[i] and increment i
            sol.append(nums[i])
            helper(i+1)
            sol.pop()

            # 3. Add nums[i] and stay in i'th index
            sol.append(nums[i])
            helper(i)
            sol.pop()
        
        helper(0)
        return res

            

            