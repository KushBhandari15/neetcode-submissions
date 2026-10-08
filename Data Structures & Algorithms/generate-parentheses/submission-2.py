class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def valid_parenthesis(curr):
            stack = []
            for char in curr:
                if char == ")":
                    if not stack:
                        return False
                    stack.pop()
                else:
                    stack.append(char)
            
            return True if not stack else False
        
        res = []
        curr = []
        def dfs(remaning1, remaining2):
            if remaning1 <= 0 and remaning1 <= 0:
                if valid_parenthesis("".join(curr)):
                    res.append("".join(curr))
            
            # use open
            if remaning1 > 0:
                curr.append("(")
                dfs(remaning1 - 1, remaining2)
                curr.pop()
            # use close
            if remaining2 > 0:
                curr.append(")")
                dfs(remaning1, remaining2 - 1)
                curr.pop()


        dfs(n, n)
        return res