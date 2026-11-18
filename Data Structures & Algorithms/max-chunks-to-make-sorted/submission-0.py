class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        res = 0
        subset = set()
        sorted_arr = sorted(arr)
        for j in range(len(arr)):
            if not subset: 
                res += 1
            if arr[j] in subset:
                subset.remove(arr[j])
            else:
                subset.add(arr[j])
            if sorted_arr[j] in subset:
                subset.remove(sorted_arr[j])
            else:
                subset.add(sorted_arr[j])

        return res