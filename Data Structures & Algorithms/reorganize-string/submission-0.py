import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        
        counter = {}
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        
        max_heap = []
        for char, count in counter.items():
            heapq.heappush(max_heap, (-count, char))
        
        res = ""
        queue = deque()        
        for _ in range(len(s)):

            first_count = 0
            if max_heap:
                first_count, first_char = heapq.heappop(max_heap)
                res += first_char
                first_count += 1
            else:
                return "" 
            
            if queue:
                waiting_count, waiting_char = queue.popleft()
                heapq.heappush(max_heap, (waiting_count, waiting_char))
            
            if first_count != 0:
                queue.append((first_count, first_char))
        
        return res