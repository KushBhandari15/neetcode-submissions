class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res, sol = [], []
        candidates.sort()
        n = len(candidates)

        def backtrack(i, curr_target):
            
            if curr_target == 0:
                res.append(sol[:])
                return

            if i == n or curr_target < 0:
                return

            # 1. Add nums[i]
            sol.append(candidates[i])
            backtrack(i+1, curr_target - candidates[i])
            sol.pop()

            # 2. Skip nums[i]
            while i + 1 < n and candidates[i] == candidates[i+1]:
                i += 1
            
            backtrack(i+1, curr_target)
        
        backtrack(0, target)
        return res

            