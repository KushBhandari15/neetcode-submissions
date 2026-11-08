class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        p1 = [1] * n
        product = 1
        prev = 1
        for i, num in enumerate(nums):
            product = product * prev
            p1[i] = product
            prev = num
        
        p2 = [1] * n
        product = 1
        prev = 1
        for i in range(n - 1, -1, -1):
            num = nums[i]
            product = product * prev
            p2[i] = product
            prev = num

        res = []
        for num1, num2 in zip(p1, p2):
            res.append(num1 * num2)
    
        return res