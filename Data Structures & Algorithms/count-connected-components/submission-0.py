class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjList = {num: [] for num in range(n)}
        
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        seen = set()
        res = 0

        def dfs(node):
            nonlocal res
            if node in seen:
                return

            stack = [node]
            seen.add(node)

            while stack:
                curr = stack.pop()
                for nei in adjList[curr]:
                    if nei not in seen:
                        stack.append(nei)
                        seen.add(nei)
                
            res += 1

        for node in range(n):
            dfs(node)
        
        return res
            


