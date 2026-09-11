class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def deflection():

            l, r = 0, len(nums) - 1
            if nums[l] <= nums[r]:
                return 0

            while l < r:
                mid = (r + l) // 2
                if nums[mid] > nums[r]:
                    l = mid + 1
                else:
                    r = mid
            
            return l

        def binary_search(l, r):

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            
            return -1
        
        defl = deflection()

        first_idx = binary_search(0, defl - 1)
        if first_idx != -1:
            return first_idx
            
        return binary_search(defl, len(nums)-1)