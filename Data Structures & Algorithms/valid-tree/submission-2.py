class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        if not n:
            return False

        adjList = {num: [] for num in range(n)}
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])

        print(adjList)
        stack = [(0, -1)]
        seen = set()
        seen.add(0)

        while stack:
            curr, parent = stack.pop()
            for neighbor in adjList[curr]:
                if neighbor is parent:
                    continue
                if neighbor not in seen:
                    stack.append((neighbor, curr))
                    seen.add(neighbor)
                else:
                    return False

        if len(seen) != n:
            return False
            
        return True