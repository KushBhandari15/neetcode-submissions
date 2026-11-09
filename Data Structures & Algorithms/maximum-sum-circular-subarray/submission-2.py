class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        i, j = 0, 1
        running_sum, res = nums[0], nums[0]
        n = len(nums)

        while i < n:
            if running_sum < 0 or i == j:
                i += 1
                j = (i + 1) % n
                if i < n:
                    running_sum = nums[i]
            else:
                running_sum += nums[j]
                j = (j + 1) % n
            res = max(res, running_sum)
    
        return res