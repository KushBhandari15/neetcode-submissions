class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        n = len(nums)
        
        # Find the intersection
        slow = nums[0]
        fast = nums[slow]

        while True:
            if slow == fast:
                break
            
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
        
        first = slow
        second = 0

        while True:
            if first == second:
                return first
            
            first = nums[first]
            second = nums[second]
            