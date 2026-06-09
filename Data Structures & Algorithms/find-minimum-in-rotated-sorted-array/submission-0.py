class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        res = 1001
        l, r = 0, len(nums) - 1

        while l <= r:

            m = (l + r)//2
            left = nums[l]; mid = nums[m]; right = nums[r]
            res = min(left, mid, right, res)

            if left <= mid <= right:
                res = min(res, left)
                return res
            elif left <= mid:
                l = m + 1
            else:
                r = m - 1
            
        
        return res