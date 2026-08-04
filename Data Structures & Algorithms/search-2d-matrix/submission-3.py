class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])

        start, end = 0, rows*cols - 1

        while start <= end:

            mid = (start + end) // 2

            r = mid // cols
            c = mid % cols

            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                end = mid - 1
            else:
                start = mid + 1
        
        return False

        