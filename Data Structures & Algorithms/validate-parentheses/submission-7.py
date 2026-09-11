class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        helper = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for char in s:
            if char not in helper:
                stack.append(char)
            else:
                if not stack or helper[char] != stack.pop():
                    return False
        
        return False if stack else True