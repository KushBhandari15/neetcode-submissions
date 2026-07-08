class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if not nums:
            return 0
        n = len(nums)
        if n < 2:
            return nums[0]
        
        first, second = 0, 0
        for num in nums[:n-1]:
            temp = max(first + num, second)
            first = second
            second = temp
        
        third, fourth = 0, 0
        for num in nums[1:]:
            temp = max(third + num, fourth)
            third = fourth
            fourth = temp
        
        return max(second, fourth)