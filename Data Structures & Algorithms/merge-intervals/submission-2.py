class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        
        n = len(intervals)
        res = []
        i, j = 0, 1
        end = intervals[0][1]
        while j < n:
            if intervals[j][0] <= end:
                end = max(end, intervals[j][1])
                j += 1
            else:
                res.append([intervals[i][0], end])
                i = j
                end = intervals[i][1]
                j += 1
        
        res.append([intervals[i][0], end])
        return res
            