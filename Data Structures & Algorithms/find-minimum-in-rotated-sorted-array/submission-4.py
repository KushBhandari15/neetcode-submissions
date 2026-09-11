class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        res = 1001
        while l <= r:
            mid = (l + r) // 2
            res = min(res, nums[mid], nums[l], nums[r])
            if nums[l] < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
    
        return res