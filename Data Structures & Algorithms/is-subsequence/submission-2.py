class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s:
            return True

        pointer = 0
        n = len(s)

        for char in t:
            if s[pointer] == char:
                pointer += 1
                if pointer == n:
                    return True
        
        return False