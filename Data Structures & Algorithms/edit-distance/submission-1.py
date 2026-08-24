class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        operations = 0
        cache = {}
        
        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i,j)]
            if i >= len(word1) and j >= len(word2):
                return 0
            if i >= len(word1):
                return len(word2) - j
            if j >= len(word2):
                return len(word1) - i
            if word1[i] == word2[j]:
                return dfs(i+1, j+1)

            # Either replace, delete or add
            # 1. Replace
            r = 1 + dfs(i+1, j+1)
            # 2. Delete
            d = 1 + dfs(i+1, j)
            # 3. Insert
            a = 1 + dfs(i, j+1)   

            cache[(i, j)] = min(r, d, a)
            return min(r, d, a)
        
        return dfs(0, 0)