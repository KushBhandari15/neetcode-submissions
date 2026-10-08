class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []
        candidates.sort()
        n = len(candidates)
        def dfs(idx):
            if idx >= len(candidates) or sum(subset) >= target:
                if sum(subset) == target:
                    res.append(subset.copy())
                return
            
            # choice 1: use current and move on
            subset.append(candidates[idx])
            dfs(idx + 1)
            subset.pop()
            # choice 2: skip current and move on
            idx = idx + 1
            while idx < n and candidates[idx] == candidates[idx - 1]:
                idx += 1
            dfs(idx)
    
        dfs(0)
        return res