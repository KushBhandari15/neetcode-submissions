class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        dp = {}
        def helper(idx):
            nonlocal n, dp

            if idx >= n:
                return 0
            if idx in dp:
                return dp[idx]
            
            dp[idx] = cost[idx] + min(helper(idx+1), helper(idx+2))

            return dp[idx]

        first = helper(0)
        second = helper(1)

        return min(first, second)
