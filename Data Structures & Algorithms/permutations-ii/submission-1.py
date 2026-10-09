class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        subset = []
        seen = set()

        def dfs():
            if len(subset) == len(nums):
                if subset not in res:
                    res.append(subset.copy())
                return
            for i in range(len(nums)):
                if i not in seen:
                    if not (i-1>0 and nums[i]==nums[i - 1] and i-1 not in seen):
                        subset.append(nums[i])
                        seen.add(i)
                        dfs()
                        subset.pop()
                        seen.remove(i)

        dfs()
        return res