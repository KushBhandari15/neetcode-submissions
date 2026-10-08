class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        subset = []

        def dfs(idx):
            if idx >= len(nums):
                res.append(subset.copy())
                return
            # use current
            subset.append(nums[idx])
            dfs(idx + 1)
            subset.pop()

            # skip
            idx += 1
            while idx < len(nums) and nums[idx] == nums[idx - 1]:
                idx += 1
            dfs(idx)

        dfs(0)
        return res