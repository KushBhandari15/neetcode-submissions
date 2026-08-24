class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}
        def dfs(i, calc):

            if i == len(nums):
                return 1 if calc == target else 0

            curr_id = (i, calc)
            if curr_id in cache:
                return cache[curr_id]
            
            first, second = 0, 0
            # Add to the total sum
            first += dfs(i + 1, calc + nums[i])
            # Subtract from the total sum
            second += dfs(i + 1, calc - nums[i])

            cache[curr_id] = first + second
            return cache[curr_id]
        
        return dfs(0, 0)
            
