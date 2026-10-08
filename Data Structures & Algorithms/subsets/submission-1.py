class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        res = []
        def dfs(idx, arr):
            if idx >= n:
                res.append(arr)
                return

            dfs(idx + 1, arr)
            dfs(idx + 1, arr + [nums[idx]])

            return
        
        dfs(0, [])

        return res