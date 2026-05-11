class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        while True:
            if n == 0:
                return False
            elif n == 1:
                return True
            elif n % 2 != 0:
                return False
             
            n = n/2
