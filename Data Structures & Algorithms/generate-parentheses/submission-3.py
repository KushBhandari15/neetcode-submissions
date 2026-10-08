class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        curr = []
        def dfs(remaning1, remaining2):
            if remaning1 == remaining2 == n:
                res.append("".join(curr))
                return
            # use open
            if remaning1 < n:
                curr.append("(")
                dfs(remaning1 + 1, remaining2)
                curr.pop()
            # use close
            if remaining2 < remaning1:
                curr.append(")")
                dfs(remaning1, remaining2 + 1)
                curr.pop()


        dfs(0, 0)
        return res