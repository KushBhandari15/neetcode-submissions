class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        res = 0
        curr_sum = 0
        prefixSum = {0: 1}

        for num in nums:
            curr_sum += num
            diff = curr_sum - k
            if diff in prefixSum:
                res += prefixSum[diff]
            prefixSum[curr_sum] = prefixSum.get(curr_sum, 0) + 1
        
        return res