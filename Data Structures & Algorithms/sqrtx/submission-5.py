class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0 or x == 1:
            return x

        for i in range(x + 1):
            if i ** 2 == x:
                return i
            if i ** 2 > x:
                return i - 1
        
