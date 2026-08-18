class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = ""

        while n > 0:
            res = res + str(n % 2)
            n = n // 2
        
        res = res + ("0" * (32 - len(res)))

        return int(res, 2)