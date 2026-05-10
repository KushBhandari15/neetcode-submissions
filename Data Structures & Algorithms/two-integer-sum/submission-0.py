class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        helper = {}
        for i in range(n):
            curr = nums[i]
            needed = target - curr
            if needed in helper:
                return [helper.get(needed), i]
            helper[curr] = i
        
        return [-1, -1]