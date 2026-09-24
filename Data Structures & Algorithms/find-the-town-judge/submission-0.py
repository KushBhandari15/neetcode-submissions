from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        adjacency_list_1 = defaultdict(list)
        adjacency_list_2 = defaultdict(list)
        for t1, t2 in trust:
            adjacency_list_1[t2].append(t1)
            adjacency_list_2[t1].append(t2)
        
        for p in range(n):
            # Condition 1
            if len(adjacency_list_2[p + 1]) == 0:
                if len(adjacency_list_1[p + 1]) == n - 1:
                    return p + 1
        
        return -1
