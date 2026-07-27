class Solution:
    def climbStairs(self, n: int) -> int:
        
        res = 0
        dp = {1: 1, 2: 2}
        def helper(n):
            if n in dp:
                return dp[n]
            
            dp[n-1] = helper(n-1)
            dp[n-2] = helper(n-2)
            
            return dp[n-1] + dp[n-2]

        return helper(n)
