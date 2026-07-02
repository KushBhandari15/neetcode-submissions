class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        adjList = {num : [] for num in range(numCourses)}

        for x, y in prerequisites:
            adjList[y].append(x)
        
        print(adjList)
        def dfs(start, end):

            seen = set()
            stack = [start]

            while stack:
                curr = stack.pop()
                for nei in adjList[curr]:
                    if nei == end:
                        return True
                    if nei not in seen:
                        stack.append(nei)
                        seen.add(nei)

            return False
        
        res = []
        for uj, vj in queries:
            res.append(dfs(vj, uj))
        
        return res
