class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        track = set()
        for i in range(len(strs)):
            first = strs[i]
            if first in track:
                continue
            n = len(first)
            first_map = {}
            curr_list = [first]
            for letter in first:
                first_map[letter] = first_map.get(letter, 0) + 1 
            for j in range(i+1, len(strs)):
                second = strs[j]
                m = len(second)
                if n != m:
                    continue
                second_map = {}
                for i in range (m):
                    second_map[second[i]] = second_map.get(second[i], 0) + 1
                if second_map == first_map:
                    curr_list.append(second)
                    track.add(second)
            res.append(curr_list)

        return res