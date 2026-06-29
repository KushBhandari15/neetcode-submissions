class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            x, y = i + 1, n - 1
            while x < y:
                curr_sum = nums[i] + nums[x] + nums[y]
                if curr_sum == 0 and [nums[i], nums[x], nums[y]] not in res:
                    res.append([nums[i], nums[x], nums[y]])
                    x += 1
                    y -= 1
                elif curr_sum < 0:
                    x += 1
                else:
                    y -= 1

        
        return res
                


