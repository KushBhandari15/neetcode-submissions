class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(len(nums)):
            min_idx, min_val = i, nums[i]
            for j in range(i, len(nums)):
                if nums[j] < min_val:
                    min_val = nums[j]
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
