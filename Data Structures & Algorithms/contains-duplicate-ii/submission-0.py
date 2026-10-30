from collections import defaultdict

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        helper = defaultdict(list)

        for i, num in enumerate(nums):
            num = nums[i]
            if num in helper:
                for j in helper[num]:
                    if abs(i - j) <= k:
                        return True

            helper[num].append(i)

        return False 