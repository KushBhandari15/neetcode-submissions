class Solution:
    def tribonacci(self, n: int) -> int:
        
        # Top down memoization approach
        dp = {0:0, 1:1, 2:1}

        def helper(n):
            nonlocal dp
            if n in dp:
                return dp[n]

            dp[n] = helper(n-1) + helper(n-2) + helper(n-3)

            return dp[n]
        
        return helper(n)