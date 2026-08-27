class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        left = 0
        right = len(nums) - 1
        k = 0

        while left <= right:

            if nums[left] != val:
                left += 1
                k += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1

        return k