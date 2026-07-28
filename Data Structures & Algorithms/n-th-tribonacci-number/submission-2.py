class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n == 0:
            return 0
        if n <= 2:
            return 1
        first, second, third = 0, 1, 1
        for num in range(3, n+1):
            tri = first + second + third
            first = second
            second = third
            third = tri
        return third

        # Top down memoization approach
        # dp = {0:0, 1:1, 2:1}

        # def helper(n):
        #     nonlocal dp
        #     if n in dp:
        #         return dp[n]

        #     dp[n-1] = helper(n-1)
        #     dp[n-2] = helper(n-2)
        #     dp[n-3] = helper(n-3)

        #     return dp[n-1] + dp[n-2] + dp[n-3]
        
        # return helper(n)