class Solution:
    def isValid(self, s: str) -> bool:
        
        helper = {
            ")" : "(",
            "}" : "{",
            "]" : "[" 
        }

        stack = []
        for i in s:
            if i == ")" or i == "]" or i == "}":
                if not stack:
                    return False
                curr = stack.pop()
                if curr != helper[i]:
                    return False
            else:
                stack.append(i)
        
        if not stack:
            return True
        return False
                