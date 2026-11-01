class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        rows, cols = len(matrix), len(matrix[0])
        
        i, j = 0, 0
        x, y = 0, 1

        while len(res) < rows * cols:
            if not (0 <= i < rows 
                and 0 <= j < cols) or matrix[i][j] == -101:
            
                i -= x; j -= y
                temp = x
                x = y
                y = temp * -1
                i += x; j += y

            res.append(matrix[i][j])
            matrix[i][j] = -101
            i += x
            j += y
        
        return res

            
                
            