class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        counter = {}
        n = len(nums)
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        res = []
        for num, count in counter.items():
            if count > n/3:
                res.append(num)
        return res        