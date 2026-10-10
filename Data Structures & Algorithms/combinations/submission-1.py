class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        res = []
        subset = []
        seen = set()
        def dfs(start):
            if len(subset) == k:
                res.append(subset.copy())
            
            for i in range(start, n + 1):
                if i not in seen:
                    subset.append(i)
                    seen.add(i)
                    dfs(i + 1)
                    subset.pop()
                    seen.remove(i)
        
        dfs(1)
        return res