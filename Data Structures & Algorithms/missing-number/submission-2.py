class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        
        helper = set(nums)

        for i in range(len(nums) + 1):
            if i not in helper:
                return i
        