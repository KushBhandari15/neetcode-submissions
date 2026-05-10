class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        start = set()
        total = set(nums)
        for num in nums:
            if num-1 not in total:
                start.add(num)
        
        res = 0
        for num in start:
            count = 1
            while True:
                if (num+count) in total:
                    count += 1
                else:
                    break
            res = max(res, count)

        return res