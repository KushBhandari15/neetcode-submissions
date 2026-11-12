class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        hash_set = set(dictionary)
        cache = {}

        def dfs(i):
            if i in cache:
                return cache[i]
            if i == len(s):
                return 0
            
            # choice 1
            res = 1 + dfs(i + 1)
            
            # choice 2
            for j in range(i, len(s)):
                if s[i : j + 1] in dictionary:
                    res = min(res, dfs(j + 1))
            cache[i] = res
            return res
        
        return dfs(0)