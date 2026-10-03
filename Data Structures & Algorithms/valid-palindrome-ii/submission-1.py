class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            
            return True
        
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                first = is_palindrome(l + 1, r)
                second = is_palindrome(l, r - 1)
                return first or second
            l += 1 
            r -= 1
        
        return True