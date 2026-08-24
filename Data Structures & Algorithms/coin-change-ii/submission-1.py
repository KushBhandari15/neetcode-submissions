class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        res = 0
        
        cache = {}
        def dfs(i, rem):
            
            if (i, rem) in cache:
                return cache[(i, rem)]
            if rem == 0:
                return 1
            if i >= len(coins) or rem < 0:
                return 0
            
            curr_id = (i, rem)
            first, second = 0, 0
            # Skip current coin
            first += dfs(i + 1, rem)
            # Use current coin and stay
            second += dfs(i, rem - coins[i])
            
            cache[curr_id] = first+second
            return cache[curr_id]


        return dfs(0, amount)
