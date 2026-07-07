class Solution:
    def climbStairs(self, n: int) -> int:
        
        mapping = {1:1, 2:2}
        def helper(n):
            nonlocal mapping

            if n in mapping:
                return mapping[n]
            
            res = 0

            if n-1 not in mapping:
                mapping[n-1] = helper(n-1)
            res += mapping[n-1]
            if n-2 not in mapping:
                mapping[n-2] = helper(n-2)
            res += mapping[n-2]

            mapping[n] = res
            return res
            
        return helper(n)
            