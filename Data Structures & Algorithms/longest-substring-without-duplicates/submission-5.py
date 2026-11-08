class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        i, j = 0, 1
        unique = {s[0]}
        res = 1
        while j < len(s):
            if s[j] in unique:
                unique.remove(s[i])
                i += 1
            else:
                unique.add(s[j])
                j += 1
                res = max(res, j - i)
        res = max(res, j - i)
        return res