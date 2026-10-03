class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        copy = nums.copy()
        n = len(nums)
        for i in range(n):
            idx = (i + k) % n
            nums[idx] = copy[i]
    

