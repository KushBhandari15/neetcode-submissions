"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        if not intervals:
            return 0

        sorted_intervals = sorted(intervals, key = lambda x: x.start)
        meeting_rooms = 1
        rooms = [sorted_intervals[0].end]
        heapq.heapify(rooms)

        for i in range(1, len(sorted_intervals)):
            start = sorted_intervals[i].start
            end = sorted_intervals[i].end
            if rooms[0] <= start:
                heapq.heappop(rooms)
            
            heapq.heappush(rooms, end)
        
        return len(rooms)
