class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False
        first_col_zero = False
        
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_zero = True
                break
                
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_zero = True
                break

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        for i in range(1, rows):
            if matrix[i][0] == 0:
                for c in range(cols):
                    matrix[i][c] = 0
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for row in matrix:
                    row[j] = 0
        
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0

