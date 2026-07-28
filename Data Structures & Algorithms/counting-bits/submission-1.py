class Solution:
    def countBits(self, n: int) -> List[int]:
        
        if n == 0:
            return [0]
        
        res = [0] * (n+1)
        res[1] = 1
        
        def helper(n):

            if n == 0:
                return 0
            if n == 1:
                return 1
            if n >= 2 and res[n] != 0:
                return res[n]
            
            bit = n%2
            res[n] += helper(n//2) + bit

            return res[n]

        for num in range(2, n+1):
            helper(num)
        
        return res

