from collections import defaultdict
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        half = total // 2
        n = len(nums)

        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                nextDP.add(t)
                nextDP.add(t + nums[i])
            dp = nextDP
        
        return half in dp

            
            


