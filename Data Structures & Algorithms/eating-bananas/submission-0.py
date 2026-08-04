import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def helper(k):
            
            return sum(math.ceil(pile / k) for pile in piles)
        
        start, end = 1, max(piles)
        res = end

        while start <= end:
            
            mid = (start + end) // 2
            curr = helper(mid)
            if curr <= h:
                res = mid
                end = mid - 1
            else:
                start = mid + 1

        return res