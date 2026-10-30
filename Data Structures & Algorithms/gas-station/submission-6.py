class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        diff = [x - y for x, y in zip(gas, cost)]
        if sum(diff) < 0:
            return -1

        n = len(gas)
        i = 0
        while i < n:
            tank = diff[i]
            j = (i + 1) % n
            while i != j and tank > 0:
                tank += diff[j]
                j = (j + 1) % n
            if i == j:
                return i
            i = j
        return -1
    