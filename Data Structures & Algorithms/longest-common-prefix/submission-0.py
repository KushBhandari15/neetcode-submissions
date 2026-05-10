class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        n = len(strs)
        m = len(strs[0])
        common = strs[0]
        for i in range (n):
            curr_comm = ""
            for j in range(m):
                if j >= len(strs[i]) or strs[0][j] != strs[i][j]:
                    break
                if strs[0][j] == strs[i][j]:
                    curr_comm += strs[0][j]
            if len(common) > len(curr_comm):
                common = curr_comm
        
        return common