from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adjList = defaultdict(list)
        
        for i in range(len(equations)):
            x, y = equations[i]
            adjList[x].append((y, values[i]))
            adjList[y].append((x, 1/values[i]))
        
        print(adjList)
        
        def dfs(start, end):
            if start not in adjList or end not in adjList:
                return -1.0
            if start == end:
                return 1.0
            
            seen = set()
            stack = [(start, 1)]
            seen.add(start)

            while stack:
                curr, prod = stack.pop()
                if curr == end:
                    return prod
                for nei, val in adjList[curr]:
                    if nei not in seen:
                        stack.append((nei, prod*val))
                        seen.add(nei)
            
            return -1.0
        
        res = []
        for start, end in queries:
            res.append(dfs(start, end))

        return res