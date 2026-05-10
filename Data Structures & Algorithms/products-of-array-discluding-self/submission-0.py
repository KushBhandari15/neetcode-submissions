class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        isZero = False
        for num in nums:
            if num == 0 and isZero == False:
                isZero = True
            else:
                total *= num

        res = []
        for num in nums:
            if isZero == True:
                if num == 0:
                    res.append(total)
                else:
                    res.append(0)
            else:
                res.append(int(total/num))
        
        return res