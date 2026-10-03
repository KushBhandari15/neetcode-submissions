class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        cleaned = "".join(char for char in s if char.isalnum()).lower()
        def helper(l, r, deleted):
            if l >= r:
                return True
            
            if cleaned[l] != cleaned[r]:
                if deleted:
                    return False
                else:
                    first = helper(l + 1, r, True)
                    second = helper(l, r - 1, True)

                    return first or second
            
            return helper(l + 1, r - 1, deleted)
        
        return helper(0, len(cleaned) - 1, False)