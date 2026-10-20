from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjList = defaultdict(list)
        for ui, vi, ti in times:
            adjList[ui].append((vi, ti))
        
        dist = [float('inf')] * (n + 1)

        def dfs(k, time):
            if time >= dist[k]:
                return
            
            dist[k] = time

            for vi, ti in adjList[k]:
                dfs(vi, time + ti)
            
        dfs(k, 0)
        res = max(dist[1:])
        return -1 if res == float('inf') else res
                