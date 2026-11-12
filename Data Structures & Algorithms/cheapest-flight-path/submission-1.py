class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        adjList = defaultdict(list)

        for dep, arr, prx in flights:
            adjList[dep].append((arr, prx))
        
        cache = {}
        def dfs(airport, stops):
            if (airport, stops) in cache:
                return cache[(airport, stops)]
            if stops > k + 1:
                return float('inf')
            if airport == dst:
                return 0
            
            res = float('inf')
            for nex, price in adjList[airport]:
                res = min(res, price + dfs(nex, stops + 1))
            
            cache[(airport, stops)] = res
            return res
        
        res = dfs(src, 0)
        return -1 if res == float('inf') else res