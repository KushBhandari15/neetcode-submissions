class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n = len(nums)
        left = 0
        curr_sum = nums[left]
        right = 0

        res = 1000000

        while right < n:
            if curr_sum >= target:
                res = min(res, right - left + 1)
                curr_sum -= nums[left]
                left += 1

            else:
                right += 1
                if right < n:
                    curr_sum += nums[right]

        return 0 if res == 1000000 else res
                    
