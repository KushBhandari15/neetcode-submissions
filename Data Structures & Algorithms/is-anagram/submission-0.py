class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)

        if n != m:
            return False
        
        helper = {}
        for i in range(n):
            curr_s = s[i]
            curr_t = t[i]
            if curr_s == curr_t:
                continue
            helper[curr_s] = helper.get(curr_s, 0) + 1
            helper[curr_t] = helper.get(curr_t, 0) - 1
            if helper[curr_t] == 0: del helper[curr_t]
            if helper[curr_s] == 0: del helper[curr_s]
        
        return True if not helper else False