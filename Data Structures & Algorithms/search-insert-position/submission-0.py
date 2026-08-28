class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        if target < nums[0]:
            return 0
        if target > nums[n-1]:
            return n

        def bs(start, end):

            if start == end:
                return start 
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return bs(start, mid)
            else:
                return bs(mid + 1, end)

        return bs(0, n - 1)