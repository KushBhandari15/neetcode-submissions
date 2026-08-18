class Solution:
    def countBits(self, n: int) -> List[int]:
        
        if n == 0:
            return [0]
        
        res = [0] * (n+1)
        res[1] = 1

        def helper(num):

            if num == 0:
                return 0
            if num == 1:
                return 1
            if num >= 2 and res[num] != 0:
                return res[num]
            
            res[num] = helper(num//2) + num%2

            return res[num]
        
        for i in range(2, n+1):
            res[i] = helper(i)

        return res