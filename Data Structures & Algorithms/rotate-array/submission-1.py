class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        if k == 0:
            return  
        new = []
        for _ in range(k):
            new.append(nums.pop())
        
        new.reverse()
        nums[:0] = new