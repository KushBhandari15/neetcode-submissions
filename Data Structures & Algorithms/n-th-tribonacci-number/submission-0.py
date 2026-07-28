class Solution:
    def tribonacci(self, n: int) -> int:
        
        dp = {0:0, 1:1, 2:1}

        def helper(n):
            nonlocal dp
            if n in dp:
                return dp[n]

            dp[n-1] = helper(n-1)
            dp[n-2] = helper(n-2)
            dp[n-3] = helper(n-3)

            return dp[n-1] + dp[n-2] + dp[n-3]
        
        return helper(n)