class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        curr_max = 0  
        res = 0

        for i in range(len(prices) - 1, -1, -1):
            res = max(res, curr_max - prices[i])
            curr_max = max(curr_max, prices[i])
        
        return res