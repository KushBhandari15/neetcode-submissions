class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = len(matrix)
        cols = len(matrix[0])

        rows_to_clean = set()
        cols_to_clean = set()

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    rows_to_clean.add(r)
                    cols_to_clean.add(c)

        for row in rows_to_clean:
            matrix[row] = [0] * cols
        for col in cols_to_clean:
            for row in matrix:
                row[col] = 0
