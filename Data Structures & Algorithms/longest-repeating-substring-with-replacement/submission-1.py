class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        i, res = 0, 0
        helper = {}
        max_freq = 0
        for j in range(len(s)):

            helper[s[j]] = helper.get(s[j], 0) + 1
            max_freq = max(max_freq, helper[s[j]])

            while (j - i + 1) - max_freq > k:
                helper[s[i]] -= 1
                i += 1

            res = max(res, j - i + 1)

        return res
            
            

            


