class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []

        def dfs(idx):
            if idx >= len(nums) or sum(subset) > target:
                if sum(subset) == target:
                    res.append(subset.copy())
                return
            
            # choice 1: use curr number
            subset.append(nums[idx])
            dfs(idx)
            subset.pop()

            # choice 2: skip and move forward
            dfs(idx + 1)

        dfs(0)
        return res