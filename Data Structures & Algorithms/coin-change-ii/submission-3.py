class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        cache = {}
        def dfs(rem, idx):
            if (rem, idx) in cache:
                return cache[(rem, idx)]
            if rem == 0:
                return 1
            if idx >= len(coins) or rem < 0:
                return 0
            
            cache[(rem, idx)] = dfs(rem - coins[idx], idx) + dfs(rem, idx + 1)
            return cache[(rem, idx)]
        
        return dfs(amount, 0)