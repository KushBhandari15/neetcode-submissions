class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        cache = {}
        def dfs(remaining):
            if remaining in cache:
                return cache[remaining]
            if remaining == 0:
                print("hi")
                return 0
            
            res = float('inf')
            for coin in coins:
                if remaining - coin >= 0:
                    res = min(res, 1 + dfs(remaining - coin))
            
            cache[remaining] = res
            return res
        
        res = dfs(amount)
        return -1 if res == float('inf') else res
