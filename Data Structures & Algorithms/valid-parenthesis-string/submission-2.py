class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack_left = []
        stack_star = []
        for i in range(len(s)):
            char = s[i]
            if char == "(":
                stack_left.append(i)
            elif char == "*":
                stack_star.append(i)
            else:
                if stack_left:
                    stack_left.pop()
                elif stack_star:
                    stack_star.pop()
                else:
                    return False

        while stack_left and stack_star:
            left_idx = stack_left.pop()
            star_idx = stack_star.pop()
            if star_idx < left_idx:
                return False
        
        if stack_left:
            return False
    
        return True
        