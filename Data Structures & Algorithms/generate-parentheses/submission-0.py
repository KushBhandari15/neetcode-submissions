class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        def helper(curr, open_count):
            nonlocal res
            if len(curr) == n*2:
                print(curr, open_count)
                if open_count == 0:
                    res.append(curr)
                return
            
            helper(curr + "(", open_count + 1)
            if open_count > 0:
                helper(curr + ")", open_count - 1)

        
        helper("(", 1)
        return res

        
