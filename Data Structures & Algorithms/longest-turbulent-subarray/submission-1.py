class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        n = len(arr)
        if n <= 1:
            return 1

        i = 0
        while i + 1 < n and arr[i] == arr[i + 1]:
            i += 1
        if i == n - 1:
            return 1
            
        j = i + 1
        increase = None
        res = j - i + 1

        for j in range(i + 1, n):
            if increase == None:
                increase = arr[i] < arr[j]
            elif arr[j] > arr[j - 1]:
                if increase:
                    i = j - 1
                increase = True
            elif arr[j] < arr[j - 1]:
                if not increase:
                    i = j - 1
                increase = False
            else:
                i = j
                increase = None

            res = max(res, j - i + 1)
    
        return res
