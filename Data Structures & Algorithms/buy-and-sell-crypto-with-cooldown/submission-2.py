
from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        res = 0
        dp = {}

        def dfs(i, holding):
            if i >= n:
                return 0
            
            curr_id = (i, holding)
            if curr_id in dp:
                return dp[curr_id]
            
            # Skip current price
            cooldown = dfs(i+1, holding)

            # Trade at current price
            if holding:
                trade = prices[i] + dfs(i+2, 0)
            else:
                trade = -prices[i] + dfs(i+1, 1)

            dp[curr_id] = max(cooldown, trade)
            
            return dp[curr_id]
            
        
        return dfs(0, 0)
