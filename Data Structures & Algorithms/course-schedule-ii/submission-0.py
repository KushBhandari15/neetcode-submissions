class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        adj_list = defaultdict(list)
        for c, p in prerequisites:
            adj_list[p].append(c)
        
        seen = [0] * numCourses
        res = []

        def dfs(course):

            if seen[course] == 1:
                return False # Found cycle
            if seen[course] == 2:
                return True
            
            seen[course] = 1

            for c in adj_list[course]:
                if not dfs(c):
                    return False
            
            res.append(course)
            seen[course] = 2
            return True
        
        for c in range(numCourses):
            if seen[c] == 0:
                if not dfs(c):
                    return []
        
        return res[::-1]