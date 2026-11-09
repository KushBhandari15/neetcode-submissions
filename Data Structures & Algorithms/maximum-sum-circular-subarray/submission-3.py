class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        curr_max, curr_min = 0, 0
        glob_max, glob_min = nums[0], nums[0]
        total = 0

        for n in nums:
            curr_max = max(curr_max + n, n)
            curr_min = min(curr_min + n, n)
            total += n
            glob_max = max(glob_max, curr_max)
            glob_min = min(glob_min, curr_min)
        
        if glob_max < 0:
            return glob_max
        
        return max(glob_max, total - glob_min)