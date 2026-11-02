from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adjList = defaultdict(list)
        for first, second in edges:
            adjList[first].append(second)
            adjList[second].append(first)
        
        def dfs(node, parent):
            curr = 0
            for edge in adjList[node]:
                if edge != parent:
                    curr = max(curr, 1 + dfs(edge, node))
            return curr
        
        res = []
        lowest = float('inf')
        for node in range(n):
            curr = dfs(node, None)
            if curr < lowest:
                lowest = curr 
                res = [node]
            elif curr == lowest:
                res.append(node)
        
        return res
