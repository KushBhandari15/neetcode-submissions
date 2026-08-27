class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        dist = 0
        for i in range(0, k):
            dist += abs(arr[i] - x)
        best_dist = dist
        best_left = 0
        left, right = 1, k

        while right < len(arr):
            curr = dist - abs(arr[left-1] - x) + abs(arr[right] - x)
            if curr < dist:
                best_dist = curr
                best_left = left
            dist = curr
            left += 1
            right += 1

        return arr[best_left: best_left + k]

        
                    