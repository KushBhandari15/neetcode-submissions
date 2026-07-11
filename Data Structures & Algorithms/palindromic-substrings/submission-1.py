class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0

        for i in range(len(s)):

            res += 1

            # Odd length
            x, y = i - 1, i + 1
            while x >= 0 and y < len(s):
                if s[x] == s[y]:
                    res += 1
                    x -= 1
                    y += 1
                else:
                    break
            
            # Even length
            x, y = i, i + 1
            while x >= 0 and y < len(s):
                if s[x] == s[y]:
                    res += 1
                    x -= 1
                    y += 1
                else:
                    break
            

        return res
