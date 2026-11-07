class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        res = ""
        n, m = len(str1), len(str2)
        i, j = 0, 0
        prefix = ""
        while i < n and j < m:
            if str1[i] == str2[j]:
                prefix += str1[i]
                i += 1
                j += 1
            else:
                break

        idx = len(prefix)
        while idx > 0:
            print(f"Trying: {prefix[:idx]}")
            if n % idx == 0 and m % idx == 0:
                print("Passed checkpoint 1")
                q1 = n // idx; q2 = m // idx
                print(q1 * prefix[:idx], q2 * prefix[:idx])
                if q1*prefix[:idx] == str1 and q2*prefix[:idx] == str2:
                    return prefix[:idx]
            idx -= 1

        return ""