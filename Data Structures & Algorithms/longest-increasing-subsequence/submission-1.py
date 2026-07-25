from functools import cache
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        @cache
        def helper(curr, prev):
            nonlocal n
            if curr >= n:
                return 0
            
            skip = helper(curr+1, prev)

            take = 0
            if prev == -1 or nums[curr] > nums[prev]:
                take = 1 + helper(curr+1, curr)
            
            return max(take, skip)
        
        return helper(0, -1)