class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        res = 0
        i = 0
        helper = set()
        for j in range(len(s)):
            
            while s[j] in helper:
                helper.remove(s[i])
                i += 1

            helper.add(s[j])
            res = max(res, j-i+1)

        
        return res
        
 