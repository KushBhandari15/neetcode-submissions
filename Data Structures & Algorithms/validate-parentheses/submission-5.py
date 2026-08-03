class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        helper = {")": "(", "}": "{", "]": "["}

        for bracket in s:
            if bracket in helper:
                latest = stack.pop() if stack else "#"
                if helper[bracket] != latest:
                    return False
            else:
                stack.append(bracket)

        
        return False if len(stack) > 0 else True
