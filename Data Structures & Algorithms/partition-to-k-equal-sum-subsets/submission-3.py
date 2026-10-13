class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        
        total = sum(nums)
        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        res = [0] * k

        def helper(idx):
            if idx == len(nums):
                return True

            for s in range(k):
                if res[s] + nums[idx] > target:
                    continue
                res[s] += nums[idx]
                if helper(idx + 1):
                    return True
                res[s] -= nums[idx]
                if res[s] == 0:
                    break
            return False
        
        return helper(0)