class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Naive Solution
        n = len(nums)
        k = k % n
        if k == 0:
            return
        copy = nums[:]

        for i in range(n):
            idx = (i + k) % n
            nums[idx] = copy[i]