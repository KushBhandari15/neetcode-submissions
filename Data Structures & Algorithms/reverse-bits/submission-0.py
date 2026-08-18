class Solution:
    def reverseBits(self, n: int) -> int:
        
        res = 0
        place = 1

        while n > 0:
            res = res + (n%2)*place
            place = place * 10
            n = n//2
        
        string = str(res)
        length = len(string)
        string = ("0"*(32-length)) + string
        string = string[::-1]

        return int(string, 2)