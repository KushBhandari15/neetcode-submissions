class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = defaultdict(list)

        for i, num in enumerate(nums):
            need = target - num
            if need in seen:
                return [seen[need][0], i]
            seen[num].append(i)
        
        return [-1, -1]
