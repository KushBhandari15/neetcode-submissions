import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)
        
        res = 1
        for _ in range(k):
            res = -heapq.heappop(max_heap)
        
        return res