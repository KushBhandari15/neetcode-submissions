class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        # Find the intersection
        slow = nums[0]
        fast = nums[slow]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
        
        # Find the start of the circle
        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow