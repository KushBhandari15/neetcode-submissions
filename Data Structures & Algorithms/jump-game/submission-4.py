class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        goal = n - 1
        for idx in range(n - 2, -1, -1):
            if goal - idx <= nums[idx]:
                goal = idx
        
        return True if goal == 0 else False
