class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        res = ""
        n, m = len(str1), len(str2)
        i, j = 0, 0
        prefix_idx = 0
        while i < n and j < m:
            if str1[i] == str2[j]:
                prefix_idx += 1
                i += 1
                j += 1
            else:
                break
        
        prefix = str1[:prefix_idx + 1]

        idx = len(prefix)
        while idx > 0:
            curr = prefix[:idx]
            if n % idx == 0 and m % idx == 0:
                q1 = n // idx; q2 = m // idx
                if q1 * curr == str1 and q2 * curr == str2:
                    return curr
            idx -= 1

        return ""