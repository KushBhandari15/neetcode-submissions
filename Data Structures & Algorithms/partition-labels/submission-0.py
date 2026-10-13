class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        helper = {}
        # maps char to last seen index
        for i in range(len(s)):
            helper[s[i]] = i
        res = []
        i = 0
        while i < len(s):
            start = i
            end = helper[s[i]]

            while start < end:
                end = max(end, helper[s[start]])
                start += 1
                
            res.append(end - i + 1)
            i = end + 1
        
        return res