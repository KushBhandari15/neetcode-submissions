from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        counter = Counter(tasks)
        max_heap = [-count for count in counter.values()]
        heapq.heapify(max_heap)

        time = 0
        cooldown_q = deque()

        while max_heap or cooldown_q:
            time += 1

            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt != 0:
                    cooldown_q.append((cnt, time+n))
            
            if cooldown_q and cooldown_q[0][1] == time:
                cnt, _ = cooldown_q.popleft()
                heapq.heappush(max_heap, cnt)
        
        return time

