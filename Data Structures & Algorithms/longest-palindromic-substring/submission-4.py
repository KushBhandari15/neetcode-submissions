class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        n = len(s)
        count = 1
        res = s[0] if n > 0 else ""

        def helper(start, end):
            nonlocal count, n, res
            if not (start >= 0 and end < n and s[start] == s[end]):
                return

            length = end - start + 1
            if length > count:
                count = length
                res = s[start:end+1]

            helper(start - 1, end + 1)
        
        for i in range(n):
            helper(i, i)
            helper(i, i+1)

        return res
        
                
