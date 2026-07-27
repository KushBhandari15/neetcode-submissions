class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = [[1]]
    
        for row in range(1, numRows):
            curr = [0] * (row+1)
            curr[0], curr[row] = 1, 1 # Boundaries are always 1
            for col in range(1, row):
                # Sum of prev row's up and left element
                curr[col] = res[row-1][col-1] + res[row-1][col]
            
            res.append(curr)
        
        return res
    