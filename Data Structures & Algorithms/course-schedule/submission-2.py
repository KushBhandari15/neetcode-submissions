class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        adjList = {num: [] for num in range(numCourses)}

        for course, pre in prerequisites:
            adjList[course].append(pre)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if adjList[course] == []:
                return True
            
            visited.add(course)
            for pre in adjList[course]:
                if not dfs(pre):
                    return False

            visited.remove(course)
            adjList[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True


