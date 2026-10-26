class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def can_ship(capacity):
            ships, curr_cap = 1, capacity
            for w in weights:
                if curr_cap - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    curr_cap = capacity
                curr_cap -= w
            return True
        
        l, r = max(weights), sum(weights)
        res = r

        while l <= r:
            mid = (l + r) // 2
            if can_ship(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res

