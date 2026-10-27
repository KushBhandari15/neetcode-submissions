import heapq
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        stone_sum = sum(stones)
        target = math.ceil(stone_sum / 2)

        dp = {}

        def dfs(idx, total):
            if total >= target or idx == len(stones):
                return abs(total - (stone_sum - total))
            if (idx, total) in dp:
                return dp[(idx, total)]
            
            dp[(idx, total)] = min(dfs(idx + 1, total),
                        dfs(idx + 1, total + stones[idx]))
        
            return dp[(idx, total)]

        return dfs(0, 0)

