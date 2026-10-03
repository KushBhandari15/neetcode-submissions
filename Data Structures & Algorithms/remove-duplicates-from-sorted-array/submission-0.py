class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        
        heap = []
        seen = set()

        for num in nums:
            if num not in seen:
                seen.add(num)
                heapq.heappush(heap, num)
            
        
        for i in range(len(seen)):
            nums[i] = heapq.heappop(heap)
        
        return len(seen)