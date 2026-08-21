from collections import defaultdict
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        half = total // 2
        n = len(nums)

        dp = [False] * (half + 1)
        dp[0] = True

        for num in nums:
            for i in range(half, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
            
            if dp[half]:
                return True
        
        return False

            
            


