class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        x = 0
        while x < len(nums):
            i, j = x + 1, len(nums) - 1
            while i < j:
                curr_sum = nums[x] + nums[i] + nums[j]
                if curr_sum == 0:
                    res.append([nums[x], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif curr_sum > 0:
                    j -= 1
                else:
                    i += 1
            x += 1
            while x < len(nums) and nums[x] == nums[x - 1]:
                x += 1
    
        return res