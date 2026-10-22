import heapq
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        heap = []
        for p, s, e in trips:
            heapq.heappush(heap, (s, e, p))
        
        order = []
        passengers = 0
        time = 0

        while heap:
            time += 1
            while heap and time >= heap[0][0]:
                s, e, p = heapq.heappop(heap)
                passengers += p
                heapq.heappush(order, (e, s, p))
            while order and time >= order[0][0]:
                e, s, p = heapq.heappop(order)
                passengers -= p
            if passengers > capacity:
                return False

        return True

