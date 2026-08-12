from collections import Counter
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        counter = Counter()
        for num in arr:
            counter[num] += 1
        
        res = []
        for i in range(len(arr)-1):
            counter[arr[i]] -= 1
            if counter[arr[i]] == 0:
                del counter[arr[i]]
            res.append(max(counter))
        
        res.append(-1)
        return res
        
