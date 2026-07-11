class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s:
            return ""

        res = 0
        start = -1
        for i in range(len(s)):

            # Odd length
            x, y = i - 1, i + 1
            while x >= 0 and y < len(s):
                if s[x] == s[y]:
                    if y-x+1 > res:
                        res = y-x+1
                        start = x
                    x -= 1
                    y += 1
                else:
                    break
            
            x, y = i, i+1
            while x >= 0 and y < len(s):
                if s[x] == s[y]:
                    if y-x+1 > res:
                        res = y-x+1
                        start = x
                    x -= 1
                    y += 1
                else:
                    break
        
        if res == 0:
            return s[0]
        return s[start:start+res]


