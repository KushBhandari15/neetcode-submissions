class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        res = 0
        if n == 1:
            return res
        i, j = 0, 1

        while j < n:
            curr_pnl = prices[j] - prices[i]
            res = max(res, curr_pnl)

            if prices[j] < prices[i]:
                i = j
            j += 1
            
        return res
