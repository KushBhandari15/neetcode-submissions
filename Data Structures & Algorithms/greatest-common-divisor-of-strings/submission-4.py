class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        n, m = len(str1), len(str2)
        idx = min(n, m)
        while idx > 0:
            curr = str1[:idx]
            if n % idx == 0 and m % idx == 0:
                q1 = n // idx; q2 = m // idx
                if q1 * curr == str1 and q2 * curr == str2:
                    return str1[:idx]
            idx -= 1

        return ""