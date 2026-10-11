class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        i, j = 0, len(nums) - 1

        while i <= j:
            
            mid_idx = (j + i) // 2
            mid = nums[mid_idx]

            if mid == target:
                return True
            
            if nums[i] == mid == nums[j]:
                i += 1
                j -= 1
            elif nums[i] <= mid:
                if nums[i] <= target < mid:
                    j = mid_idx - 1
                else:
                    i = mid_idx + 1
            else:
                if mid < target <= nums[j]:
                    i = mid_idx + 1
                else:
                    j = mid_idx - 1

        return False


