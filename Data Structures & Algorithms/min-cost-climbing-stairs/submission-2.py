class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        n = len(cost)
        dp = {}
        def helper(idx, count):
            nonlocal n, dp

            if idx >= n:
                return count
            if idx in dp:
                return dp[idx]
            
            first = helper(idx+1, count + cost[idx])
            dp[idx+1] = first - cost[idx]
            second = helper(idx+2, count + cost[idx])
            dp[idx+2] = second - cost[idx]

            return min(first, second)

        first = helper(0, 0)
        second = helper(1, 0)

        return min(first, second)
