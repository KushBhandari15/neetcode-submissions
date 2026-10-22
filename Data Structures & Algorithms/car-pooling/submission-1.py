import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        trips.sort(key = lambda x: x[1])

        heap = []
        passengers = 0

        for p, s, e in trips:

            while heap and heap[0][0] <= s:
                end, count = heapq.heappop(heap)
                passengers -= count
            passengers += p

            if passengers > capacity:
                return False
            
            heapq.heappush(heap, (e, p))
        
        return True

