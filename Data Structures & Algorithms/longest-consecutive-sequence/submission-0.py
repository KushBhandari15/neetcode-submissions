class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        start = set()
        for num in nums:
            if num-1 not in nums:
                start.add(num)
        
        res = 0
        for num in start:
            count = 1
            while True:
                if (num+count) in nums:
                    count += 1
                else:
                    break
            res = max(res, count)

        return res