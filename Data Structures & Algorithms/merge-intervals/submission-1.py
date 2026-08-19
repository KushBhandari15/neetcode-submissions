class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        i = 0
        n = len(intervals)
        res = []
        while i < n:
            j = i + 1
            while j < n and intervals[i][1] >= intervals[j][0]:
                intervals[i][0] = min(intervals[i][0], intervals[j][0])
                intervals[i][1] = max(intervals[i][1], intervals[j][1])
                j += 1
            res.append(intervals[i])
            i = j
        
        return res

