from collections import defaultdict
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        adj = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i][0], points[i][1]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j][0], points[j][1]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        seen = set()
        minH = [[0, 0]]

        while len(seen) < len(points):
            cost, i = heapq.heappop(minH)
            if i in seen:
                continue
            res += cost
            seen.add(i)
            for dist, nei in adj[i]:
                if nei not in seen:
                    heapq.heappush(minH, [dist, nei])
        
        return res
