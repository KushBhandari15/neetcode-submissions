class Solution:
    def reverse(self, x: int) -> int:
        
        negative = False
        
        if x < 0:
            negative = True
            x *= -1

        reverse = int(str(x)[::-1])

        if negative:
            reverse *= -1

        if reverse > 2**31 - 1 or reverse < -2**31:
            return 0

        return reverse