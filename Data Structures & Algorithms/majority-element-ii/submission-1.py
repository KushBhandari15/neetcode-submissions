class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        nums.sort()
        res = []
        n = len(nums)
        i = 0
        print(nums, n)

        for j in range(n):
            if nums[i] != nums[j]:
                if j - i > n / 3:
                    res.append(nums[i])
                i = j

        print(j, i)
        if j - i + 1 > n / 3:
            res.append(nums[i])

        return res