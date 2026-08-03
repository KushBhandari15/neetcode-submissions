class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        helper = {"(": ")", "{": "}", "[": "]"}

        for bracket in s:
            if bracket in helper:
                stack.append(bracket)
            else:
                if stack:
                    latest = stack.pop()
                    if helper[latest] != bracket:
                        return False
                else:
                    return False
        
        return False if len(stack) > 0 else True
