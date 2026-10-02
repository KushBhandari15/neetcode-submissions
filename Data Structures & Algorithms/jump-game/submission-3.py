class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        memo = {}

        def helper(i):
            if i in memo:
                return memo[i]
            if i >= len(nums) - 1:
                print("Reached")
                return True
            print(i)    
            for jump in range(1, nums[i] + 1):
                if helper(i + jump):
                    memo[i] = True
                    return memo[i]

            memo[i] = False
            return memo[i]
        
        return helper(0)