class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        n = len(s)
        i = 0
        while i < n:
            j = i
            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            start = j+1
            end = start+length
            curr = s[start: end]
            res.append(curr)
            i = end
        
        return res
