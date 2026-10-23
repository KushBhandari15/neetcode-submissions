class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        while True:
            if n in seen:
                return False
            if n == 1:
                return True
            
            seen.add(n)

            digits = []
            curr = n
            while curr:
                digits.append(curr % 10)
                curr = curr // 10

            new = 0
            for digit in digits:
                new += digit**2

            n = new