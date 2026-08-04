class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def binary_search(nums):

            start, end = 0, len(nums) - 1
            while start <= end:

                mid = (start + end) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    end = mid - 1
                else:
                    start = mid + 1
                
            return -1
        
        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            
            if matrix[row][0] <= target <= matrix[row][cols-1]:
                res = binary_search(matrix[row])
                return False if res == -1 else True
        
        return False