class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        least = float('inf')
        most = float('-inf')
        for price in prices:
            
            if price < least:
                least = price
                most = price
            else:
                most = max(price, most)
            
            if most-least > 0:
                profit += most - least
                least = most
        
        return profit

