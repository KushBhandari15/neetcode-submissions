class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        grid = []

        for c in range(len(matrix[0])):
            row = []
            for r in range(len(matrix)):
                row.append(matrix[r][c])
            grid.append(row)
        
        return grid