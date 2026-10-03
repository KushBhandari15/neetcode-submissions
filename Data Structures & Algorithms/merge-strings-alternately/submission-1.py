class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        l, r = 0, 0
        x, y = len(word1), len(word2)
        res = ""
        while l < x and r < y:
           res += word1[l]
           res += word2[r]
           l += 1
           r += 1
        
        while l < x:
            res += word1[l]
            l += 1
        while r < y:
            res += word2[r]
            r += 1
        
        return res
         