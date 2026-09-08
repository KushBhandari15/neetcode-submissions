class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = set()
        num_to_idx = {}

        for i in range(len(nums)):
            look = target - nums[i]
            if look in seen:
                return [num_to_idx[look], i]
            else:
                seen.add(nums[i])
                num_to_idx[nums[i]] = i

        return []        